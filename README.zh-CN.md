<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/banner-light.svg">
  <img alt="video-director: Turn a one-line idea into a shot-by-shot prompt for AI video models (Kling, Veo, Sora and others), with camera, lighting and motion vocabulary." src="assets/banner.svg" width="1280" height="320">
</picture>

# video-director：Kling、Veo 3、Wan、Runway 的 AI 视频提示词

[![License: MIT](https://img.shields.io/badge/license-MIT-d1fe17?style=flat-square&labelColor=0d0f12)](LICENSE)
[![Claude Code skill](https://img.shields.io/badge/Claude_Code-skill-d1fe17?style=flat-square&labelColor=0d0f12)](#安装)
[![Cursor](https://img.shields.io/badge/Cursor-rules-d1fe17?style=flat-square&labelColor=0d0f12)](#安装)
[![Codex](https://img.shields.io/badge/Codex-AGENTS.md-d1fe17?style=flat-square&labelColor=0d0f12)](#安装)
[![Zero dependencies](https://img.shields.io/badge/dependencies-0-d1fe17?style=flat-square&labelColor=0d0f12)](#安装)

**输入一句话创意，输出逐秒分镜，再按每个模型自己的格式渲染成提示词。**

[快速开始](#快速开始) · [工作原理](#工作原理) · [示例](#示例) · [安装](#安装) · [常见问题](#常见问题)

</div>

[English](README.md) · [Русский](README.ru.md) · 简体中文 · [Español](README.es.md) · [Português (BR)](README.pt-BR.md) · [日本語](README.ja.md) · [한국어](README.ko.md)

面向 Kling 3.0、Veo 3、Wan 2.5、Seedance 和 Runway 的 AI 视频提示词，按模型真正读得懂的方式来写：一份带时间轴的分镜（0-2 秒、2-4 秒……），每个节拍一个运镜，加上镜头焦段、灯光方案、一句运动物理描述、三层声音和一份简短的负面提示词列表；然后按模型逐一渲染，自动套用各自的长度上限、负面提示词处理方式和音频支持情况。文生视频和图生视频都适用。它以 Claude Code 技能、Cursor 规则和 Codex / `AGENTS.md` 片段的形式发布，另附一个纯标准库的 Python 脚本，不用任何智能体也能直接运行。

| **先写分镜** | **按模型渲染** | **真正管用的词汇表** |
|:---|:---|:---|
| 脚本先搭出节拍网格，所有槽位填满、时间轴对得上之前，拒绝渲染。 | 同一份分镜可以变成 Kling 的多镜头提示词、带引号对白的 Veo 一镜到底提示词、800 字符以内的 Wan 提示词、带编号镜头的 Seedance 提示词，或者只含正向描述的 Runway 提示词。 | 八张参考表（运镜、焦段、灯光、物理、声音、负面提示词、模型限制、格式），供智能体和 `vocab` 命令随时取用。 |

## 快速开始

```bash
git clone https://github.com/uniqaiapp/video-director
cd video-director
python3 scripts/storyboard.py new --idea "latte art at dawn" -o board.json   # scaffold with [[fill: ...]] slots
python3 scripts/storyboard.py check examples/latte-art-dawn.json --model kling
python3 scripts/storyboard.py render examples/latte-art-dawn.json --model kling
```

第一条命令会生成一份分镜骨架：2 秒一个节拍的网格，外加预填好的焦段、灯光和物理提示（这个创意一看就是微距加黄金时刻）。由智能体或你自己把槽位填上；`check` 负责校验；`render` 打印该模型的提示词、负面提示词字段和注意事项。

## 演示

<img alt="video-director demo: scaffold a storyboard, check an example, render it for Kling 3.0" src="assets/demo.svg" width="820">

## 工作原理

1. **搭骨架。** `new` 把创意变成 JSON：每 2 秒一个节拍（最后一个节拍吸收余数），主体、场景、风格和每个节拍都留有 `[[fill: ...]]` 标记；当创意明显属于微距、航拍、夜景、人像、产品、水下、追逐或科幻时，还会给出焦段、运镜、灯光、物理和声音的关键词提示。
2. **填内容。** 技能（`SKILL.md`）告诉智能体怎么填：每个节拍只发生一件事，第一个节拍交代环境、最后一个节拍定住，每两个节拍一个运镜，用具体名词，物理用一句话，声音用三个短语，负面提示词只写名词。词汇来自 `references/`。
3. **校验。** 结构性错误（槽位未填、时间轴有空洞、提示词超过硬上限）直接判失败；模型适配问题只给警告：Veo 只支持 4/6/8 秒，Wan 和 Runway 只支持 5/10 秒，Runway 忽略负面提示词且没有音频，单镜头模型里出现了剪切。
4. **渲染。** 同一份分镜，按每个模型的格式输出。Kling 读的是主体、画面风格、带时间的镜头、运动、音频；Veo 得到的是 "one continuous take"（一镜到底），节拍之间用 "Then" 衔接，对白加引号，负面字段里额外加上 `subtitles, captions`，因为不加的话它会把字幕直接烧进画面；Wan 用精简版式；Seedance 用 `Shot 1 (0-2s): ...` 的编号格式；Runway 则把运镜放在最前面，并且只用正向描述。

```
idea ──new──▶ board.json ──fill (agent)──▶ check ──▶ render --model kling | veo | wan | seedance | runway
                                             ▲                   │
                                             └── fix one field ◀─┘  (floating → physics, flat → light, artefacts → negative)
```

模型限制集中在一张表里（`python3 scripts/storyboard.py models`），并标注了从厂商文档读取的日期；来源列在 `references/model-notes.md`。这个仓库里没有任何质量评分或基准测试：脚本只负责结构和限制，成片质量取决于节拍写得怎么样。

## 示例

[`examples/`](examples/README.md) 里有十二份分镜，每份都配一个 Markdown 页面，展示时间轴和面向每个模型渲染出的提示词。测试会把每个页面与 `render --model all --format md` 的输出逐字节比对，所以它们不可能和脚本脱节。

<details>
<summary><b>霓虹雨夜街头（Veo 3，8 秒，竖屏，带对白）：从分镜到提示词</b></summary>

**分镜**（`examples/neon-rain-street.json`，节选）

```text
0-2s  she stands under the awning watching the rain, neon reflections sliding across her coat   | slow push-in at eye level, framed waist-up
2-4s  a car passes, its headlights sweep across her face; she turns to the camera                | continue the push-in
4-6s  she says the line, half smiling                                                            | hold on a medium close-up
6-8s  she steps out into the rain and opens the umbrella                                         | slow tilt up following the umbrella
physics: rain falls in straight lines and bounces off the awning edge; her coat is wet and heavy; the umbrella opens with a snap and settles
sound:   steady rain, tyres on wet asphalt, a distant siren | umbrella snapping open | She says, quietly, lip-synced: "You're late. Again."
```

**Veo 3 提示词**（`render --model veo`）

```text
A woman in her thirties in a dark raincoat, wet hair pushed back, holding a closed umbrella in a narrow city street at night in heavy rain, neon shop signs reflected in the wet asphalt. Anamorphic, teal and magenta grade, Kodak 500T grain in the shadows. 35mm anamorphic, f/2, oval bokeh. Magenta and cyan neon practicals as key, cool fill from the sky, rim from a passing car. One continuous take over 8 seconds. She stands under the awning watching the rain, neon reflections sliding across her coat. Camera: slow push-in at eye level, framed waist-up. Then a car passes, its headlights sweep across her face; she turns to the camera. Camera: continue the push-in. Then she says the line, half smiling. Camera: hold on a medium close-up. Then she steps out into the rain and opens the umbrella. Camera: slow tilt up following the umbrella. Motion: rain falls in straight lines and bounces off the awning edge; her coat is wet and heavy; the umbrella opens with a snap and settles. Audio. Ambience: steady rain, tyres on wet asphalt, a distant siren. Sound effects: umbrella snapping open. Dialogue: She says, quietly, lip-synced: "You're late. Again."
```

负面字段：`morphing, extra limbs, warped hands, flicker, text, watermark, logo, jump cuts, frame jitter, subtitles, captions`

包含所有模型的完整页面：[examples/neon-rain-street.md](examples/neon-rain-street.md)。

</details>

<details>
<summary><b>运动鞋转台（Runway Gen-4，5 秒，图生视频）：哪些内容被丢掉了，为什么</b></summary>

Runway 只读正向描述，也没有原生音频，所以 `render --model runway` 会把运镜放在开头，保留节拍和物理描述，丢掉负面提示词列表和声音块。注意事项里会写明这一点，`check --model runway` 也会打印同样的两条警告。分镜本身仍然保留这两部分，留给后期剪辑用。

```text
Slow 90-degree orbit, clockwise, at shoe height: A white leather sneaker with a gum sole, laces tied, pristine in a seamless light-grey studio backdrop, slow gradient to white. The sneaker sits on a matte turntable, three-quarter view, and begins to rotate. Camera: slow 90-degree orbit, clockwise, at shoe height. Then the rotation reveals the side profile and the stitching. Camera: continue the orbit. Then the shoe comes to rest facing the camera. Camera: hold. Motion: rigid object; reflections on the leather slide smoothly as it rotates; no deformation; the turntable motion is constant. Clean high-key commercial look, neutral colour.
```

完整页面：[examples/sneaker-turntable.md](examples/sneaker-turntable.md)。

</details>

<details>
<summary><b>沙漠飙车（Kling 3.0，10 秒）：一次有意为之的剪切，以及单镜头模型对此的反应</b></summary>

节拍 4 是“切到车内过肩镜头”。Kling 3.0 会把带时间的节拍当作镜头来执行，所以提示词保留了这次剪切。`check --model veo` 的回答是：

```text
WARN   desert-car-chase.json: Veo 3 / 3.1: 10s is not an available length (4/6/8 s); nearest is 8s, re-time the beats
WARN   desert-car-chase.json: Veo 3 / 3.1 is single-shot: beat 4 asks for a cut, which it cannot do; merge it into the previous beat or change the angle gradually
OK     desert-car-chase.json: 5 beats, 10s, 2 warning(s) for Veo 3 / 3.1
```

完整页面：[examples/desert-car-chase.md](examples/desert-car-chase.md)。

</details>

| 分镜 | 目标模型 | 展示内容 |
|---|---|---|
| [latte-art-dawn](examples/latte-art-dawn.md) | Kling 3.0，8 秒 | 基准案例：一个主体、一种光、一种液体 |
| [candle-confession](examples/candle-confession.md) | Veo 3，8 秒 | 单一光源，一个 3 秒的对白节拍 |
| [sci-fi-corridor-reveal](examples/sci-fi-corridor-reveal.md) | Veo 3，8 秒 | 用光线变化作为事件 |
| [coastline-drone-dawn](examples/coastline-drone-dawn.md) | Wan 2.5，10 秒 | 800 字符上限内的五个航拍节拍 |
| [ramen-steam-macro](examples/ramen-steam-macro.md) | Wan 2.5，5 秒，9:16 | 微距、蒸汽和液体物理 |
| [fashion-tunnel-walk](examples/fashion-tunnel-walk.md) | Kling 3.0，10 秒，9:16 | 图生视频，行走和丝绸物理 |
| [cat-window-rain](examples/cat-window-rain.md) | Seedance 2.0，5 秒 | 微动作，编号镜头 |
| [jellyfish-drift](examples/jellyfish-drift.md) | Seedance 2.0，10 秒 | 水下阻力、焦散、移焦 |
| [rooftop-timelapse-dusk](examples/rooftop-timelapse-dusk.md) | generic，12 秒 | 3 秒节拍；Veo、Wan、Runway 上的长度警告 |

## 安装

任何读取指令文件的智能体都能用。Python 3.9+（或者你手头已有的任何 Python 3）。无需安装任何包。

<details open>
<summary><b>Claude Code</b></summary>

```bash
# user-level
git clone https://github.com/uniqaiapp/video-director ~/.claude/skills/video-director
# or project-level
git clone https://github.com/uniqaiapp/video-director .claude/skills/video-director
```

然后在任意会话里输入 `/video-director`，或者直接描述你想要的片段；技能会根据自己的 `description` 自动触发。仓库公开后，`npx skills add uniqaiapp/video-director` 也可以用。作为插件安装（待 uniqaiapp 市场发布后）：先 `/plugin marketplace add uniqaiapp/skills`，再 `/plugin install video-director@uniqaiapp`。

</details>

<details>
<summary><b>Cursor</b></summary>

把 `SKILL.md`、`scripts/`、`references/` 和 [`.cursor/rules/video-director.mdc`](.cursor/rules/video-director.mdc) 复制到你的项目里。规则文件通过 `@SKILL.md` 内嵌技能本体。

</details>

<details>
<summary><b>Codex / 任何读取 AGENTS.md 的智能体</b></summary>

把 `SKILL.md`、`scripts/` 和 `references/` 复制到 `.agents/skills/video-director/`，再把 [`codex/INSTRUCTIONS.md`](codex/INSTRUCTIONS.md) 里的片段加进你的 `AGENTS.md`。本仓库自带的 [`AGENTS.md`](AGENTS.md) 是通用版本。

</details>

<details>
<summary><b>不用智能体</b></summary>

每条命令都可以独立运行：`python3 scripts/storyboard.py --help`。也可以把 [`SKILL.md`](SKILL.md) 直接粘进任意模型的系统提示词；除 frontmatter 外，它没有任何智能体专属语法。

</details>

## 用法

```bash
python3 scripts/storyboard.py models                                   # limits table with its check date
python3 scripts/storyboard.py new --idea "..." --duration 8 --model veo --aspect 9:16 -o board.json
python3 scripts/storyboard.py vocab camera orbit                      # also: lens, light, physics, sound, negative
python3 scripts/storyboard.py check board.json --model veo
python3 scripts/storyboard.py render board.json --model veo           # or kling,wan  or  all --format md -o board.md
```

在哪里运行提示词：Kling 3.0、Veo 3 和 Wan 2.5 在 [UniqAI 的文生视频工作台](https://uniqai.app/video/text-to-video?utm_source=github&utm_medium=readme-zh-cn&utm_campaign=video-director) 里并排可用，同一份分镜可以在同一个页面上试三个模型；换成其他任何前端或 API 也一样，提示词就是纯文本。

## 常见问题

<details>
<summary><b>该选哪个模型？</b></summary>

对白或声音很重要：选 Veo 3（原生音频最强，但最长 8 秒）。片段内需要剪切，或者时长要 10-15 秒：选 Kling 3.0 或 Seedance 2.0（多镜头）。有起始图的产品视频：选 Runway Gen-4 或 Kling。想先低成本试一遍：选 Wan 2.5，提示词保持简短。`check` 命令会在你花掉积分之前告诉你哪些内容放不进去。

</details>

<details>
<summary><b>画面发飘、滑动或变形，该改什么？</b></summary>

一次只改一个字段：飘或滑是 `physics` 的问题（"feet plant firmly on each step"、"the cup rests on the saucer"）；变形通常是事件太多，删掉一个节拍，或者把最后一个节拍改成定住；伪影以名词形式写进 `negative`。重新 check、重新 render。`references/motion-physics.md` 里有现成的短语。

</details>

<details>
<summary><b>模型限制是最新的吗？</b></summary>

这些限制是在 `python3 scripts/storyboard.py models` 打印的日期从各厂商文档读取的，来源列在 `references/model-notes.md`。厂商会在不通知的情况下更改限制。当校验结果与厂商页面不一致时，以页面为准，并附上 URL 和日期提一个 issue 或 PR。

</details>

<details>
<summary><b>Sora、Hailuo、Luma、Pika 能用吗？</b></summary>

用 `--model generic`：输出完整的结构化提示词和单独的负面提示词列表，再由你手动裁剪到该模型的限制以内。`sora` 被接受为 `generic` 的别名，因为 OpenAI 已在 2026 年停止 Sora，没有可供适配的在线目标了。要新增模型，PR 需要附上该模型有文档依据的限制和来源。

</details>

## 相关项目

- [awesome-ai-video-prompts](https://github.com/uniqaiapp/awesome-ai-video-prompts)：精选并分类的 AI 视频模型提示词，附生成时用的参数，提供 JSON 和 Markdown 两种格式。
- [ai-video-pricing](https://github.com/uniqaiapp/ai-video-pricing)：人工核对的 AI 视频生成价格表，按秒和按片段计价，每行都有来源 URL 和核对日期。
- [ugc-ad-director](https://github.com/uniqaiapp/ugc-ad-director)：为 AI 视频撰写短篇 UGC 风格广告的脚本和分镜表：钩子、证明、优惠，并按模型输出提示词。
- [no-plastic](https://github.com/uniqaiapp/no-plastic)：让 AI 人像看起来自然的提示词规则和检查器：皮肤质感、灯光和焦段选择，避免塑料感。

## 参与贡献

欢迎提 issue 和 pull request。改动尽量小，并在 PR 描述里附上一份分镜和它渲染出的提示词。本地检查方法见 [CONTRIBUTING.md](CONTRIBUTING.md)（`python3 tests/run.py`，无依赖）。

## 许可证

代码和示例：[MIT](LICENSE)。`references/` 里的词汇表：CC BY 4.0，署名方式为 "UniqAI, github.com/uniqaiapp/video-director"。© UniqAI

---

<div align="center">

<sub>由 <a href="https://uniqai.app/?utm_source=github&utm_medium=readme-zh-cn&utm_campaign=video-director">UniqAI</a> 出品，一款集 AI 图片、视频和聊天于一体的应用：Kling 3.0、Veo 3、Flux、Nano Banana 以及 GPT-5/Claude/Gemini/Grok 都在一个地方。我们写这个技能，是为了不用再一遍遍向自己解释运镜。</sub>

</div>
