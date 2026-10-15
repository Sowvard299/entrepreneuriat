# Skill sources

Third-party skills vendored into this repo. Each was read in full before being added.
To update one, re-copy its folder from the source repo at a newer commit.

| Skill | Source | Commit | License |
|-------|--------|--------|---------|
| `llm-council` | [aiwithremy/claude-skills-llm-council](https://github.com/aiwithremy/claude-skills-llm-council) (by Ole Lehmann, after Karpathy's LLM Council) | `55ee36e` | none stated in source repo |
| `ai-startup-opportunity-generator` | [nmsavaliya/claude-startup-validator](https://github.com/nmsavaliya/claude-startup-validator) | `8f558c9` | MIT |
| `startup-design` | [ferdinandobons/startup-skill](https://github.com/ferdinandobons/startup-skill) | `a5f97c3` | MIT |
| `brainstorm-ideas-new`, `identify-assumptions-new`, `market-sizing`, `beachhead-segment`, `lean-canvas` | [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | `8607e3b` | MIT |
| `interview-script`, `summarize-interview`, `brainstorm-experiments-new`, `competitor-analysis`, `sentiment-analysis` | [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | `c68487d` | MIT |
| `before-you-build` | [wshobson/agents](https://github.com/wshobson/agents) (`plugins/before-you-build`) | `46891e7` | MIT |
| `mom-test`, `jobs-to-be-done` | [wondelai/skills](https://github.com/wondelai/skills) | `c172996` | MIT |
| `startup-competitors`, `startup-positioning`, `startup-pitch` (added 2026-10-15) | [ferdinandobons/startup-skill](https://github.com/ferdinandobons/startup-skill) | `a5f97c3` | MIT |
| `cac-modeler`, `competitor-mapper`, `decision-memo`, `desire-evaluator`, `distribution-analysis`, `idea-scoring`, `pivot-engine`, `pricing-and-wtp`, `retention-predictor`, `tam-sam-som-builder`, `trend-analysis`, `trend-to-product-mapper`, `user-background-interviewer`, `user-segmentation-profiler`, `weakness-detection` (added 2026-10-15) | [MaxKmet/idea-validation-agents](https://github.com/MaxKmet/idea-validation-agents) (canonical `skills/<name>/`, not the `.claude/skills/` stubs) | `3a4c800` | MIT |
| `business-model`, `monetization-strategy`, `pricing-strategy`, `startup-canvas`, `value-proposition`, `swot-analysis`, `porters-five-forces`, `pestle-analysis`, `ansoff-matrix`, `product-vision`, `product-strategy`, `gtm-strategy`, `gtm-motions`, `ideal-customer-profile`, `growth-loops`, `competitive-battlecard`, `market-segments`, `user-personas`, `user-segmentation`, `customer-journey-map`, `positioning-ideas`, `value-prop-statements`, `product-name`, `marketing-ideas`, `north-star-metric`, `opportunity-solution-tree`, `prioritize-assumptions`, `pre-mortem`, `strategy-red-team`, `create-prd`, `draft-nda`, `privacy-policy` (added 2026-10-15) | [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | `c68487d` | MIT |

Each MIT-licensed skill folder carries its original `LICENSE` file.

Notes on the 2026-10-15 batch:
- The MaxKmet skills target indie B2C mobile apps (App Store, TikTok, USD price benchmarks). Read their
  benchmarks as US app-store figures, not as French data; the thresholds and score grid of `CLAUDE.md` still
  win over `idea-scoring`. They write their outputs to `memory/` at the repo root (their convention):
  `memory/README.md`, `memory/market_insights/README.md` and `memory/extra-context/core-human-desires.md`
  (read by `desire-evaluator` and `user-background-interviewer`) are copied verbatim from the same commit.
  Their orchestrator (`CLAUDE.md` + `workflows/`) is not copied: skills are called one by one.
  `desire-evaluator`, `retention-predictor`, `weakness-detection` and `user-segmentation-profiler` are v0.1.0
  upstream, with TODOs left in place.
- `draft-nda` and `privacy-policy` produce drafts only; a French lawyer must review them (French law, RGPD).

Not vendored (2026-10-15), from the list the user supplied:
- `Solo-Entrepreneur/solopreneur` (MIT): the skill is a wrapper around 20 lecture transcripts of Stanford
  CS183B "How to Start a Startup" (about 870 KB). The repo's MIT license may not cover third-party
  transcripts, and this repo is public. The source repo ships a `.claude-plugin/marketplace.json`, so it can be
  installed locally as a plugin without copying it here.
- `pssah4/digital-innovation-agents` (MIT): `business-analysis` depends on its own `project-conventions`
  framework (software V-model); `humanizer` is English-only, points to a missing vocabulary file, and its
  examples come from Wikipedia (CC BY-SA). The other skills are software engineering, out of scope.
- `rhofkens/business-idea-multi-agent` (TypeScript app), `simerusm/ai-simulated-startup` (app, no license),
  `fayerman-source/startup-ideas` and `ashishpatel26/500-AI-Agents-Projects` (lists): no skill to copy.

Not vendored (2026-10-13): `startup-painpoint-scout` from
[vasilyu1983/AI-Agents-public](https://github.com/vasilyu1983/AI-Agents-public) (`3ee3637`, MIT). It depends on a
separate `research-painpoint-scanner` skill and targets Reddit/HN, which our agents cannot read. Its evidence
rules (≥ 3 threads per theme, top themes on ≥ 2 sources, frequency × severity × addressability, stop protocol)
are reused in `.claude/agents/chercheur.md`, credited there. `voice-of-customer-miner` (deanpeters) is
CC BY-NC-SA: not copied.

Homemade (no external source): the `market-segment-scanner` skill, and the subagents in
`.claude/agents/` (`chercheur`, `auditeur`, `verificateur`).

Note: the `mom-test` and `jobs-to-be-done` "Further Reading" book links include
the author's Amazon affiliate tag.
