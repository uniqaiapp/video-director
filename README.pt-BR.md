<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/banner-light.svg">
  <img alt="video-director: Turn a one-line idea into a shot-by-shot prompt for AI video models (Kling, Veo, Sora and others), with camera, lighting and motion vocabulary." src="assets/banner.svg" width="1280" height="320">
</picture>

# video-director: prompts de vídeo com IA para Kling, Veo 3, Wan e Runway

[![License: MIT](https://img.shields.io/badge/license-MIT-d1fe17?style=flat-square&labelColor=0d0f12)](LICENSE)
[![Claude Code skill](https://img.shields.io/badge/Claude_Code-skill-d1fe17?style=flat-square&labelColor=0d0f12)](#instalação)
[![Cursor](https://img.shields.io/badge/Cursor-rules-d1fe17?style=flat-square&labelColor=0d0f12)](#instalação)
[![Codex](https://img.shields.io/badge/Codex-AGENTS.md-d1fe17?style=flat-square&labelColor=0d0f12)](#instalação)
[![Zero dependencies](https://img.shields.io/badge/dependencies-0-d1fe17?style=flat-square&labelColor=0d0f12)](#instalação)

**Entra uma ideia, sai um storyboard segundo a segundo, renderizado como prompt no formato de cada modelo.**

[Início rápido](#início-rápido) · [Como funciona](#como-funciona) · [Exemplos](#exemplos) · [Instalação](#instalação) · [Perguntas frequentes](#perguntas-frequentes)

</div>

[English](README.md) · [Русский](README.ru.md) · [简体中文](README.zh-CN.md) · [Español](README.es.md) · Português (BR) · [日本語](README.ja.md) · [한국어](README.ko.md)

Prompts de vídeo com IA para Kling 3.0, Veo 3, Wan 2.5, Seedance e Runway, escritos do jeito que os modelos leem: um storyboard com tempos marcados (0-2 s, 2-4 s, ...) com um movimento de câmera por beat, uma lente, um esquema de luz, uma frase de física do movimento, três camadas de som e uma lista negativa curta, depois renderizado para cada modelo respeitando seu limite de duração, o tratamento de prompt negativo e o suporte a áudio. Funciona para texto para vídeo e imagem para vídeo. Vem como skill do Claude Code, regra do Cursor e snippet para Codex / `AGENTS.md`, mais um script Python só com a biblioteca padrão, que roda sem nenhum agente.

| **Storyboard primeiro** | **Renderização por modelo** | **Vocabulário que funciona** |
|:---|:---|:---|
| O script monta uma grade de beats e se recusa a renderizar até que todos os campos estejam preenchidos e a linha do tempo feche. | Um storyboard vira um prompt multi-shot para Kling, um take único para Veo com diálogo entre aspas, um prompt de 800 caracteres para Wan, planos numerados para Seedance ou um prompt só positivo para Runway. | Oito tabelas de referência (câmera, lente, luz, física, som, negativos, limites dos modelos, formato) de onde o agente e o comando `vocab` puxam o vocabulário. |

## Início rápido

```bash
git clone https://github.com/uniqaiapp/video-director
cd video-director
python3 scripts/storyboard.py new --idea "latte art at dawn" -o board.json   # scaffold with [[fill: ...]] slots
python3 scripts/storyboard.py check examples/latte-art-dawn.json --model kling
python3 scripts/storyboard.py render examples/latte-art-dawn.json --model kling
```

O primeiro comando escreve o esqueleto de um storyboard com grade de beats de 2 segundos e dicas de lente, luz e física já preenchidas (a ideia é lida como macro e golden hour). O agente, ou você, preenche os campos; `check` valida; `render` imprime o prompt, o campo negativo e as observações para aquele modelo.

## Demo

<img alt="video-director demo: scaffold a storyboard, check an example, render it for Kling 3.0" src="assets/demo.svg" width="820">

## Como funciona

1. **Esqueleto.** `new` transforma a ideia em JSON: beats a cada 2 segundos (o último absorve o restante), marcadores `[[fill: ...]]` para sujeito, cenário, estilo e cada beat, além de dicas por palavra-chave para lente, câmera, luz, física e som quando a ideia é claramente macro, aérea, noturna, retrato, produto, subaquática, perseguição ou ficção científica.
2. **Preenchimento.** A skill (`SKILL.md`) diz ao agente como fazer: um evento por beat, o primeiro beat estabelece a cena e o último segura o plano, um movimento de câmera a cada dois beats, substantivos concretos, física em uma frase, som em três expressões, negativos como substantivos. O vocabulário vem de `references/`.
3. **Verificação.** Erros estruturais (campos não preenchidos, buracos na linha do tempo, prompt acima do limite rígido) reprovam; problemas de compatibilidade com o modelo geram aviso: Veo só faz 4/6/8 s, Wan e Runway 5/10 s, Runway ignora negativos e não tem áudio, um corte em um modelo de plano único.
4. **Renderização.** O mesmo storyboard no formato de cada modelo. Kling lê sujeito, visual, planos com tempo, movimento, áudio; Veo recebe "one continuous take" com os beats ligados por "Then", diálogo entre aspas e `subtitles, captions` acrescentados ao campo negativo, porque senão ele queima legendas no vídeo; Wan recebe o layout enxuto; Seedance recebe `Shot 1 (0-2s): ...`; Runway recebe a câmera primeiro e só frases positivas.

```
idea ──new──▶ board.json ──fill (agent)──▶ check ──▶ render --model kling | veo | wan | seedance | runway
                                             ▲                   │
                                             └── fix one field ◀─┘  (floating → physics, flat → light, artefacts → negative)
```

Os limites dos modelos ficam em uma única tabela (`python3 scripts/storyboard.py models`) com a data em que foram lidos na documentação do fornecedor; `references/model-notes.md` traz as fontes. Não há notas de qualidade nem benchmarks neste repositório: o script impõe estrutura e limites, a qualidade do clipe depende dos beats.

## Exemplos

Doze storyboards em [`examples/`](examples/README.md), cada um com uma página Markdown mostrando a linha do tempo e o prompt renderizado para todos os modelos. Os testes comparam byte a byte cada página com `render --model all --format md`, então elas não podem divergir do script.

<details>
<summary><b>Rua de neon na chuva (Veo 3, 8 s, vertical, diálogo): storyboard → prompt</b></summary>

**Storyboard** (`examples/neon-rain-street.json`, resumido)

```text
0-2s  she stands under the awning watching the rain, neon reflections sliding across her coat   | slow push-in at eye level, framed waist-up
2-4s  a car passes, its headlights sweep across her face; she turns to the camera                | continue the push-in
4-6s  she says the line, half smiling                                                            | hold on a medium close-up
6-8s  she steps out into the rain and opens the umbrella                                         | slow tilt up following the umbrella
physics: rain falls in straight lines and bounces off the awning edge; her coat is wet and heavy; the umbrella opens with a snap and settles
sound:   steady rain, tyres on wet asphalt, a distant siren | umbrella snapping open | She says, quietly, lip-synced: "You're late. Again."
```

**Prompt para Veo 3** (`render --model veo`)

```text
A woman in her thirties in a dark raincoat, wet hair pushed back, holding a closed umbrella in a narrow city street at night in heavy rain, neon shop signs reflected in the wet asphalt. Anamorphic, teal and magenta grade, Kodak 500T grain in the shadows. 35mm anamorphic, f/2, oval bokeh. Magenta and cyan neon practicals as key, cool fill from the sky, rim from a passing car. One continuous take over 8 seconds. She stands under the awning watching the rain, neon reflections sliding across her coat. Camera: slow push-in at eye level, framed waist-up. Then a car passes, its headlights sweep across her face; she turns to the camera. Camera: continue the push-in. Then she says the line, half smiling. Camera: hold on a medium close-up. Then she steps out into the rain and opens the umbrella. Camera: slow tilt up following the umbrella. Motion: rain falls in straight lines and bounces off the awning edge; her coat is wet and heavy; the umbrella opens with a snap and settles. Audio. Ambience: steady rain, tyres on wet asphalt, a distant siren. Sound effects: umbrella snapping open. Dialogue: She says, quietly, lip-synced: "You're late. Again."
```

Campo negativo: `morphing, extra limbs, warped hands, flicker, text, watermark, logo, jump cuts, frame jitter, subtitles, captions`

Página completa com todos os modelos: [examples/neon-rain-street.md](examples/neon-rain-street.md).

</details>

<details>
<summary><b>Tênis na plataforma giratória (Runway Gen-4, 5 s, imagem para vídeo): o que é descartado e por quê</b></summary>

O Runway lê apenas frases positivas e não tem áudio nativo, então `render --model runway` abre com o movimento de câmera, mantém os beats e a física e descarta a lista negativa e o bloco de som. As observações dizem isso, e `check --model runway` imprime os mesmos dois avisos. O storyboard guarda os dois para a edição.

```text
Slow 90-degree orbit, clockwise, at shoe height: A white leather sneaker with a gum sole, laces tied, pristine in a seamless light-grey studio backdrop, slow gradient to white. The sneaker sits on a matte turntable, three-quarter view, and begins to rotate. Camera: slow 90-degree orbit, clockwise, at shoe height. Then the rotation reveals the side profile and the stitching. Camera: continue the orbit. Then the shoe comes to rest facing the camera. Camera: hold. Motion: rigid object; reflections on the leather slide smoothly as it rotates; no deformation; the turntable motion is constant. Clean high-key commercial look, neutral colour.
```

Página completa: [examples/sneaker-turntable.md](examples/sneaker-turntable.md).

</details>

<details>
<summary><b>Perseguição de carros no deserto (Kling 3.0, 10 s): um corte deliberado, e o que os modelos de plano único dizem sobre ele</b></summary>

O beat 4 é "cut to an interior over-the-shoulder shot" (corte para um plano interno por cima do ombro). O Kling 3.0 segue beats com tempo como planos, então o prompt mantém o corte. `check --model veo` responde:

```text
WARN   desert-car-chase.json: Veo 3 / 3.1: 10s is not an available length (4/6/8 s); nearest is 8s, re-time the beats
WARN   desert-car-chase.json: Veo 3 / 3.1 is single-shot: beat 4 asks for a cut, which it cannot do; merge it into the previous beat or change the angle gradually
OK     desert-car-chase.json: 5 beats, 10s, 2 warning(s) for Veo 3 / 3.1
```

Página completa: [examples/desert-car-chase.md](examples/desert-car-chase.md).

</details>

| Storyboard | Alvo | Mostra |
|---|---|---|
| [latte-art-dawn](examples/latte-art-dawn.md) | Kling 3.0, 8 s | a linha de base: um sujeito, uma luz, um líquido |
| [candle-confession](examples/candle-confession.md) | Veo 3, 8 s | fonte de luz única, um beat de diálogo de 3 segundos |
| [sci-fi-corridor-reveal](examples/sci-fi-corridor-reveal.md) | Veo 3, 8 s | uma mudança de luz como evento |
| [coastline-drone-dawn](examples/coastline-drone-dawn.md) | Wan 2.5, 10 s | cinco beats aéreos dentro do limite de 800 caracteres |
| [ramen-steam-macro](examples/ramen-steam-macro.md) | Wan 2.5, 5 s, 9:16 | macro, física de vapor e líquido |
| [fashion-tunnel-walk](examples/fashion-tunnel-walk.md) | Kling 3.0, 10 s, 9:16 | imagem para vídeo, física de caminhada e seda |
| [cat-window-rain](examples/cat-window-rain.md) | Seedance 2.0, 5 s | micromovimento, planos numerados |
| [jellyfish-drift](examples/jellyfish-drift.md) | Seedance 2.0, 10 s | arrasto subaquático, cáusticas, rack focus |
| [rooftop-timelapse-dusk](examples/rooftop-timelapse-dusk.md) | generic, 12 s | beats de 3 segundos; avisos de duração para Veo, Wan e Runway |

## Instalação

Funciona com qualquer agente que leia arquivos de instruções. Python 3.9+ (ou qualquer Python 3 que você já tenha). Nenhum pacote para instalar.

<details open>
<summary><b>Claude Code</b></summary>

```bash
# user-level
git clone https://github.com/uniqaiapp/video-director ~/.claude/skills/video-director
# or project-level
git clone https://github.com/uniqaiapp/video-director .claude/skills/video-director
```

Depois, `/video-director` em qualquer sessão, ou simplesmente descreva o clipe; a `description` da skill a aciona. `npx skills add uniqaiapp/video-director` também funciona assim que o repositório estiver público. Como plugin, quando o marketplace uniqaiapp for publicado: `/plugin marketplace add uniqaiapp/skills` e depois `/plugin install video-director@uniqaiapp`.

</details>

<details>
<summary><b>Cursor</b></summary>

Copie `SKILL.md`, `scripts/`, `references/` e [`.cursor/rules/video-director.mdc`](.cursor/rules/video-director.mdc) para o seu projeto. O arquivo de regra incorpora a skill com `@SKILL.md`.

</details>

<details>
<summary><b>Codex / qualquer agente que leia AGENTS.md</b></summary>

Copie `SKILL.md`, `scripts/` e `references/` para `.agents/skills/video-director/` e adicione o snippet de [`codex/INSTRUCTIONS.md`](codex/INSTRUCTIONS.md) ao seu `AGENTS.md`. O [`AGENTS.md`](AGENTS.md) deste repositório é a versão genérica.

</details>

<details>
<summary><b>Sem agente</b></summary>

Todos os comandos rodam sozinhos: `python3 scripts/storyboard.py --help`. Cole [`SKILL.md`](SKILL.md) no system prompt de qualquer modelo; ele não tem sintaxe específica de agente fora do frontmatter.

</details>

## Uso

```bash
python3 scripts/storyboard.py models                                   # limits table with its check date
python3 scripts/storyboard.py new --idea "..." --duration 8 --model veo --aspect 9:16 -o board.json
python3 scripts/storyboard.py vocab camera orbit                      # also: lens, light, physics, sound, negative
python3 scripts/storyboard.py check board.json --model veo
python3 scripts/storyboard.py render board.json --model veo           # or kling,wan  or  all --format md -o board.md
```

Onde rodar o prompt: Kling 3.0, Veo 3 e Wan 2.5 ficam lado a lado no [compositor de texto para vídeo da UniqAI](https://uniqai.app/video/text-to-video?utm_source=github&utm_medium=readme-pt-br&utm_campaign=video-director), então um mesmo storyboard pode ser testado em três modelos a partir da mesma página; qualquer outro front-end ou API funciona da mesma forma, o prompt é texto puro.

## Perguntas frequentes

<details>
<summary><b>Qual modelo escolher?</b></summary>

Diálogo ou som que importa: Veo 3 (o áudio nativo mais forte, mas no máximo 8 s). Um corte dentro do clipe ou 10-15 s: Kling 3.0 ou Seedance 2.0 (multi-shot). Uma imagem inicial e um produto: Runway Gen-4 ou Kling. Uma primeira passada barata: Wan 2.5, com prompt curto. O comando `check` avisa o que não vai caber antes de você gastar créditos.

</details>

<details>
<summary><b>O clipe flutua, desliza ou deforma. O que eu mudo?</b></summary>

Um campo por vez: flutuar ou deslizar é `physics` ("feet plant firmly on each step", "the cup rests on the saucer"); deformação (morphing) costuma ser excesso de eventos, então remova um beat ou transforme o último em um plano parado; artefatos vão em `negative` como substantivos. Verifique de novo, renderize de novo. `references/motion-physics.md` tem as expressões.

</details>

<details>
<summary><b>Os limites dos modelos estão atualizados?</b></summary>

Foram lidos na documentação de cada fornecedor na data impressa por `python3 scripts/storyboard.py models` e listados com as fontes em `references/model-notes.md`. Os fornecedores mudam limites sem aviso. Quando a verificação discordar da página do fornecedor, confie na página e abra uma issue ou um PR com a URL e a data.

</details>

<details>
<summary><b>Funciona com Sora, Hailuo, Luma, Pika?</b></summary>

Use `--model generic`: o prompt estruturado completo com a lista negativa separada, que você corta à mão até o limite do modelo. `sora` é aceito como alias de `generic` porque a OpenAI descontinuou o Sora em 2026 e não há mais um alvo ativo para formatar. PRs que adicionem um modelo precisam dos limites documentados com fonte.

</details>

## Relacionados

- [awesome-ai-video-prompts](https://github.com/uniqaiapp/awesome-ai-video-prompts): prompts curados e categorizados para modelos de vídeo com IA, com as configurações que os produziram, em JSON e Markdown.
- [ai-video-pricing](https://github.com/uniqaiapp/ai-video-pricing): tabela de preços conferida à mão para geração de vídeo com IA, por segundo e por clipe, com URL da fonte e data de verificação em cada linha.
- [ugc-ad-director](https://github.com/uniqaiapp/ugc-ad-director): roteiro e lista de planos para anúncios curtos no estilo UGC com vídeo IA: gancho, prova, oferta, com saída de prompt por modelo.
- [no-plastic](https://github.com/uniqaiapp/no-plastic): regras de prompt e um verificador para retratos com IA de aparência natural: textura de pele, iluminação e escolhas de lente que evitam o visual plastificado.

## Contribuindo

Issues e pull requests são bem-vindos. Mantenha as mudanças pequenas e inclua um storyboard com o prompt renderizado na descrição do PR. Veja [CONTRIBUTING.md](CONTRIBUTING.md) para as verificações locais (`python3 tests/run.py`, sem dependências).

## Licença

Código e exemplos: [MIT](LICENSE). O vocabulário em `references/`: CC BY 4.0, atribuição "UniqAI, github.com/uniqaiapp/video-director". © UniqAI

---

<div align="center">

<sub>Feito pela <a href="https://uniqai.app/?utm_source=github&utm_medium=readme-pt-br&utm_campaign=video-director">UniqAI</a>, um app de foto, vídeo e chat com IA: Kling 3.0, Veo 3, Flux, Nano Banana e GPT-5/Claude/Gemini/Grok em um só lugar. Escrevemos esta skill para parar de explicar movimentos de câmera para nós mesmos.</sub>

</div>
