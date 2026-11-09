# ROM4n2

```go
package identity

import "context"

// Engineer is the delivery contract: deterministic concurrency runtimes,
// agent-harness guardrails, and verifiable receipts behind every claim.
type Engineer interface {
    Supervise(ctx context.Context, tasks <-chan Task) (<-chan Receipt, error)
    Deliver(ctx context.Context, scope Scope) (Artifact, error)
}

// Dispatch: cooperative preemption, worker pool, AIMD, WithCancelCause.
// Availability: remote engineering roles (Go backend / Agent harness) primary;
// limited fixed-scope project work in parallel. Sources + test receipts.
```

```text
+-----------------------------------------------------------------------------+
|                         SYSTEMS RUNTIME & HARNESS                           |
+-----------------------------------------------------------------------------+
|  [ Ingest / SSE ]       -->  [ singleflight (N->1) ]  -->  [ AIMD Controller ] |
|  [ Worker Pool ]        -->  [ SQLite WAL CAS Queue ] -->  [ CancelCause Trap ] |
|  [ AST Fitness Gates ]  -->  [ Mutation Test Harness] -->  [ Zero-Race Receipts]|
+-----------------------------------------------------------------------------+
```

---

### Tech Stack & Core Competencies

- **Primary Languages**: `Go (1.24+)` · `C/C++` · `Python (3.11+)`
- **OSS Collaboration**: `Rust` (upstream PR delivery; not a service offering)
- **Systems & Concurrency**: CSP / Goroutines / Channels · `context.WithCancelCause` · Worker Pool & Two-Phase Shutdown · `singleflight` (N->1 dedup) · AIMD Congestion Control · Linux POSIX · Docker · Low-Latency SSE Streaming
- **Agent Harness & Guardrails**: ReAct Loop · AST Conformance Gates · Adversarial Mutation Testing · Model Context Protocol (MCP) · FTS5+vec0 RRF Hybrid Retrieval
- **Data & Persistence**: SQLite (WAL, Two-Tier sharded locks, CAS transactional queue) · Redis · MySQL · Local-First Storage
- **Engineering Gates**: Strict TDD · Adversarial Mutation Testing · Monolith Decoupling · Zero-Leak Resource Lifetimes

---

### Availability & Collaboration

- **Primary - Remote Engineering Roles**: `Go Backend` / `Agent Infrastructure & Harness` · internship, long-term part-time, or full-time remote · 4-5 days/week · 3-6+ months.
- **Parallel - Fixed-Scope Project Work**: Go concurrency audits, MCP / CLI tooling, race-clean receipts. Single-item scope, written acceptance criteria, platform escrow or milestone payment.
- **Technical Pitch**: Hand me a goroutine leak, a cascading cancellation race, or an AST gate leaking edge cases; root cause plus passing deterministic receipts.

---

### Flagship Projects & Open Source Contributions

| Project | Role | Architecture & Stack | Verifiable Engineering Highlights |
| --- | --- | --- | --- |
| [agent-runtime](https://github.com/ROM4n2/agent-runtime) | Author | Go 1.24+ · Worker Pool · SQLite WAL | Async Agent harness; CAS queue & push scheduler; token-level SSE; upstream retry & token metering; 21 ADRs; 545 tests (race clean) |
| [blind-llm-eyes](https://github.com/ROM4n2/blind-llm-eyes) | Author | Go 1.24+ · net/http · singleflight · AIMD | Streaming vision proxy (22,109 LOC); errgroup parallel image processing 39.7 s -> 19.8 s (-50%, bench receipt); singleflight dedup; sharded LRU + SQLite cache; 409 tests (race clean) |
| [DeLector](https://github.com/ROM4n2/DeLector) | Author | Python 3.11 · Go 1.24+ · FastAPI | German CEFR A1-C1 reader & exam workbench (v5.22.1); offline-first spaCy NLP + FSRS; Go companion agent & supervisor daemon; 315 merged PRs; 2,999 pytest + 218 Go tests |
| [defensive-skills](https://github.com/ROM4n2/defensive-skills) | Author | Python · AST Gate · Mutation Testing · MCP | AI coding-agent harness & conformance gates; 28-skill tree (27 sub-skills + router), 3-tier disclosure & budget gates; AST authorization gates; 115 tests |
| [google/adk-go](https://github.com/google/adk-go) | Contributor | Go · GORM · Agent toolkit | 3 PRs under review (none merged yet): [#1823](https://github.com/google/adk-go/pull/1823) GORM TablePrefix isolation · [#1978](https://github.com/google/adk-go/pull/1978) value-configured launcher Runnable · [#1990](https://github.com/google/adk-go/pull/1990) live tool responses across reconnect |
| [Qingjian](https://github.com/qingjian-team/qingjian) | Contributor | Rust · IME Engine & CLI | 26 merged upstream PRs: [#720](https://github.com/qingjian-team/qingjian/pull/720) date parser · [#794](https://github.com/qingjian-team/qingjian/pull/794) custom phrases · [#825](https://github.com/qingjian-team/qingjian/pull/825) dual/full pinyin mixed typing |

---

### Verifiable Receipts

| Dimension | Physical Signal / Proof | Verifiable Receipt |
| --- | --- | --- |
| Concurrency & Runtime | Go 1.24+ Worker Pool, CAS transactional queue, AIMD streaming | [agent-runtime](https://github.com/ROM4n2/agent-runtime) (545 tests, go test -race clean) · [blind-llm-eyes](https://github.com/ROM4n2/blind-llm-eyes) (409 tests) |
| Agent Harness & Guardrails | AST Conformance Gate, mutation verification, MCP protocol | [defensive-skills](https://github.com/ROM4n2/defensive-skills) (115 tests) · [DeLector](https://github.com/ROM4n2/DeLector) (2,999 pytest + 218 Go) |
| OSS Collaborative Delivery | RFC 2119 discipline, upstream Go/Rust review gates | [qingjian](https://github.com/qingjian-team/qingjian) (26 merged PRs) · [adk-go](https://github.com/google/adk-go) (3 PRs open for review) |
| Test Discipline & Invariants | Execution receipts over self-reporting | 4,286 itemized tests across four flagship repos; race detector clean on both Go runtimes |

```bash
# Deterministic Evidence Probe: clone & run race detector on flagship runtime
git clone --depth 1 https://github.com/ROM4n2/agent-runtime.git && cd agent-runtime && go test -race -count=1 ./...
```

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
- **Collaboration**: Open to remote engineering roles in Go concurrency runtime design, autonomous agent harnesses, and systems infrastructure; limited fixed-scope project work alongside.
