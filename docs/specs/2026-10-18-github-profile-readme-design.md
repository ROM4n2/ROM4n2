# Design Specification: GitHub Profile README for ROM4n2

**Date**: 2026-10-18  
**Status**: APPROVED  
**Author**: ROM4n2 & Hermes Agent  
**Target Path**: `docs/specs/2026-10-18-github-profile-readme-design.md`  
**Deploy Target**: `ROM4n2/ROM4n2` (`README.md`)

---

## 1. Problem Statement & User Value

- **Why build this**: 
  Visiting `github.com/ROM4n2` currently displays only the default GitHub interface without a profile README (`ROM4n2/ROM4n2` repository does not exist). Visitors must navigate through a list of public repositories and fork records to deduce the engineer's technical domain. A dedicated, structured Profile README establishes an authoritative, high-signal technical identity in under 5 seconds.
- **Target Scenario & Persona**:
  - Target audience: Senior engineering managers, open-source maintainers, high-rigor system collaborators.
  - Persona demonstrated: Pragmatic Senior Systems Engineer specializing in Go 1.24+ high-concurrency backends, Agent Harness infrastructure, and systems programming (C/C++, Rust).
- **Cost of Doing Nothing**:
  Passive perception loss; visitors miss primary achievements like `DeLector`, `qingjian`, and `blind-llm-eyes`, or confuse fork exploration with core production contributions.

---

## 2. User Journey & Core Flow

- **Happy Path (<= 3 steps to value)**:
  1. **Landing & Identity Anchor (0-3s)**: Visitor lands on `github.com/ROM4n2`. Header displays clear identity, core philosophy ("Pragmatic Systems Engineering, Zero-Hallucination, Rigorous Defensive Design"), and active stack badges.
  2. **Flagship Project Scanning (3-10s)**: Visitor reviews the Structured Showcase Matrix with concise problem-solution metrics, architecture tags, and direct repository links for `DeLector`, `qingjian`, and `blind-llm-eyes`.
  3. **Verification & Action (10-20s)**: Visitor clicks into repository source code or uses provided contact/collaboration links (Email, SSH key, Git profile).
- **Friction Points & Mitigation**:
  - *Friction*: Third-party dynamic badge services (e.g., Shields.io, GitHub Readme Stats) frequently timeout, show broken image icons, or suffer rate-limiting.
  - *Mitigation*: Prefer native GitHub Markdown tables, raw SVG assets with fallback text, and avoid blocking external iframe/script loaders.
  - *Friction*: Low contrast in GitHub Dark/Light themes.
  - *Mitigation*: Use theme-adaptive GitHub Markdown image syntax (`#gh-dark-mode-only` and `#gh-light-mode-only`) or theme-agnostic minimalist monochrome palettes.
- **Error Feedback & Recovery**:
  All project references link directly to verified canonical GitHub repository URLs (`https://github.com/ROM4n2/...` and `https://github.com/qingjian-team/...`).

---

## 3. Architecture & Content Schema

The Profile README adheres to strict academic editorial style with zero emojis, zero innerHTML, and zero marketing buzzwords.

### 3.1 Document Layout Schema

```text
+--------------------------------------------------------------+
| 1. Header & Identity Anchor                                  |
|    - Name / Handle / One-line Engineering Baseline           |
|    - Focus: Go 1.24+ Concurrency, Agent Harness, Systems     |
+--------------------------------------------------------------+
| 2. Core Technical Competencies (Structured Table)           |
|    - Languages: Go, C/C++, Python, Rust                      |
|    - Systems: Concurrency, Linux/WSL2, Docker, MySQL, Redis  |
|    - Methodologies: TDD, Defensive Design, Verification First|
+--------------------------------------------------------------+
| 3. Flagship Projects Matrix (Problem -> Tech -> Impact)       |
|    - DeLector (Offline-First German NLP Workbench)           |
|    - Qingjian (Rust Dual-Language Input Method)              |
|    - blind-llm-eyes (Go Image Adaptation Proxy)              |
|    - know-her (Evidence-Graded Health Info System)           |
+--------------------------------------------------------------+
| 4. Engineering Principles & Invariants                       |
|    - Zero-Hallucination (Physical Evidence Over Claims)      |
|    - Anti-Sycophancy & Guard Clauses Flattening              |
|    - Local-First & Zero Leaks (RAII, Explicit Contexts)      |
+--------------------------------------------------------------+
| 5. Footprint & Contact                                       |
|    - Email, PGP/SSH public key, Collaboration Channels       |
+--------------------------------------------------------------+
```

### 3.2 Showcase Project Specifications

1. **DeLector (`ROM4n2/DeLector`)**:
   - Tagline: Local-first German CEFR (A1-C1) reading and exam preparation workbench.
   - Core Tech: Python 3.11, spaCy NLP pipeline, FSRS memory scheduling algorithm, Desktop/Mobile portable runtime.
   - Key Engineering Highlights: Completely offline capable, deterministic vocabulary parsing, rigorous data privacy.
2. **Qingjian (`qingjian-team/qingjian` / `ROM4n2/qingjian`)**:
   - Tagline: Dual-language cognitive Pinyin input method written in Rust.
   - Core Tech: Rust, OS-level input hooks, zero-copy candidate lexicon mapping.
   - Key Engineering Highlights: Active core contributor, zero raw unwrap discipline, dual-stream vocabulary acquisition.
3. **blind-llm-eyes (`ROM4n2/blind-llm-eyes`)**:
   - Tagline: High-throughput Go reverse proxy enabling vision capabilities for text-only LLMs.
   - Core Tech: Go 1.24+, net/http reverse proxy, Anthropic Messages API format translation.
   - Key Engineering Highlights: Streaming chunk parser, zero heap thrashing, low-latency bridge.
4. **know-her (`ROM4n2/know-her`)**:
   - Tagline: Evidence-graded health science publication and knowledge platform.
   - Core Tech: Static-first architecture, automated dead-link CI gates.
   - Key Engineering Highlights: Strict evidence tiers, zero-404 verification gates.

---

## 4. Edge Cases & Resilience

- **External Asset Failure**:
  If third-party badge providers fail, the Markdown structure must remain fully readable as plain text. Every badge image must have descriptive `alt` text.
- **GitHub Theme Adaptability**:
  All tables, dividers, and typography must render with high contrast across both GitHub Default Light and GitHub Dimmed/Dark themes.
- **XSS & Renderer Sanitization**:
  Strict adherence to standard GitHub Flavored Markdown (GFM). Zero raw HTML tags where markdown suffices; zero `style` attributes; zero unescaped dynamic scripts.

---

## 5. Test & Verification Strategy

- **Link Verification**:
  Every hyperlink in the rendered `README.md` must resolve to HTTP 200 via `curl -s -o /dev/null -w "%{http_code}" <URL>`.
- **Markdown Linting**:
  Verify formatting consistency using `npx markdownlint-cli` or equivalent Python AST markdown parser. Check for no trailing spaces, valid table alignments, and correct header hierarchy.
- **Visual Rendering Probe**:
  Inspect preview rendering inside headless Chromium / local preview server to confirm no layout shifts or broken table columns.

---

## 6. Fog of War & Scope Boundaries

- **Fog of War (Resolved / Explicitly Decided)**:
  - Excluded Projects: `ROM4n2/scriptorium-vault` and `Defensive Skills (dfs-*)` are excluded from this release as they are internal assets undergoing refactoring.
  - Excluded Projects: `ROM4n2/adk-go` is excluded from the primary showcase card to maintain focus on author/contributor works.
  - Automated Stats Cron: Dynamic commit-counter cron workflows are deferred; initial release utilizes deterministic static Markdown to ensure 100% uptime and zero maintenance overhead.
- **Out of Scope (Explicit Non-Goals)**:
  - Creating a complex JavaScript/React web application.
  - Embedding non-standard iframe/CSS widgets.
  - Social media marketing badges or vanity counters.

---

## Self-Review Checklist

- [x] Zero "TODO" or "TBD" placeholders across the specification.
- [x] No ambiguous assumptions or hidden scope creep.
- [x] The Ladder of Reuse checked: standard GitHub GFM native features over heavy dynamic microservices.
