# ROM4n2

```go
package identity

type SystemsEngineer struct {
	Handle     string   `json:"handle"`
	Focus      []string `json:"focus"`
	CoreStack  []string `json:"core_stack"`
	Discipline []string `json:"discipline"`
}

var Me = SystemsEngineer{
	Handle: "ROM4n2",
	Focus: []string{
		"High-Throughput Go Systems & Concurrency",
		"Autonomous Agent Harness & Guard Architecture",
		"Offline-First Local Systems (Python, C/C++)",
	},
	CoreStack: []string{
		"Go 1.24+ (CSP, net/http, singleflight, AIMD)",
		"C/C++, Python 3.11+",
		"Linux / POSIX, Docker, Deterministic CI",
	},
	Discipline: []string{
		"Zero-Hallucination (Receipts Over Claims)",
		"Strict TDD & Adversarial Mutation Gates",
		"Guard Clauses (Max Indentation: 2)",
	},
}
```

---

### Tech Stack & Core Competencies

- **Primary Languages**: `Go (1.24+)` · `C/C++` · `Python (3.11+)`
- **OSS Collaboration**: `Rust` (Upstream PR delivery & RFC feature work via compiler/clippy gates)
- **Systems & Concurrency**: CSP / Goroutines / Channels · `singleflight` (N→1 dedup) · AIMD Congestion Control · Linux POSIX · Docker · Low-Latency Streaming
- **Data & Persistence**: SQLite (WAL, Two-Tier sharded locks) · Redis · MySQL · Local-First Storage
- **Engineering Gates**: Strict TDD · Adversarial Mutation Testing · Monolith Decoupling · Zero-Leak Resource Lifetimes

---

### Flagship Projects & Open Source Contributions

| Project | Role | Architecture & Stack | Verifiable Engineering Highlights |
| --- | --- | --- | --- |
| [blind-llm-eyes](https://github.com/ROM4n2/blind-llm-eyes) | Author | Go 1.24+ · net/http · singleflight · AIMD | Low-latency SSE streaming proxy; AIMD adaptive concurrency; in-flight image dedup (N→1); two-tier cache (LRU + SQLite); `go test -race` CI |
| [DeLector](https://github.com/ROM4n2/DeLector) | Author | Python 3.11 · spaCy · FSRS Algorithm | 170+ merged PRs; offline-first desktop/mobile reading workbench; modular monolith decoupling; 2,300+ deterministic tests |
| [Qingjian](https://github.com/qingjian-team/qingjian) | Contributor | Rust · Upstream Engine & CLI | Contributed core `v` mode date parser ([PR #720](https://github.com/qingjian-team/qingjian/pull/720) merged) & dictionary derivation ([PR #718](https://github.com/qingjian-team/qingjian/pull/718)); zero clippy warnings |
| [know-her](https://github.com/ROM4n2/know-her) | Author | Static Architecture · Dead-Link CI | Evidence-graded women's health platform; automated dead-link CI gates; deterministic static publishing |

---

### Engineering Principles & Invariants

1. **Zero-Hallucination (Physical Evidence Over Claims)**: Statements, benchmarks, and bug fixes require automated execution receipts and verifiable test outputs before landing.
2. **Anti-Sycophancy & Guard Clauses Flattening**: Maximum two indentation levels; branch boundaries enforced early without nested logic drift.
3. **Local-First & Zero Leaks**: Deterministic RAII/context lifetimes; fully functional offline without unvetted cloud dependencies.

---

### Contact & Identity

- **Email**: [beianderen@gmail.com](mailto:beianderen@gmail.com)
- **GitHub Profile**: [https://github.com/ROM4n2](https://github.com/ROM4n2)
- **Public Keys**: SSH keys available at [https://github.com/ROM4n2.keys](https://github.com/ROM4n2.keys)
- **Collaboration**: Open for technical exchanges in Go concurrency runtime design, autonomous agent harnesses, and systems infrastructure.
