# entrepreneuriat

A Claude Code workspace for finding and validating a company idea.

## Installed skills

They live in `.claude/skills/`. Claude Code loads them automatically whenever
this repo is opened, locally or in a Claude Code cloud session.

| Stage | Skill | Use it for | Example prompt |
|-------|-------|-----------|----------------|
| Generate | `ai-startup-opportunity-generator` | Workflow-grounded ideas, scored on 6 dimensions, checked against 10 failure patterns | "Give me 10 startup ideas for a solo founder in logistics" |
| Generate | `jobs-to-be-done` | Find unmet "jobs" customers are struggling with | "What jobs are freelancers badly served on for invoicing?" |
| Generate | `brainstorm-ideas-new` | Multi-perspective ideation (PM / designer / engineer) | `/brainstorm-ideas-new AI tool for small clinics` |
| Decide | `llm-council` | 5 advisors + anonymous peer review + chairman verdict | "Council this: which of these 3 ideas should I pursue?" |
| Validate | `startup-design` | Full research → strategy → validation, or Fast Track go/no-go | "Quick validation, fast track: <idea>" |
| Validate | `market-sizing` | TAM / SAM / SOM, top-down and bottom-up | `/market-sizing <idea> in France` |
| Validate | `beachhead-segment` | Pick the first, smallest winnable market | `/beachhead-segment <idea>` |
| Validate | `identify-assumptions-new` | Risky assumptions across 8 categories | `/identify-assumptions-new <idea>` |
| Validate | `lean-canvas` | One-page business model | `/lean-canvas <idea>` |
| Customers | `mom-test` | Interview scripts that don't produce false positives | "Write me a Mom Test interview script for <segment>" |

See `CLAUDE.md` for the recommended workflow and the founder profile to fill in.

## Idea search runs

- First run (October 2026): research in `ideas/_recherche/`, winning idea in `ideas/recrutement-garages/`.
- To rerun the whole process in a new conversation, follow `relancer-la-recherche.md` (step-by-step guide and ready-to-paste prompt, in French).
Sources, commits and licenses are listed in `.claude/skills/SOURCES.md`.
