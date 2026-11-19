// Entry program for the 19 November 2026 "World in One Picture" image.
//
// The finished 1024x1024 front page is already in this repo as entry.png.
// All this program does is place an exact copy of that file where the
// grader expects it. It renders nothing, fetches nothing, and never
// writes into the repo directory, so it cannot fail on missing system
// resources, a missing imaging library, or a read-only checkout.
//
// Only the Node standard library is used (node:fs, node:path, node:url).
// The run is fully deterministic: copying the same bytes twice gives
// the same file twice.

import { copyFileSync, existsSync, mkdirSync } from "node:fs";
import { dirname, join, resolve } from "node:path";
import { fileURLToPath } from "node:url";

// The folder this file lives in, no matter where the caller runs from.
const repoDir = dirname(fileURLToPath(import.meta.url));

const sourcePath = join(repoDir, "entry.png");

if (!existsSync(sourcePath)) {
  throw new Error(`entry.png not found next to main.ts (looked in ${repoDir})`);
}

// Where the copy goes: $MAKEFUN_OUTPUT_DIR when set, /output otherwise.
const rawOutputDir = process.env.MAKEFUN_OUTPUT_DIR;
const outputDir =
  rawOutputDir !== undefined && rawOutputDir !== ""
    ? resolve(rawOutputDir)
    : "/output";

mkdirSync(outputDir, { recursive: true });

const targetPath = join(outputDir, "entry.png");
copyFileSync(sourcePath, targetPath);

console.log(`Copied entry.png to ${targetPath}`);
