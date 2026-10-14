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

Each MIT-licensed skill folder carries its original `LICENSE` file.

Not vendored (2026-10-13): `startup-painpoint-scout` from
[vasilyu1983/AI-Agents-public](https://github.com/vasilyu1983/AI-Agents-public) (`3ee3637`, MIT). It depends on a
separate `research-painpoint-scanner` skill and targets Reddit/HN, which our agents cannot read. Its evidence
rules (≥ 3 threads per theme, top themes on ≥ 2 sources, frequency × severity × addressability, stop protocol)
are reused in `.claude/agents/chercheur.md`, credited there. `voice-of-customer-miner` (deanpeters) is
CC BY-NC-SA: not copied.

Re-checked on 2026-10-14: the six skills added on 2026-10-13 (`before-you-build`, `interview-script`,
`summarize-interview`, `competitor-analysis`, `sentiment-analysis`, `brainstorm-experiments-new`) were re-read in
full and diffed against their upstream commits above: byte-identical, plus the upstream `LICENSE` file.
`startup-painpoint-scout` was re-read in full at `3ee3637` (also the repo's latest commit on that date): its
"Required Skill" section makes it abort unless `research-painpoint-scanner` is installed, and that skill does not
exist anywhere in the public repo. Copied as is, the agent would not run, so it stays not vendored.

Homemade (no external source): the `market-segment-scanner` skill, and the subagents in
`.claude/agents/` (`chercheur`, `auditeur`, `verificateur`).

Note: the `mom-test` and `jobs-to-be-done` "Further Reading" book links include
the author's Amazon affiliate tag.
