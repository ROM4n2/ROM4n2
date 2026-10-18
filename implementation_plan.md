# GitHub Profile README (ROM4n2/ROM4n2) Implementation Plan

> **Goal**: Build and publish a high-signal, academic, zero-emoji GitHub Profile README for ROM4n2, showcasing core systems competencies and verified flagship projects.
> **Tech Stack**: Markdown (GitHub Flavored Markdown), Python 3.11 (Harness/Verification), GitHub CLI (`gh`).
> **Spec Reference**: `docs/specs/2026-10-18-github-profile-readme-design.md`
> **Global Constraints**: Strict GFM, UTF-8 stdout, zero emojis, zero innerHTML, all hyperlinks return verified HTTP 200, guard clauses in scripts.
> **Branch**: `feat/profile-readme` — initialized from local master/main, landed via branch merge before public deployment.

---

## [*] Decisions So Far

- [Spec-2026-10-18](docs/specs/2026-10-18-github-profile-readme-design.md): Adopted Option A (Native Profile README in `ROM4n2/ROM4n2`) over standalone web dashboard.
- [Scope-Decision]: Excluded `scriptorium-vault` and `Defensive Skills (dfs-*)` (unreleased internal assets).
- [Scope-Decision]: Excluded `adk-go` from the primary showcase card to highlight author/core-contributor works.
- [Project-Selection]: Included `qingjian` (Rust dual-language input method) alongside `DeLector`, `blind-llm-eyes`, and `know-her`.
- [Reliability-Decision]: Rejected third-party dynamic badge services (Shields.io/Readme Stats) to prevent timeout broken images; selected pure static GFM tables and monochrome badges.

---

## [*] Active Frontier (Unblocked Tasks)

### Task 1: Git Repository Baseline & Verification Test Harness [Tier: 1-Light] [Mode: AFK] [Subagent: TDD Builder]

**Files:**
- Create: `.gitignore`
- Create: `scripts/verify_profile.py`
- Test: `scripts/verify_profile.py` (self-test mode)

**Interfaces:**
- Consumes: Target Markdown file path (e.g., `README.md`).
- Produces: CLI exit code 0 if:
  1. Zero emojis found in text (regex scan).
  2. Zero raw HTML tags / `innerHTML` patterns found.
  3. All external markdown links (`[text](url)`) resolve to HTTP 200 (via `urllib.request`).
  4. Header hierarchy and table balance are valid.
  Otherwise returns non-zero exit code with line-numbered violations.

**Injected Instincts (Compile-Time Rule Injection):**
- [ ] `[Instinct: UTF-8 Stdout]`: Ensure `sys.stdout.reconfigure(encoding="utf-8", errors="replace")` is set in Python scripts.
- [ ] `[Instinct: Zero-Dependency]`: Use Python standard library (`urllib.request`, `re`, `pathlib`, `sys`) only.
- [ ] `[Instinct: Guard Clauses]`: Flatten nested loops and conditions with guard clauses.

**Subagent Prompt Scaffold (for /dfs-exec):**
> "Implement Task 1: Repository baseline and verification harness.
> Mode: AFK | Role: TDD Builder
> Goal: Initialize git in `D:/Code/personal-homepage`, add `.gitignore`, and create `scripts/verify_profile.py` to enforce zero-emoji, zero-HTML, and link HTTP 200 rules.
> Target Files: Create `.gitignore`, Create `scripts/verify_profile.py`.
> TDD Steps:
> 1. Write `scripts/verify_profile.py` with CLI interface `python scripts/verify_profile.py <file.md>`.
> 2. Test harness with a temporary invalid markdown file containing emojis and invalid links to verify failure (RED).
> 3. Verify exit code 1 and error reporting on failing probe.
> 4. Ensure script adheres to Python 3.11 stdlib with explicit error messages (GREEN).
> Return: Summary with MANDATORY Physical Execution Receipt (exit code + stdout snippet)."

**Step Breakdown:**
- [ ] **Step 1: Write failing probe test (RED)** (Run `scripts/verify_profile.py` on malformed probe file; verify failure output).
- [ ] **Step 2: Run verification harness and capture non-zero exit code**.
- [ ] **Step 3: Implement `scripts/verify_profile.py` and `.gitignore` (GREEN)**.
- [ ] **Step 4: Verify clean pass on valid test probe (Exit code 0)**.
- [ ] **Step 5: Refactor with guard clauses and UTF-8 encoding configuration**.
- [ ] **Step 6: Physical Evidence Gate**: Capture raw terminal execution receipt (Exit code 0).
- [ ] **Step 7: Git atomic commit**: Commit baseline and harness to `feat/profile-readme`.

---

### Task 2: Draft Profile README Content & Component Matrix [Tier: 2-Standard] [Mode: AFK] [Subagent: TDD Builder]

**Files:**
- Create: `README.md`
- Test: `scripts/verify_profile.py`

**Interfaces:**
- Consumes: `docs/specs/2026-10-18-github-profile-readme-design.md` specifications.
- Produces: Production `README.md` containing:
  - Header: `ROM4n2` identity, engineering philosophy, and specialization summary.
  - Core Technical Competencies Table: Languages (Go, C/C++, Python, Rust), Systems & Infrastructure, Quality Invariants.
  - Flagship Projects Matrix: `DeLector`, `qingjian`, `blind-llm-eyes`, `know-her` with exact URLs and problem-solution descriptions.
  - Engineering Invariants: Zero-hallucination, anti-sycophancy, guard clauses.
  - Footprint & Public Channels.

**Injected Instincts (Compile-Time Rule Injection):**
- [ ] `[Instinct: Editorial Rigor]`: Zero emojis, academic styling, no colloquial filler.
- [ ] `[Instinct: Real URLs]`: All links must point to existing repositories (`ROM4n2/DeLector`, `qingjian-team/qingjian`, etc.).
- [ ] `[Instinct: Table Layout]`: Align table pipes consistently for terminal and web rendering.

**Subagent Prompt Scaffold (for /dfs-exec):**
> "Implement Task 2: Draft Profile README content and component matrix.
> Mode: AFK | Role: TDD Builder
> Goal: Write `README.md` according to the 5 schema sections in `docs/specs/2026-10-18-github-profile-readme-design.md`.
> Target Files: Create `README.md`.
> TDD Steps:
> 1. Run `python scripts/verify_profile.py README.md` before file creation or on empty file to establish RED state.
> 2. Write the complete, production-grade `README.md` with zero emojis, pure GFM tables, and accurate project URLs.
> 3. Run `python scripts/verify_profile.py README.md` to establish GREEN state (all links return HTTP 200, zero syntax errors).
> 4. Ensure no markdown lint violations.
> Return: Summary with MANDATORY Physical Execution Receipt (exit code + stdout snippet)."

**Step Breakdown:**
- [x] **Step 1: Verify missing/empty file fails harness (RED)**.
- [x] **Step 2: Author `README.md` according to spec sections 1 through 5 (GREEN)**.
- [x] **Step 3: Execute `python scripts/verify_profile.py README.md` and verify all link checks return HTTP 200**.
- [x] **Step 4: Check for zero emojis and zero raw HTML tags**.
- [x] **Step 5: Physical Evidence Gate**: Capture raw terminal execution receipt.
- [x] **Step 6: Git atomic commit**: Commit `README.md` to `feat/profile-readme`.

---

### Task 3: Dual-Theme Contrast & GFM Rendering Proof [Tier: 1-Light] [Mode: AFK] [Subagent: Evidence Auditor]

**Files:**
- Test: `README.md`
- Inspect: Rendered HTML output via local conversion or browser probe.

**Interfaces:**
- Consumes: `README.md`.
- Produces: Physical verification receipt demonstrating clean rendering, no broken table wraps, and contrast compliance.

**Injected Instincts (Compile-Time Rule Injection):**
- [ ] `[Instinct: Physical Evidence]`: Capture actual markdown render output or test receipt.

**Subagent Prompt Scaffold (for /dfs-exec):**
> "Implement Task 3: Dual-theme contrast and rendering proof.
> Mode: AFK | Role: Evidence Auditor
> Goal: Verify that `README.md` renders without table breakage, overflows, or contrast regressions in both light and dark backgrounds.
> Verification Steps:
> 1. Parse `README.md` to verify table column counts match across all rows.
> 2. Generate rendered HTML preview or verify structure using standard python markdown engine.
> 3. Confirm all badge image URLs and anchors have fallback alt text.
> Return: Physical Execution Receipt with table row verification and link audit report."

**Step Breakdown:**
- [x] **Step 1: Run automated table structure validator on `README.md`**.
- [x] **Step 2: Confirm every badge/image has descriptive text fallback**.
- [x] **Step 3: Physical Evidence Gate**: Log verification report with column and link counts.
- [x] **Step 4: Git atomic commit**: Clean tag or status commit if needed.

---

### Task 4: GitHub Remote Publication & Live Profile Sync [Tier: 3-Critical] [Mode: HITL] [Subagent: Release Coordinator]

**Files:**
- Target: GitHub Remote `ROM4n2/ROM4n2`

**Interfaces:**
- Consumes: Local verified `README.md` on `main` branch.
- Produces: Created public repository `ROM4n2/ROM4n2` on GitHub, pushed `main` branch, and HTTP 200 receipt from `https://github.com/ROM4n2`.

**Injected Instincts (Compile-Time Rule Injection):**
- [ ] `[Instinct: Human Checkpoint]`: Require explicit user confirmation before executing remote creation or push.
- [ ] `[Instinct: Verify Remote]`: Run `gh repo view ROM4n2/ROM4n2` after push to confirm live state.

**Subagent Prompt Scaffold (for /dfs-exec):**
> "Implement Task 4: GitHub remote publication and live profile sync.
> Mode: HITL | Role: Release Coordinator
> Goal: Create public repository `ROM4n2/ROM4n2`, set remote origin, push `main`, and verify GitHub profile display.
> Execution Steps:
> 1. Request human approval for remote repository creation.
> 2. Run `gh repo create ROM4n2/ROM4n2 --public --description 'GitHub Profile README' --source=. --remote=origin --push`.
> 3. Verify repository status using `gh repo view ROM4n2/ROM4n2`.
> 4. Verify HTTP response from `https://github.com/ROM4n2`.
> Return: Physical Execution Receipt with repository URL and live confirmation."

**Step Breakdown:**
- [x] **Step 1: HITL Gate: Present final `README.md` to user and request publication authorization**.
- [x] **Step 2: Initialize remote repository `ROM4n2/ROM4n2` via GitHub CLI (`gh`)**.
- [x] **Step 3: Push commits to remote `main` branch**.
- [x] **Step 4: Verify repository exists and is public via `gh repo view`**.
- [x] **Step 5: Physical Evidence Gate**: Capture raw terminal execution receipt with git push logs and HTTP 200 confirmation.

---

## [*] Fog of War (Not Yet Specified)

- **[Deferred 1]**: Automated commit/activity statistics workflow (Deferred until initial profile baseline is live and verified; avoids brittle GitHub Actions failures on initial rollout).

---

## [x] Out of Scope

- Standalone web frontend applications (React, Vue, Astro, Hugo).
- Unofficial third-party SVG badge widgets susceptible to uptime degradation.
- Emoji badges or non-academic marketing visuals.
