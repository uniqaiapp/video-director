<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/banner-light.svg">
  <img alt="video-director: Turn a one-line idea into a shot-by-shot prompt for AI video models (Kling, Veo, Sora and others), with camera, lighting and motion vocabulary." src="assets/banner.svg" width="1280" height="320">
</picture>

# video-director: prompts de video con IA para Kling, Veo 3, Wan y Runway

[![License: MIT](https://img.shields.io/badge/license-MIT-d1fe17?style=flat-square&labelColor=0d0f12)](LICENSE)
[![Claude Code skill](https://img.shields.io/badge/Claude_Code-skill-d1fe17?style=flat-square&labelColor=0d0f12)](#instalación)
[![Cursor](https://img.shields.io/badge/Cursor-rules-d1fe17?style=flat-square&labelColor=0d0f12)](#instalación)
[![Codex](https://img.shields.io/badge/Codex-AGENTS.md-d1fe17?style=flat-square&labelColor=0d0f12)](#instalación)
[![Zero dependencies](https://img.shields.io/badge/dependencies-0-d1fe17?style=flat-square&labelColor=0d0f12)](#instalación)

**Entra una idea, sale un storyboard segundo a segundo, renderizado como prompt en el formato propio de cada modelo.**

[Inicio rápido](#inicio-rápido) · [Cómo funciona](#cómo-funciona) · [Ejemplos](#ejemplos) · [Instalación](#instalación) · [Preguntas frecuentes](#preguntas-frecuentes)

</div>

[English](README.md) · [Русский](README.ru.md) · [简体中文](README.zh-CN.md) · Español · [Português (BR)](README.pt-BR.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

Prompts de video con IA para Kling 3.0, Veo 3, Wan 2.5, Seedance y Runway, escritos tal como los leen los modelos: un storyboard con tiempos (0-2 s, 2-4 s, ...) con un movimiento de cámara por beat, un objetivo, un esquema de luz, una frase de física del movimiento, tres capas de sonido y una lista negativa corta; después se renderiza para cada modelo aplicando su límite de longitud, su manejo del prompt negativo y su soporte de audio. Funciona para texto a video e imagen a video. Se distribuye como skill de Claude Code, regla de Cursor y snippet para Codex / `AGENTS.md`, más un script de Python de biblioteca estándar que puedes ejecutar sin ningún agente.

| **Primero el storyboard** | **Renderizado por modelo** | **Vocabulario que funciona** |
|:---|:---|:---|
| El script genera una rejilla de beats y se niega a renderizar hasta que todos los campos están rellenos y la línea de tiempo cuadra. | Un mismo storyboard se convierte en un prompt multiplano para Kling, una toma única con diálogo entre comillas para Veo, un prompt de 800 caracteres para Wan, planos numerados para Seedance o un prompt solo positivo para Runway. | Ocho tablas de referencia (cámara, objetivo, luz, física, sonido, negativos, límites de modelo, formato) de las que beben el agente y el comando `vocab`. |

## Inicio rápido

```bash
git clone https://github.com/uniqaiapp/video-director
cd video-director
python3 scripts/storyboard.py new --idea "latte art at dawn" -o board.json   # scaffold with [[fill: ...]] slots
python3 scripts/storyboard.py check examples/latte-art-dawn.json --model kling
python3 scripts/storyboard.py render examples/latte-art-dawn.json --model kling
```

El primer comando escribe un esqueleto de storyboard con una rejilla de beats de 2 segundos y sugerencias ya rellenas de objetivo, luz y física (la idea se lee como macro y hora dorada). El agente, o tú, rellena los campos; `check` valida; `render` imprime el prompt, su campo negativo y las notas para ese modelo.

## Demo

<img alt="video-director demo: scaffold a storyboard, check an example, render it for Kling 3.0" src="assets/demo.svg" width="820">

## Cómo funciona

1. **Esqueleto.** `new` convierte la idea en JSON: beats cada 2 segundos (el último absorbe el resto), marcadores `[[fill: ...]]` para sujeto, escenario, estilo y cada beat, y sugerencias por palabra clave de objetivo, cámara, luz, física y sonido cuando la idea es claramente macro, aérea, nocturna, retrato, producto, submarina, persecución o ciencia ficción.
2. **Relleno.** La skill (`SKILL.md`) le dice al agente cómo: un evento por beat, el primer beat establece y el último sostiene, un movimiento de cámara cada dos beats, sustantivos concretos, la física en una frase, el sonido en tres sintagmas, los negativos como sustantivos. El vocabulario sale de `references/`.
3. **Comprobación.** Los errores estructurales (campos sin rellenar, huecos en la línea de tiempo, prompt por encima del tope) hacen fallar; los problemas de ajuste al modelo avisan: Veo solo admite 4/6/8 s, Wan y Runway 5/10 s, Runway ignora los negativos y no tiene audio, un corte en un modelo de plano único.
4. **Renderizado.** El mismo storyboard en el formato de cada modelo. Kling lee sujeto, look, planos con tiempos, movimiento, audio; Veo recibe "one continuous take" con los beats unidos por "Then", diálogo entre comillas y `subtitles, captions` añadido a su campo negativo porque, si no, incrusta subtítulos; Wan recibe el formato escueto; Seedance recibe `Shot 1 (0-2s): ...`; Runway recibe la cámara primero y solo frases positivas.

```
idea ──new──▶ board.json ──fill (agent)──▶ check ──▶ render --model kling | veo | wan | seedance | runway
                                             ▲                   │
                                             └── fix one field ◀─┘  (floating → physics, flat → light, artefacts → negative)
```

Los límites de los modelos viven en una sola tabla (`python3 scripts/storyboard.py models`) con la fecha en que se leyeron de la documentación de cada proveedor; `references/model-notes.md` tiene las fuentes. En este repositorio no hay puntuaciones de calidad ni benchmarks: el script impone estructura y límites, la calidad del clip depende de los beats.

## Ejemplos

Doce storyboards en [`examples/`](examples/README.md), cada uno con una página en Markdown que muestra la línea de tiempo y el prompt renderizado para cada modelo. Los tests comparan byte a byte cada página con `render --model all --format md`, así que no pueden desviarse del script.

<details>
<summary><b>Calle con neón bajo la lluvia (Veo 3, 8 s, vertical, diálogo): del storyboard al prompt</b></summary>

**Storyboard** (`examples/neon-rain-street.json`, abreviado)

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

Página completa con todos los modelos: [examples/neon-rain-street.md](examples/neon-rain-street.md).

</details>

<details>
<summary><b>Zapatilla en plato giratorio (Runway Gen-4, 5 s, imagen a video): qué se descarta y por qué</b></summary>

Runway solo lee frases positivas y no tiene audio nativo, así que `render --model runway` abre con el movimiento de cámara, conserva los beats y la física, y descarta la lista negativa y el bloque de sonido. Las notas lo indican, y `check --model runway` imprime los mismos dos avisos. El storyboard conserva ambos para la edición.

```text
Slow 90-degree orbit, clockwise, at shoe height: A white leather sneaker with a gum sole, laces tied, pristine in a seamless light-grey studio backdrop, slow gradient to white. The sneaker sits on a matte turntable, three-quarter view, and begins to rotate. Camera: slow 90-degree orbit, clockwise, at shoe height. Then the rotation reveals the side profile and the stitching. Camera: continue the orbit. Then the shoe comes to rest facing the camera. Camera: hold. Motion: rigid object; reflections on the leather slide smoothly as it rotates; no deformation; the turntable motion is constant. Clean high-key commercial look, neutral colour.
```

Página completa: [examples/sneaker-turntable.md](examples/sneaker-turntable.md).

</details>

<details>
<summary><b>Persecución en el desierto (Kling 3.0, 10 s): un corte deliberado y qué dicen de él los modelos de plano único</b></summary>

El beat 4 es "cut to an interior over-the-shoulder shot" (corte a un plano interior por encima del hombro). Kling 3.0 sigue los beats con tiempos como planos, así que el prompt lo conserva. `check --model veo` responde:

```text
WARN   desert-car-chase.json: Veo 3 / 3.1: 10s is not an available length (4/6/8 s); nearest is 8s, re-time the beats
WARN   desert-car-chase.json: Veo 3 / 3.1 is single-shot: beat 4 asks for a cut, which it cannot do; merge it into the previous beat or change the angle gradually
OK     desert-car-chase.json: 5 beats, 10s, 2 warning(s) for Veo 3 / 3.1
```

Página completa: [examples/desert-car-chase.md](examples/desert-car-chase.md).

</details>

| Storyboard | Modelo objetivo | Qué muestra |
|---|---|---|
| [latte-art-dawn](examples/latte-art-dawn.md) | Kling 3.0, 8 s | la base: un sujeto, una luz, un líquido |
| [candle-confession](examples/candle-confession.md) | Veo 3, 8 s | una única fuente de luz, un beat de diálogo de 3 segundos |
| [sci-fi-corridor-reveal](examples/sci-fi-corridor-reveal.md) | Veo 3, 8 s | un cambio de luz como evento |
| [coastline-drone-dawn](examples/coastline-drone-dawn.md) | Wan 2.5, 10 s | cinco beats aéreos por debajo del tope de 800 caracteres |
| [ramen-steam-macro](examples/ramen-steam-macro.md) | Wan 2.5, 5 s, 9:16 | macro, física del vapor y del líquido |
| [fashion-tunnel-walk](examples/fashion-tunnel-walk.md) | Kling 3.0, 10 s, 9:16 | imagen a video, física de la caminata y de la seda |
| [cat-window-rain](examples/cat-window-rain.md) | Seedance 2.0, 5 s | micromovimiento, planos numerados |
| [jellyfish-drift](examples/jellyfish-drift.md) | Seedance 2.0, 10 s | arrastre submarino, cáusticas, cambio de foco |
| [rooftop-timelapse-dusk](examples/rooftop-timelapse-dusk.md) | generic, 12 s | beats de 3 segundos; avisos de longitud en Veo, Wan y Runway |

## Instalación

Funciona con cualquier agente que lea archivos de instrucciones. Python 3.9+ (o cualquier Python 3 que ya tengas). No hay paquetes que instalar.

<details open>
<summary><b>Claude Code</b></summary>

```bash
# user-level
git clone https://github.com/uniqaiapp/video-director ~/.claude/skills/video-director
# or project-level
git clone https://github.com/uniqaiapp/video-director .claude/skills/video-director
```

Después escribe `/video-director` en cualquier sesión, o simplemente describe el clip; la `description` de la skill la activa. `npx skills add uniqaiapp/video-director` también funciona en cuanto el repositorio sea público. Como plugin, cuando se publique el marketplace de uniqaiapp: `/plugin marketplace add uniqaiapp/skills` y luego `/plugin install video-director@uniqaiapp`.

</details>

<details>
<summary><b>Cursor</b></summary>

Copia `SKILL.md`, `scripts/`, `references/` y [`.cursor/rules/video-director.mdc`](.cursor/rules/video-director.mdc) a tu proyecto. El archivo de regla incrusta la skill con `@SKILL.md`.

</details>

<details>
<summary><b>Codex / cualquier agente con AGENTS.md</b></summary>

Copia `SKILL.md`, `scripts/` y `references/` a `.agents/skills/video-director/` y añade el fragmento de [`codex/INSTRUCTIONS.md`](codex/INSTRUCTIONS.md) a tu `AGENTS.md`. El [`AGENTS.md`](AGENTS.md) del propio repositorio es la versión genérica.

</details>

<details>
<summary><b>Sin agente</b></summary>

Todos los comandos funcionan de forma independiente: `python3 scripts/storyboard.py --help`. Pega [`SKILL.md`](SKILL.md) en el system prompt de cualquier modelo; no tiene sintaxis específica de ningún agente fuera del frontmatter.

</details>

## Uso

```bash
python3 scripts/storyboard.py models                                   # limits table with its check date
python3 scripts/storyboard.py new --idea "..." --duration 8 --model veo --aspect 9:16 -o board.json
python3 scripts/storyboard.py vocab camera orbit                      # also: lens, light, physics, sound, negative
python3 scripts/storyboard.py check board.json --model veo
python3 scripts/storyboard.py render board.json --model veo           # or kling,wan  or  all --format md -o board.md
```

Dónde ejecutar el prompt: Kling 3.0, Veo 3 y Wan 2.5 están disponibles uno al lado del otro en el [compositor de texto a video de UniqAI](https://uniqai.app/video/text-to-video?utm_source=github&utm_medium=readme-es&utm_campaign=video-director), así que un mismo storyboard se puede probar en tres modelos desde la misma página; cualquier otro front end o API funciona igual, el prompt es texto plano.

## Preguntas frecuentes

<details>
<summary><b>¿Qué modelo elijo?</b></summary>

Diálogo o sonido que importa: Veo 3 (el audio nativo más sólido, pero 8 s como máximo). Un corte dentro del clip o 10-15 s: Kling 3.0 o Seedance 2.0 (multiplano). Una imagen inicial y un producto: Runway Gen-4 o Kling. Una primera pasada barata: Wan 2.5, con el prompt corto. El comando `check` te dice qué no va a encajar antes de gastar créditos.

</details>

<details>
<summary><b>El clip flota, se desliza o se deforma. ¿Qué cambio?</b></summary>

Un campo cada vez: flotar o deslizarse es `physics` ("feet plant firmly on each step", "the cup rests on the saucer"); la deformación suele ser demasiados eventos, así que quita un beat o convierte el último en un plano sostenido; los artefactos van en `negative` como sustantivos. Vuelve a comprobar, vuelve a renderizar. `references/motion-physics.md` tiene las frases.

</details>

<details>
<summary><b>¿Están al día los límites de los modelos?</b></summary>

Se leyeron de la documentación de cada proveedor en la fecha que imprime `python3 scripts/storyboard.py models` y están listados con sus fuentes en `references/model-notes.md`. Los proveedores cambian los límites sin avisar. Cuando la comprobación no coincida con la página del proveedor, fíate de la página y abre un issue o un PR con la URL y la fecha.

</details>

<details>
<summary><b>¿Funciona con Sora, Hailuo, Luma, Pika?</b></summary>

Usa `--model generic`: el prompt estructurado completo con una lista negativa aparte, que recortas a mano hasta el límite del modelo. `sora` se acepta como alias de `generic` porque OpenAI discontinuó Sora en 2026 y no hay un objetivo vivo para el que dar formato. Los PR que añadan un modelo necesitan sus límites documentados con una fuente.

</details>

## Relacionados

- [awesome-ai-video-prompts](https://github.com/uniqaiapp/awesome-ai-video-prompts): prompts seleccionados y categorizados para modelos de video con IA, con los ajustes que los produjeron, en JSON y Markdown.
- [ai-video-pricing](https://github.com/uniqaiapp/ai-video-pricing): tabla de precios verificada a mano para la generación de video con IA, por segundo y por clip, con URL de origen y fecha de comprobación en cada fila.
- [ugc-ad-director](https://github.com/uniqaiapp/ugc-ad-director): guion y lista de planos para anuncios cortos estilo UGC con video IA: gancho, prueba, oferta, con prompts de salida por modelo.
- [no-plastic](https://github.com/uniqaiapp/no-plastic): reglas de prompt y un comprobador para retratos con IA de aspecto natural: textura de piel, iluminación y elección de objetivo que evitan el aspecto plástico.

## Contribuir

Los issues y los pull requests son bienvenidos. Mantén los cambios pequeños e incluye un storyboard junto con su prompt renderizado en la descripción del PR. Consulta [CONTRIBUTING.md](CONTRIBUTING.md) para las comprobaciones locales (`python3 tests/run.py`, sin dependencias).

## Licencia

Código y ejemplos: [MIT](LICENSE). El vocabulario de `references/`: CC BY 4.0, atribución "UniqAI, github.com/uniqaiapp/video-director". © UniqAI

---

<div align="center">

<sub>Hecho por <a href="https://uniqai.app/?utm_source=github&utm_medium=readme-es&utm_campaign=video-director">UniqAI</a>, una app de foto, video y chat con IA: Kling 3.0, Veo 3, Flux, Nano Banana y GPT-5/Claude/Gemini/Grok en un solo lugar. Escribimos esta skill para dejar de explicarnos los movimientos de cámara a nosotros mismos.</sub>

</div>
