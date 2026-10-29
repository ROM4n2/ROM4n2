# ROM4n2

```go
package identity

type SystemsEngineer struct {
	Handle     string   `json:"handle"`
	Status     string   `json:"status"`
	Focus      []string `json:"focus"`
	CoreStack  []string `json:"core_stack"`
	Discipline []string `json:"discipline"`
}

var Me = SystemsEngineer{
	Handle: "ROM4n2",
	Status: "Seeking Go Backend / Agent Harness Intern (Xi'an / Remote)",
	Focus: []string{
		"High-Throughput Go Systems & Concurrency",
		"Autonomous Agent Harness & Guard Architecture",
		"Offline-First Local Systems (Python, C/C++)",
	},
	CoreStack: []string{
		"Go 1.24+ (CSP, Worker Pool, singleflight, AIMD)",
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
- **Systems & Concurrency**: CSP / Goroutines / Channels · `context.WithCancelCause` · Worker Pool & Two-Phase Shutdown · `singleflight` (N→1 dedup) · AIMD Congestion Control · Linux POSIX · Docker · Low-Latency SSE Streaming
- **Agent Harness & Guardrails**: ReAct Loop · AST Conformance Gates · Adversarial Mutation Testing · Model Context Protocol (MCP) · FTS5+vec0 RRF Hybrid Retrieval
- **Data & Persistence**: SQLite (WAL, Two-Tier sharded locks, CAS transactional queue) · Redis · MySQL · Local-First Storage
- **Engineering Gates**: Strict TDD · Adversarial Mutation Testing · Monolith Decoupling · Zero-Leak Resource Lifetimes

---

### Flagship Projects & Open Source Contributions

| Project | Role | Architecture & Stack | Verifiable Engineering Highlights |
| --- | --- | --- | --- |
| [agent-runtime](https://github.com/ROM4n2/agent-runtime) | Author | Go 1.24+ · Worker Pool · SQLite WAL | Async Agent harness (P10); CAS queue & push scheduler; token-level SSE; upstream retry backoff & token cost metering; 21 ADRs; 545 tests (0 race) |
| [blind-llm-eyes](https://github.com/ROM4n2/blind-llm-eyes) | Author | Go 1.24+ · net/http · singleflight · AIMD | Streaming reverse proxy (22k+ LOC Go); AIMD adaptive concurrency (+50%); singleflight dedup (N→1); sharded cache (LRU + SQLite); 409 tests (0 race) |
| [DeLector](https://github.com/ROM4n2/DeLector) | Author | Go 1.24+ · Python 3.11 · DAG · Supervisor | Dual-engine (v5.19.0): 8,100+ LOC Go Agent subsystem (DAG engine, Supervisor daemon with cascading SIGTERM); single-instance lock & port rollover; 176 merged PRs; 2,584 tests |
| [google/adk-go](https://github.com/google/adk-go) | Contributor | Go · GORM NamingStrategy · Multi-Tenant | Authored [PR #1823](https://github.com/google/adk-go/pull/1823) (in review); solved table prefix isolation via `schema.TablerWithNamer`; 4-model mutation checks & disk SQLite E2E probe |
| [Qingjian](https://github.com/qingjian-team/qingjian) | Contributor | Rust · Upstream Engine & CLI | 25 merged upstream PRs; contributed core `v` mode date parser ([PR #720](https://github.com/qingjian-team/qingjian/pull/720)), dictionary derivation ([PR #718](https://github.com/qingjian-team/qingjian/pull/718)), custom phrase expansion ([PR #794](https://github.com/qingjian-team/qingjian/pull/794)), macOS QWERTZ fix ([PR #588](https://github.com/qingjian-team/qingjian/pull/588)); zero clippy warnings |
| [defensive-skills](https://github.com/ROM4n2/defensive-skills) | Author | Python · AST Gate · Mutation Testing · MCP | AI coding agent harness (v0.4.0); 28 DFS skills with 3-tier progressive disclosure & budget gates; AST authorization gates; 114 tests across 9 suites |
| [know-her](https://github.com/ROM4n2/know-her) | Author | Static Architecture · Dead-Link CI | Evidence-graded health reference; automated dead-link CI gates; deterministic static publishing; 25 tests clean |

---

### Live: Chances of Getting Hired

- **Target Roles**: `Go Backend Engineering Intern` · `AI Agent Infrastructure & Harness Architecture Intern` (Xi'an on-site or Remote · Available 4–5 days/week · 3–6+ months)
- **Direct Technical Pitch**: Prefer a concrete technical challenge to a cover letter. Hand me a goroutine leak, a cascading cancellation race, or an AST gate that leaks edge cases, and I will trace root causes and deliver passing deterministic receipts before the day ends.

| Dimension | Physical Signal / Proof | Verifiable Receipt |
| --- | --- | --- |
| Concurrency & Runtime | Go 1.24+ Worker Pool, CAS transactional queue, AIMD streaming | [agent-runtime](https://github.com/ROM4n2/agent-runtime) (545 tests, 0 race) · [blind-llm-eyes](https://github.com/ROM4n2/blind-llm-eyes) (409 tests) |
| Agent Harness & Guardrails | AST Conformance Gate, mutation verification, MCP protocol | [defensive-skills](https://github.com/ROM4n2/defensive-skills) (114 tests) · [DeLector](https://github.com/ROM4n2/DeLector) (Go DAG + Supervisor) |
| OSS Collaborative Delivery | Strict RFC 2119, upstream clippy gates, GORM isolation fix | [qingjian](https://github.com/qingjian-team/qingjian) (25 merged PRs) · [adk-go](https://github.com/google/adk-go/pull/1823) (PR #1823 in review) |
| Test Discipline & Invariants | Automated execution receipts over self-reporting | 5,800+ collected tests across portfolio, 100% clean on default branches |

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
