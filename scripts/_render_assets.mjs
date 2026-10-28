#!/usr/bin/env node
// Maintainer-only: regenerates assets/ (banner, light banner, social preview PNG, terminal demo)
// from the shared uniqaiapp design kit. Not part of the install; users get the committed files.
// Requires the design kit checkout next to this repo (or UNIQAI_DESIGN pointing at it) and, for the PNG,
// sharp reachable from the design kit's render-social.mjs.
//
//   node scripts/_render_assets.mjs
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

const ROOT = path.dirname(path.dirname(fileURLToPath(import.meta.url)));
const KIT = process.env.UNIQAI_DESIGN || path.resolve(ROOT, "../_shared/design"); // conventions-allow: abs-path
const OUT = path.join(ROOT, "assets");

const { renderBanner } = await import(pathToFileURL(path.join(KIT, "render-banner.mjs")).href);
const { renderSocialPng } = await import(pathToFileURL(path.join(KIT, "render-social.mjs")).href);
const { renderTerminal } = await import(pathToFileURL(path.join(KIT, "render-terminal.mjs")).href);

const base = {
  repo: "video-director",
  title: "video-director",
  glyph: "VD",
  tagline: "Idea to shot list to Kling, Veo, Wan, Runway prompt",
};
fs.mkdirSync(OUT, { recursive: true });
fs.writeFileSync(path.join(OUT, "banner.svg"), renderBanner({ ...base, theme: "dark" }));
fs.writeFileSync(path.join(OUT, "banner-light.svg"), renderBanner({ ...base, theme: "light" }));
await renderSocialPng({ ...base, tagline: "Turn a one-line idea into a second-by-second storyboard and a prompt for Kling 3.0, Veo 3, Wan 2.5, Seedance or Runway." }, path.join(OUT, "social-preview.png"));

const script = fs.readFileSync(path.join(ROOT, "demo.txt"), "utf8").replace(/\r/g, "").split("\n");
if (script.length && script[script.length - 1] === "") script.pop();
fs.writeFileSync(path.join(OUT, "demo.svg"), renderTerminal({ lines: script, title: "video-director — bash", loop: true }));

for (const f of fs.readdirSync(OUT)) console.log(f.padEnd(22), (fs.statSync(path.join(OUT, f)).size / 1024).toFixed(1) + " KB");
