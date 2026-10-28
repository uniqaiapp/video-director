<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/banner.svg">
  <source media="(prefers-color-scheme: light)" srcset="assets/banner-light.svg">
  <img alt="video-director: Turn a one-line idea into a shot-by-shot prompt for AI video models (Kling, Veo, Sora and others), with camera, lighting and motion vocabulary." src="assets/banner.svg" width="1280" height="320">
</picture>

# video-director：Kling・Veo 3・Wan・Runway 向け AI動画プロンプト

[![License: MIT](https://img.shields.io/badge/license-MIT-d1fe17?style=flat-square&labelColor=0d0f12)](LICENSE)
[![Claude Code skill](https://img.shields.io/badge/Claude_Code-skill-d1fe17?style=flat-square&labelColor=0d0f12)](#インストール)
[![Cursor](https://img.shields.io/badge/Cursor-rules-d1fe17?style=flat-square&labelColor=0d0f12)](#インストール)
[![Codex](https://img.shields.io/badge/Codex-AGENTS.md-d1fe17?style=flat-square&labelColor=0d0f12)](#インストール)
[![Zero dependencies](https://img.shields.io/badge/dependencies-0-d1fe17?style=flat-square&labelColor=0d0f12)](#インストール)

**アイデアを入れると秒単位の絵コンテが出てきて、各モデルの形式に合わせたプロンプトとして出力されます。**

[クイックスタート](#クイックスタート) · [仕組み](#仕組み) · [例](#例) · [インストール](#インストール) · [FAQ](#faq)

</div>

[English](README.md) · [Русский](README.ru.md) · [简体中文](README.zh-CN.md) · [Español](README.es.md) · [Português (BR)](README.pt-BR.md) · 日本語 · [한국어](README.ko.md)

AI動画プロンプトを、Kling 3.0・Veo 3・Wan 2.5・Seedance・Runway がそのまま読める形で書きます。秒単位の絵コンテ（0〜2秒、2〜4秒、…）に、ビートごとに1つのカメラワーク、レンズ、ライティング、モーション物理の一文、3層のサウンド、短いネガティブリストを収め、それをモデルごとの文字数上限、ネガティブプロンプトの扱い、音声対応を反映してレンダリングします。テキストから動画（text-to-video）と画像から動画（image-to-video）の両方で使えます。Claude Code のスキル、Cursor のルール、Codex / `AGENTS.md` 用スニペットとして提供し、エージェントなしでも動く標準ライブラリのみの Python スクリプトが付属します。

| **絵コンテが先** | **モデルごとに出力** | **効く語彙** |
|:---|:---|:---|
| スクリプトはビートのグリッドを組み立て、すべてのスロットが埋まりタイムラインの合計が合うまでレンダリングを拒否します。 | 1つの絵コンテが、Kling のマルチショットプロンプト、セリフを引用符で入れた Veo のワンテイク、800文字の Wan プロンプト、番号付きの Seedance ショット、ポジティブ表現のみの Runway プロンプトになります。 | 8つのリファレンス表（カメラ、レンズ、ライト、物理、サウンド、ネガティブ、モデル上限、フォーマット）をエージェントと `vocab` コマンドが参照します。 |

## クイックスタート

```bash
git clone https://github.com/uniqaiapp/video-director
cd video-director
python3 scripts/storyboard.py new --idea "latte art at dawn" -o board.json   # scaffold with [[fill: ...]] slots
python3 scripts/storyboard.py check examples/latte-art-dawn.json --model kling
python3 scripts/storyboard.py render examples/latte-art-dawn.json --model kling
```

最初のコマンドは、2秒刻みのビートグリッドと、レンズ・ライト・物理のヒントをあらかじめ入れた絵コンテの雛形を書き出します（このアイデアはマクロとゴールデンアワーと判定されます）。スロットはエージェント、またはあなたが埋めます。`check` が検証し、`render` がそのモデル向けのプロンプト、ネガティブ欄、注意点を出力します。

## デモ

<img alt="video-director demo: scaffold a storyboard, check an example, render it for Kling 3.0" src="assets/demo.svg" width="820">

## 仕組み

1. **雛形を作る。** `new` がアイデアを JSON に変換します。2秒ごとのビート（最後のビートが余りを吸収）、subject・setting・style と各ビートの `[[fill: ...]]` マーカー、そしてアイデアがマクロ、空撮、夜景、ポートレート、プロダクト、水中、チェイス、SF と明らかな場合はレンズ・カメラ・ライト・物理・サウンドのキーワードヒントが入ります。
2. **埋める。** スキル（`SKILL.md`）がエージェントに書き方を指示します。1ビートに1つの出来事、最初のビートで状況を示して最後のビートで静止、2ビートに1つのカメラワーク、具体的な名詞、物理は一文、サウンドは3つのフレーズ、ネガティブは名詞で。語彙は `references/` から引きます。
3. **チェックする。** 構造上のエラー（未記入のスロット、タイムラインの抜け、ハード上限を超えたプロンプト）は失敗になり、モデル適合の問題は警告になります。Veo は4/6/8秒のみ、Wan と Runway は5/10秒、Runway はネガティブを無視し音声もなし、シングルショットのモデルでのカット、といったものです。
4. **レンダリングする。** 同じ絵コンテを各モデルの形式で出力します。Kling は被写体、ルック、時間付きショット、モーション、オーディオを読みます。Veo には "one continuous take" を付けてビートを "Then" でつなぎ、セリフを引用符で入れ、放っておくと字幕を焼き込んでしまうのでネガティブ欄に `subtitles, captions` を足します。Wan は簡潔なレイアウト、Seedance は `Shot 1 (0-2s): ...`、Runway はカメラを先頭にしたポジティブ表現のみです。

```
idea ──new──▶ board.json ──fill (agent)──▶ check ──▶ render --model kling | veo | wan | seedance | runway
                                             ▲                   │
                                             └── fix one field ◀─┘  (floating → physics, flat → light, artefacts → negative)
```

モデルの上限は1つの表（`python3 scripts/storyboard.py models`）にまとめ、ベンダーのドキュメントから読み取った日付を付けています。出典は `references/model-notes.md` にあります。このリポジトリに品質スコアやベンチマークはありません。スクリプトが保証するのは構造と上限で、クリップの質はビートの中身次第です。

## 例

[`examples/`](examples/README.md) に12本の絵コンテがあり、それぞれタイムラインと全モデル向けのレンダリング済みプロンプトを載せた Markdown ページが付いています。テストは各ページを `render --model all --format md` の出力とバイト単位で比較するので、スクリプトからずれることはありません。

<details>
<summary><b>ネオン雨の街（Veo 3、8秒、縦型、セリフあり）：絵コンテ → プロンプト</b></summary>

**絵コンテ**（`examples/neon-rain-street.json`、抜粋）

```text
0-2s  she stands under the awning watching the rain, neon reflections sliding across her coat   | slow push-in at eye level, framed waist-up
2-4s  a car passes, its headlights sweep across her face; she turns to the camera                | continue the push-in
4-6s  she says the line, half smiling                                                            | hold on a medium close-up
6-8s  she steps out into the rain and opens the umbrella                                         | slow tilt up following the umbrella
physics: rain falls in straight lines and bounces off the awning edge; her coat is wet and heavy; the umbrella opens with a snap and settles
sound:   steady rain, tyres on wet asphalt, a distant siren | umbrella snapping open | She says, quietly, lip-synced: "You're late. Again."
```

**Veo 3 プロンプト**（`render --model veo`）

```text
A woman in her thirties in a dark raincoat, wet hair pushed back, holding a closed umbrella in a narrow city street at night in heavy rain, neon shop signs reflected in the wet asphalt. Anamorphic, teal and magenta grade, Kodak 500T grain in the shadows. 35mm anamorphic, f/2, oval bokeh. Magenta and cyan neon practicals as key, cool fill from the sky, rim from a passing car. One continuous take over 8 seconds. She stands under the awning watching the rain, neon reflections sliding across her coat. Camera: slow push-in at eye level, framed waist-up. Then a car passes, its headlights sweep across her face; she turns to the camera. Camera: continue the push-in. Then she says the line, half smiling. Camera: hold on a medium close-up. Then she steps out into the rain and opens the umbrella. Camera: slow tilt up following the umbrella. Motion: rain falls in straight lines and bounces off the awning edge; her coat is wet and heavy; the umbrella opens with a snap and settles. Audio. Ambience: steady rain, tyres on wet asphalt, a distant siren. Sound effects: umbrella snapping open. Dialogue: She says, quietly, lip-synced: "You're late. Again."
```

ネガティブ欄：`morphing, extra limbs, warped hands, flicker, text, watermark, logo, jump cuts, frame jitter, subtitles, captions`

全モデル分を載せたページ：[examples/neon-rain-street.md](examples/neon-rain-street.md)

</details>

<details>
<summary><b>スニーカーのターンテーブル（Runway Gen-4、5秒、画像から動画）：何が落とされ、なぜか</b></summary>

Runway はポジティブ表現しか読まず、ネイティブの音声もありません。そのため `render --model runway` はカメラワークを先頭に置き、ビートと物理は残し、ネガティブリストとサウンドのブロックは落とします。注意点にその旨が出力され、`check --model runway` も同じ2つの警告を出します。編集用に、絵コンテ側には両方とも残ります。

```text
Slow 90-degree orbit, clockwise, at shoe height: A white leather sneaker with a gum sole, laces tied, pristine in a seamless light-grey studio backdrop, slow gradient to white. The sneaker sits on a matte turntable, three-quarter view, and begins to rotate. Camera: slow 90-degree orbit, clockwise, at shoe height. Then the rotation reveals the side profile and the stitching. Camera: continue the orbit. Then the shoe comes to rest facing the camera. Camera: hold. Motion: rigid object; reflections on the leather slide smoothly as it rotates; no deformation; the turntable motion is constant. Clean high-key commercial look, neutral colour.
```

全体のページ：[examples/sneaker-turntable.md](examples/sneaker-turntable.md)

</details>

<details>
<summary><b>砂漠のカーチェイス（Kling 3.0、10秒）：意図的なカットと、シングルショットのモデルの反応</b></summary>

ビート4は「cut to an interior over-the-shoulder shot」です。Kling 3.0 は時間付きのビートをショットとして扱うので、プロンプトにそのまま残ります。`check --model veo` はこう答えます。

```text
WARN   desert-car-chase.json: Veo 3 / 3.1: 10s is not an available length (4/6/8 s); nearest is 8s, re-time the beats
WARN   desert-car-chase.json: Veo 3 / 3.1 is single-shot: beat 4 asks for a cut, which it cannot do; merge it into the previous beat or change the angle gradually
OK     desert-car-chase.json: 5 beats, 10s, 2 warning(s) for Veo 3 / 3.1
```

全体のページ：[examples/desert-car-chase.md](examples/desert-car-chase.md)

</details>

| 絵コンテ | 対象 | 見どころ |
|---|---|---|
| [latte-art-dawn](examples/latte-art-dawn.md) | Kling 3.0、8秒 | 基本形：被写体1つ、光源1つ、液体1つ |
| [candle-confession](examples/candle-confession.md) | Veo 3、8秒 | 単一光源、3秒のセリフのビート |
| [sci-fi-corridor-reveal](examples/sci-fi-corridor-reveal.md) | Veo 3、8秒 | 光の変化を出来事にする |
| [coastline-drone-dawn](examples/coastline-drone-dawn.md) | Wan 2.5、10秒 | 800文字の上限内に収めた5つの空撮ビート |
| [ramen-steam-macro](examples/ramen-steam-macro.md) | Wan 2.5、5秒、9:16 | マクロ、湯気と液体の物理 |
| [fashion-tunnel-walk](examples/fashion-tunnel-walk.md) | Kling 3.0、10秒、9:16 | 画像から動画、歩行とシルクの物理 |
| [cat-window-rain](examples/cat-window-rain.md) | Seedance 2.0、5秒 | 微細な動き、番号付きショット |
| [jellyfish-drift](examples/jellyfish-drift.md) | Seedance 2.0、10秒 | 水中の抵抗、コースティクス、ラックフォーカス |
| [rooftop-timelapse-dusk](examples/rooftop-timelapse-dusk.md) | generic、12秒 | 3秒のビート。Veo、Wan、Runway では長さの警告が出る |

## インストール

指示ファイルを読むエージェントならどれでも動きます。Python 3.9 以上（手元にある Python 3 で構いません）。インストールするパッケージはありません。

<details open>
<summary><b>Claude Code</b></summary>

```bash
# user-level
git clone https://github.com/uniqaiapp/video-director ~/.claude/skills/video-director
# or project-level
git clone https://github.com/uniqaiapp/video-director .claude/skills/video-director
```

その後、任意のセッションで `/video-director` と入力するか、作りたいクリップを説明するだけで、スキルの `description` がトリガーになります。リポジトリが公開されれば `npx skills add uniqaiapp/video-director` でも入ります。プラグインとしては、uniqaiapp マーケットプレイスの公開後に `/plugin marketplace add uniqaiapp/skills` のあと `/plugin install video-director@uniqaiapp` です。

</details>

<details>
<summary><b>Cursor</b></summary>

`SKILL.md`、`scripts/`、`references/`、[`.cursor/rules/video-director.mdc`](.cursor/rules/video-director.mdc) をプロジェクトにコピーします。ルールファイルは `@SKILL.md` でスキルを埋め込んでいます。

</details>

<details>
<summary><b>Codex / AGENTS.md を読むエージェント</b></summary>

`SKILL.md`、`scripts/`、`references/` を `.agents/skills/video-director/` にコピーし、[`codex/INSTRUCTIONS.md`](codex/INSTRUCTIONS.md) のスニペットを自分の `AGENTS.md` に追加します。このリポジトリの [`AGENTS.md`](AGENTS.md) が汎用版です。

</details>

<details>
<summary><b>エージェントなしで</b></summary>

すべてのコマンドが単体で動きます：`python3 scripts/storyboard.py --help`。[`SKILL.md`](SKILL.md) はどのモデルのシステムプロンプトにも貼れます。フロントマター以外にエージェント固有の構文はありません。

</details>

## 使い方

```bash
python3 scripts/storyboard.py models                                   # limits table with its check date
python3 scripts/storyboard.py new --idea "..." --duration 8 --model veo --aspect 9:16 -o board.json
python3 scripts/storyboard.py vocab camera orbit                      # also: lens, light, physics, sound, negative
python3 scripts/storyboard.py check board.json --model veo
python3 scripts/storyboard.py render board.json --model veo           # or kling,wan  or  all --format md -o board.md
```

プロンプトを実行する場所について。[UniqAI のテキストから動画コンポーザー](https://uniqai.app/video/text-to-video?utm_source=github&utm_medium=readme-ja&utm_campaign=video-director)では Kling 3.0、Veo 3、Wan 2.5 を並べて使えるので、1つの絵コンテを同じページから3つのモデルで試せます。他のフロントエンドや API でも同じように使えます。プロンプトはただのテキストです。

## FAQ

<details>
<summary><b>どのモデルを選べばよいですか</b></summary>

セリフや音が重要なら Veo 3（ネイティブ音声が最も強いが最大8秒）。クリップ内でのカット、または10〜15秒なら Kling 3.0 か Seedance 2.0（マルチショット）。開始画像とプロダクトなら Runway Gen-4 か Kling。安く一発目を試すなら Wan 2.5、プロンプトは短く。`check` コマンドが、クレジットを使う前に収まらないものを教えてくれます。

</details>

<details>
<summary><b>クリップが浮く、滑る、形が崩れる。何を変えればよいですか</b></summary>

一度に1つのフィールドだけ変えます。浮きや滑りは `physics` の担当（"feet plant firmly on each step"、"the cup rests on the saucer"）。形が崩れるのはたいてい出来事が多すぎるので、ビートを1つ減らすか最後を静止にします。アーティファクトは `negative` に名詞で入れます。再チェック、再レンダリング。フレーズは `references/motion-physics.md` にあります。

</details>

<details>
<summary><b>モデルの上限は最新ですか</b></summary>

各ベンダーのドキュメントから、`python3 scripts/storyboard.py models` が表示する日付に読み取ったもので、出典は `references/model-notes.md` に一覧しています。ベンダーは予告なく上限を変えます。チェックがベンダーのページと食い違うときはページの方を信じ、URL と日付を添えて issue か PR を立ててください。

</details>

<details>
<summary><b>Sora、Hailuo、Luma、Pika でも使えますか</b></summary>

`--model generic` を使ってください。ネガティブリストを別立てにした完全な構造化プロンプトが出るので、モデルの上限に合わせて手で削ります。`sora` は `generic` のエイリアスとして受け付けます。OpenAI が2026年に Sora を終了し、整形対象となる稼働中のサービスがないためです。モデルを追加する PR には、出典付きの公式な上限が必要です。

</details>

## 関連リポジトリ

- [awesome-ai-video-prompts](https://github.com/uniqaiapp/awesome-ai-video-prompts)：AI動画モデル向けの厳選・分類済みプロンプト集。生成に使った設定付きで、JSON と Markdown で提供。
- [ai-video-pricing](https://github.com/uniqaiapp/ai-video-pricing)：AI動画生成の料金表を手作業で確認したもの。秒単価とクリップ単価、全行に出典 URL と確認日付き。
- [ugc-ad-director](https://github.com/uniqaiapp/ugc-ad-director)：AI動画向けの短い UGC風広告の台本とショットリスト。フック、証拠、オファー、モデルごとのプロンプト出力付き。
- [no-plastic](https://github.com/uniqaiapp/no-plastic)：自然に見える AI ポートレートのためのプロンプトルールとチェッカー。プラスチック感を避ける肌の質感、ライティング、レンズの選び方。

## コントリビュート

Issue と Pull Request を歓迎します。変更は小さく保ち、PR の説明に絵コンテとそのレンダリング済みプロンプトを添えてください。ローカルでのチェック（`python3 tests/run.py`、依存なし）は [CONTRIBUTING.md](CONTRIBUTING.md) を参照してください。

## ライセンス

コードと例：[MIT](LICENSE)。`references/` の語彙：CC BY 4.0、帰属表示は "UniqAI, github.com/uniqaiapp/video-director"。© UniqAI

---

<div align="center">

<sub>開発：<a href="https://uniqai.app/?utm_source=github&utm_medium=readme-ja&utm_campaign=video-director">UniqAI</a>。Kling 3.0、Veo 3、Flux、Nano Banana、GPT-5/Claude/Gemini/Grok を1か所で使える AI 写真・動画・チャットアプリです。このスキルは、カメラワークを自分たち自身に何度も説明し直すのをやめるために書きました。</sub>

</div>
