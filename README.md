# ROM4n2

Pragmatic Systems Engineering, Zero-Hallucination, Rigorous Defensive Design.

Systems engineer focused on Go 1.24+ Concurrency, Agent Harness Architecture, and Systems Programming (C/C++, Rust). Building verifiable, local-first architectures with strict invariant guarantees.

---

## Core Technical Competencies

| Domain | Focus Areas | Key Technologies & Invariants |
| --- | --- | --- |
| Languages | Systems programming, high-concurrency runtimes, automated verification tooling | Go (1.24+), C/C++, Python (3.11+), Rust |
| Systems & Infrastructure | Low-latency network I/O, deterministic container environments, structured caching | Concurrency (CSP / Channels), Linux / WSL2, Docker, MySQL, Redis |
| Methodologies | Defensive verification harnesses, guard clause design, zero-leak resource management | Strict TDD, Defensive Design, Verification First |

---

## Flagship Projects Matrix

| Project | Focus | Architecture & Stack | Key Highlights |
| --- | --- | --- | --- |
| [DeLector](https://github.com/ROM4n2/DeLector) | Offline-First German CEFR (A1-C1) Reading Workbench | Python 3.11, spaCy NLP pipeline, FSRS algorithm | Deterministic vocabulary parsing, offline-first exam prep, zero network dependencies |
| [Qingjian](https://github.com/qingjian-team/qingjian) | Dual-Language Cognitive Pinyin Input Method | Rust, OS-level input hooks, zero-copy candidate lexicon mapping | Active core contributor, zero raw unwrap discipline, dual-stream vocabulary acquisition |
| [blind-llm-eyes](https://github.com/ROM4n2/blind-llm-eyes) | Vision Adaptation Reverse Proxy for Text-Only LLMs | Go 1.24+, net/http streaming proxy, Anthropic Messages API translation | High-throughput streaming chunk parser, low-latency protocol bridge |
| [know-her](https://github.com/ROM4n2/know-her) | Evidence-Graded Health Science Publication Platform | Static-first architecture, automated dead-link CI gates | Structured evidence grading tiers, automated dead-link CI gates, deterministic builds |

---

## Engineering Principles & Invariants

- Zero-Hallucination (Physical Evidence Over Claims): Statements, benchmarks, and bug fixes require automated execution receipts and verifiable test outputs before landing.
- Anti-Sycophancy & Guard Clauses Flattening: Deeply nested branching is eliminated in favor of early-return guard clauses (maximum two indentation levels). Code structure enforces invariant boundaries directly.
- Local-First & Zero Leaks: Resource lifetimes are managed deterministically via RAII, explicit contexts, and deferred cleanups. Core tools remain functional offline without unvetted external service dependencies.

---

## Footprint & Contact

- Email: [beianderen@gmail.com](mailto:beianderen@gmail.com)
- GitHub Profile: [https://github.com/ROM4n2](https://github.com/ROM4n2)
- Public Keys: SSH keys available at [https://github.com/ROM4n2.keys](https://github.com/ROM4n2.keys)
- Collaboration Channels: Open for technical exchanges in Go concurrency runtime design, autonomous agent harnesses, and systems infrastructure.
