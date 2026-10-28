<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/banner-light.svg">
  <img alt="video-director: Turn a one-line idea into a shot-by-shot prompt for AI video models (Kling, Veo, Sora and others), with camera, lighting and motion vocabulary." src="assets/banner.svg" width="1280" height="320">
</picture>

# video-director: промпты для ИИ-видео под Kling, Veo 3, Wan и Runway

[![License: MIT](https://img.shields.io/badge/license-MIT-d1fe17?style=flat-square&labelColor=0d0f12)](LICENSE)
[![Claude Code skill](https://img.shields.io/badge/Claude_Code-skill-d1fe17?style=flat-square&labelColor=0d0f12)](#установка)
[![Cursor](https://img.shields.io/badge/Cursor-rules-d1fe17?style=flat-square&labelColor=0d0f12)](#установка)
[![Codex](https://img.shields.io/badge/Codex-AGENTS.md-d1fe17?style=flat-square&labelColor=0d0f12)](#установка)
[![Zero dependencies](https://img.shields.io/badge/dependencies-0-d1fe17?style=flat-square&labelColor=0d0f12)](#установка)

**На входе идея, на выходе посекундная раскадровка, собранная в промпт в формате каждой модели.**

[Быстрый старт](#быстрый-старт) · [Как это работает](#как-это-работает) · [Примеры](#примеры) · [Установка](#установка) · [FAQ](#faq)

</div>

[English](README.md) · Русский · [简体中文](README.zh-CN.md) · [Español](README.es.md) · [Português (BR)](README.pt-BR.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

Промпты для ИИ-видео под Kling 3.0, Veo 3, Wan 2.5, Seedance и Runway, написанные так, как их читают модели: раскадровка с таймингом (0-2 с, 2-4 с, ...), одно движение камеры на бит, объектив, схема света, одно предложение про физику движения, три слоя звука и короткий негативный список. Затем всё это рендерится под каждую модель с учётом её лимита длины, поддержки негативного промпта и звука. Работает для text-to-video и image-to-video. Поставляется как скилл для Claude Code, правило для Cursor и сниппет для Codex / `AGENTS.md`, плюс Python-скрипт на стандартной библиотеке, который можно запускать без агента.

| **Сначала раскадровка** | **Рендер под каждую модель** | **Словарь, который работает** |
|:---|:---|:---|
| Скрипт создаёт сетку битов и отказывается рендерить, пока не заполнены все слоты и не сходится таймлайн. | Одна раскадровка становится мультишот-промптом для Kling, одним непрерывным планом с диалогом в кавычках для Veo, промптом на 800 символов для Wan, нумерованными кадрами для Seedance или промптом без негативов для Runway. | Восемь справочных таблиц (камера, объектив, свет, физика, звук, негативы, лимиты моделей, формат), из которых берут слова агент и команда `vocab`. |

## Быстрый старт

```bash
git clone https://github.com/uniqaiapp/video-director
cd video-director
python3 scripts/storyboard.py new --idea "latte art at dawn" -o board.json   # scaffold with [[fill: ...]] slots
python3 scripts/storyboard.py check examples/latte-art-dawn.json --model kling
python3 scripts/storyboard.py render examples/latte-art-dawn.json --model kling
```

Первая команда записывает каркас раскадровки с сеткой битов по 2 секунды и заранее подставленными подсказками по объективу, свету и физике (идея читается как макро и золотой час). Агент, или вы сами, заполняет слоты; `check` проверяет; `render` печатает промпт, его негативное поле и примечания для выбранной модели.

## Демо

<img alt="video-director demo: scaffold a storyboard, check an example, render it for Kling 3.0" src="assets/demo.svg" width="820">

## Как это работает

1. **Каркас.** `new` превращает идею в JSON: биты каждые 2 секунды (последний забирает остаток), маркеры `[[fill: ...]]` для субъекта, места, стиля и каждого бита, а также подсказки по ключевым словам для объектива, камеры, света, физики и звука, когда идея очевидно макро, аэросъёмка, ночь, портрет, продукт, под водой, погоня или sci-fi.
2. **Заполнение.** Скилл (`SKILL.md`) объясняет агенту, как это делать: одно событие на бит, первый бит задаёт сцену, последний держит кадр, одно движение камеры на два бита, конкретные существительные, физика одним предложением, звук тремя фразами, негативы существительными. Словарь берётся из `references/`.
3. **Проверка.** Структурные ошибки (незаполненные слоты, разрывы в таймлайне, промпт длиннее жёсткого лимита) валят проверку; несовпадения с моделью дают предупреждение: Veo умеет только 4/6/8 с, Wan и Runway 5/10 с, Runway игнорирует негативы и не делает звук, монтажная склейка на одношотовой модели.
4. **Рендер.** Та же раскадровка в формате каждой модели. Kling читает субъект, облик, кадры с таймингом, движение, звук; Veo получает "one continuous take" с битами, соединёнными через "Then", диалог в кавычках и `subtitles, captions` в негативном поле, потому что иначе она вжигает субтитры в кадр; Wan получает сжатую раскладку; Seedance получает `Shot 1 (0-2s): ...`; Runway получает камеру первой и только позитивные формулировки.

```
idea ──new──▶ board.json ──fill (agent)──▶ check ──▶ render --model kling | veo | wan | seedance | runway
                                             ▲                   │
                                             └── fix one field ◀─┘  (floating → physics, flat → light, artefacts → negative)
```

Лимиты моделей живут в одной таблице (`python3 scripts/storyboard.py models`) с датой, когда они были сверены с документацией вендора; источники в `references/model-notes.md`. В репозитории нет оценок качества и бенчмарков: скрипт следит за структурой и лимитами, качество клипа зависит от битов.

## Примеры

Двенадцать раскадровок в [`examples/`](examples/README.md), у каждой есть Markdown-страница с таймлайном и отрендеренным промптом для каждой модели. Тесты побайтово сравнивают каждую страницу с результатом `render --model all --format md`, так что страницы не могут разойтись со скриптом.

<details>
<summary><b>Неоновая улица под дождём (Veo 3, 8 с, вертикаль, диалог): раскадровка → промпт</b></summary>

**Раскадровка** (`examples/neon-rain-street.json`, сокращённо)

```text
0-2s  she stands under the awning watching the rain, neon reflections sliding across her coat   | slow push-in at eye level, framed waist-up
2-4s  a car passes, its headlights sweep across her face; she turns to the camera                | continue the push-in
4-6s  she says the line, half smiling                                                            | hold on a medium close-up
6-8s  she steps out into the rain and opens the umbrella                                         | slow tilt up following the umbrella
physics: rain falls in straight lines and bounces off the awning edge; her coat is wet and heavy; the umbrella opens with a snap and settles
sound:   steady rain, tyres on wet asphalt, a distant siren | umbrella snapping open | She says, quietly, lip-synced: "You're late. Again."
```

**Промпт для Veo 3** (`render --model veo`)

```text
A woman in her thirties in a dark raincoat, wet hair pushed back, holding a closed umbrella in a narrow city street at night in heavy rain, neon shop signs reflected in the wet asphalt. Anamorphic, teal and magenta grade, Kodak 500T grain in the shadows. 35mm anamorphic, f/2, oval bokeh. Magenta and cyan neon practicals as key, cool fill from the sky, rim from a passing car. One continuous take over 8 seconds. She stands under the awning watching the rain, neon reflections sliding across her coat. Camera: slow push-in at eye level, framed waist-up. Then a car passes, its headlights sweep across her face; she turns to the camera. Camera: continue the push-in. Then she says the line, half smiling. Camera: hold on a medium close-up. Then she steps out into the rain and opens the umbrella. Camera: slow tilt up following the umbrella. Motion: rain falls in straight lines and bounces off the awning edge; her coat is wet and heavy; the umbrella opens with a snap and settles. Audio. Ambience: steady rain, tyres on wet asphalt, a distant siren. Sound effects: umbrella snapping open. Dialogue: She says, quietly, lip-synced: "You're late. Again."
```

Негативное поле: `morphing, extra limbs, warped hands, flicker, text, watermark, logo, jump cuts, frame jitter, subtitles, captions`

Полная страница со всеми моделями: [examples/neon-rain-street.md](examples/neon-rain-street.md).

</details>

<details>
<summary><b>Кроссовок на поворотном столе (Runway Gen-4, 5 с, image-to-video): что отбрасывается и почему</b></summary>

Runway читает только позитивные формулировки и не умеет генерировать звук, поэтому `render --model runway` ставит движение камеры первым, сохраняет биты и физику, а негативный список и блок звука отбрасывает. Примечания говорят об этом прямо, а `check --model runway` печатает те же два предупреждения. В раскадровке и то и другое остаётся для монтажа.

```text
Slow 90-degree orbit, clockwise, at shoe height: A white leather sneaker with a gum sole, laces tied, pristine in a seamless light-grey studio backdrop, slow gradient to white. The sneaker sits on a matte turntable, three-quarter view, and begins to rotate. Camera: slow 90-degree orbit, clockwise, at shoe height. Then the rotation reveals the side profile and the stitching. Camera: continue the orbit. Then the shoe comes to rest facing the camera. Camera: hold. Motion: rigid object; reflections on the leather slide smoothly as it rotates; no deformation; the turntable motion is constant. Clean high-key commercial look, neutral colour.
```

Полная страница: [examples/sneaker-turntable.md](examples/sneaker-turntable.md).

</details>

<details>
<summary><b>Погоня в пустыне (Kling 3.0, 10 с): намеренная склейка и что о ней говорят одношотовые модели</b></summary>

Бит 4 это «cut to an interior over-the-shoulder shot» (склейка на план из салона через плечо). Kling 3.0 воспринимает биты с таймингом как отдельные кадры, поэтому промпт сохраняет склейку. `check --model veo` отвечает так:

```text
WARN   desert-car-chase.json: Veo 3 / 3.1: 10s is not an available length (4/6/8 s); nearest is 8s, re-time the beats
WARN   desert-car-chase.json: Veo 3 / 3.1 is single-shot: beat 4 asks for a cut, which it cannot do; merge it into the previous beat or change the angle gradually
OK     desert-car-chase.json: 5 beats, 10s, 2 warning(s) for Veo 3 / 3.1
```

Полная страница: [examples/desert-car-chase.md](examples/desert-car-chase.md).

</details>

| Раскадровка | Модель | Что показывает |
|---|---|---|
| [latte-art-dawn](examples/latte-art-dawn.md) | Kling 3.0, 8 с | базовый случай: один субъект, один источник света, одна жидкость |
| [candle-confession](examples/candle-confession.md) | Veo 3, 8 с | единственный источник света, бит с диалогом на 3 секунды |
| [sci-fi-corridor-reveal](examples/sci-fi-corridor-reveal.md) | Veo 3, 8 с | смена света как событие |
| [coastline-drone-dawn](examples/coastline-drone-dawn.md) | Wan 2.5, 10 с | пять аэробитов в пределах лимита 800 символов |
| [ramen-steam-macro](examples/ramen-steam-macro.md) | Wan 2.5, 5 с, 9:16 | макро, физика пара и жидкости |
| [fashion-tunnel-walk](examples/fashion-tunnel-walk.md) | Kling 3.0, 10 с, 9:16 | image-to-video, физика походки и шёлка |
| [cat-window-rain](examples/cat-window-rain.md) | Seedance 2.0, 5 с | микродвижение, нумерованные кадры |
| [jellyfish-drift](examples/jellyfish-drift.md) | Seedance 2.0, 10 с | сопротивление воды, каустика, перевод фокуса |
| [rooftop-timelapse-dusk](examples/rooftop-timelapse-dusk.md) | generic, 12 с | биты по 3 секунды; предупреждения о длине для Veo, Wan, Runway |

## Установка

Работает с любым агентом, который читает файлы инструкций. Python 3.9+ (или любой Python 3, который у вас уже есть). Пакеты ставить не нужно.

<details open>
<summary><b>Claude Code</b></summary>

```bash
# user-level
git clone https://github.com/uniqaiapp/video-director ~/.claude/skills/video-director
# or project-level
git clone https://github.com/uniqaiapp/video-director .claude/skills/video-director
```

Дальше `/video-director` в любой сессии, или просто опишите клип; скилл срабатывает по своему `description`. `npx skills add uniqaiapp/video-director` тоже заработает, как только репозиторий станет публичным. Как плагин, когда будет опубликован маркетплейс uniqaiapp: `/plugin marketplace add uniqaiapp/skills`, затем `/plugin install video-director@uniqaiapp`.

</details>

<details>
<summary><b>Cursor</b></summary>

Скопируйте `SKILL.md`, `scripts/`, `references/` и [`.cursor/rules/video-director.mdc`](.cursor/rules/video-director.mdc) в свой проект. Файл правила встраивает скилл через `@SKILL.md`.

</details>

<details>
<summary><b>Codex / любой агент с AGENTS.md</b></summary>

Скопируйте `SKILL.md`, `scripts/` и `references/` в `.agents/skills/video-director/` и добавьте сниппет из [`codex/INSTRUCTIONS.md`](codex/INSTRUCTIONS.md) в свой `AGENTS.md`. Собственный [`AGENTS.md`](AGENTS.md) репозитория это универсальная версия.

</details>

<details>
<summary><b>Без агента</b></summary>

Каждая команда работает автономно: `python3 scripts/storyboard.py --help`. Вставьте [`SKILL.md`](SKILL.md) в системный промпт любой модели; кроме frontmatter, в нём нет синтаксиса, привязанного к конкретному агенту.

</details>

## Использование

```bash
python3 scripts/storyboard.py models                                   # limits table with its check date
python3 scripts/storyboard.py new --idea "..." --duration 8 --model veo --aspect 9:16 -o board.json
python3 scripts/storyboard.py vocab camera orbit                      # also: lens, light, physics, sound, negative
python3 scripts/storyboard.py check board.json --model veo
python3 scripts/storyboard.py render board.json --model veo           # or kling,wan  or  all --format md -o board.md
```

Где запускать промпт: Kling 3.0, Veo 3 и Wan 2.5 доступны рядом друг с другом в [генераторе видео по тексту UniqAI](https://uniqai.app/video/text-to-video?utm_source=github&utm_medium=readme-ru&utm_campaign=video-director), так что одну раскадровку можно попробовать на трёх моделях с одной страницы; любой другой интерфейс или API работает так же, промпт это обычный текст.

## FAQ

<details>
<summary><b>Какую модель выбрать?</b></summary>

Важны диалог или звук: Veo 3 (самый сильный нативный звук, но максимум 8 с). Нужна склейка внутри клипа или 10-15 с: Kling 3.0 или Seedance 2.0 (мультишот). Стартовое изображение и продукт: Runway Gen-4 или Kling. Дешёвый первый проход: Wan 2.5, промпт держите коротким. Команда `check` скажет, что не влезет, до того как вы потратите кредиты.

</details>

<details>
<summary><b>Клип плывёт, скользит или морфится. Что менять?</b></summary>

По одному полю за раз: если объект плывёт или скользит, это `physics` («feet plant firmly on each step», «the cup rests on the saucer»); морфинг обычно означает слишком много событий, так что уберите бит или превратите последний в удержание кадра; артефакты идут в `negative` существительными. Перепроверьте, перерендерьте. Фразы есть в `references/motion-physics.md`.

</details>

<details>
<summary><b>Лимиты моделей актуальны?</b></summary>

Они сверены с документацией каждого вендора на дату, которую печатает `python3 scripts/storyboard.py models`, и перечислены с источниками в `references/model-notes.md`. Вендоры меняют лимиты без предупреждения. Если проверка расходится со страницей вендора, верьте странице и откройте issue или PR с URL и датой.

</details>

<details>
<summary><b>Работает ли это для Sora, Hailuo, Luma, Pika?</b></summary>

Используйте `--model generic`: полный структурированный промпт с отдельным негативным списком, который вы вручную урезаете под лимит модели. `sora` принимается как псевдоним `generic`, потому что OpenAI закрыла Sora в 2026 году и живой цели для форматирования нет. PR с новой моделью должен содержать её задокументированные лимиты с источником.

</details>

## Смежные проекты

- [awesome-ai-video-prompts](https://github.com/uniqaiapp/awesome-ai-video-prompts): подборка промптов для ИИ-видео по категориям, с настройками, на которых они были сгенерированы, в JSON и Markdown.
- [ai-video-pricing](https://github.com/uniqaiapp/ai-video-pricing): проверенная вручную таблица цен на генерацию ИИ-видео, за секунду и за клип, с URL источника и датой проверки в каждой строке.
- [ugc-ad-director](https://github.com/uniqaiapp/ugc-ad-director): сценарий и список кадров для коротких UGC-роликов на ИИ-видео: хук, доказательство, оффер, с промптами под каждую модель.
- [no-plastic](https://github.com/uniqaiapp/no-plastic): правила промптов и чекер для естественных ИИ-портретов: текстура кожи, свет и выбор объектива без пластикового вида.

## Участие в проекте

Issues и pull request приветствуются. Делайте изменения небольшими и прикладывайте к описанию PR раскадровку вместе с отрендеренным промптом. Локальные проверки описаны в [CONTRIBUTING.md](CONTRIBUTING.md) (`python3 tests/run.py`, без зависимостей).

## Лицензия

Код и примеры: [MIT](LICENSE). Словарь в `references/`: CC BY 4.0, атрибуция "UniqAI, github.com/uniqaiapp/video-director". © UniqAI

---

<div align="center">

<sub>Проект <a href="https://uniqai.app/?utm_source=github&utm_medium=readme-ru&utm_campaign=video-director">UniqAI</a>, приложения для ИИ-фото, видео и чата: Kling 3.0, Veo 3, Flux, Nano Banana и GPT-5/Claude/Gemini/Grok в одном месте. Мы написали этот скилл, чтобы перестать заново объяснять себе движения камеры.</sub>

</div>
