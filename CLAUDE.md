# Entrepreneuriat: finding a company idea

This repo is a workspace for finding, validating, and choosing a company idea.
Skills live in `.claude/skills/` (see `.claude/skills/SOURCES.md`).

## Founder profile

Fill this in. Several skills (especially `llm-council` and `startup-design`)
read this file first, and their advice gets much more specific when it is filled.

- **Background / skills:** Marketing. Finishing a master's degree, currently a
  work-study (alternance) Product Manager at EDF, in charge of electricity offers
  for small and medium businesses (TPE / PME).
- **Industries I know from the inside:** Energy / electricity retail for B2B SMBs.
- **Interests:** AI, deeptech, agrifood (agroalimentaire). Open to any field.
- **Problems I have personally seen or suffered at work:** _TODO (e.g. what SMB
  customers struggle with on energy bills, contracts, consumption...)_
- **People I can easily reach (network, communities):** _TODO (EDF colleagues,
  SMB customers, master's classmates and alumni...)_
- **Time available:** _TODO (full-time / side project, hours per week)_
- **Budget / runway:** _TODO_
- **Geography / language of first market:** _TODO_
- **Ambition:** _TODO (lifestyle business, bootstrapped SaaS, VC-scale startup...)_
- **Things I do NOT want to do:** _TODO_

## Workflow

1. **Generate**: `ai-startup-opportunity-generator` (scored, ranked opportunities),
   `jobs-to-be-done` (find unmet jobs), `brainstorm-ideas-new`.
2. **Shortlist**: `llm-council` to pressure-test the top 3-5 ideas against each other.
3. **Research the favourite**: `startup-design` (Fast Track for a quick go/no-go,
   full mode for the deep version), `market-sizing`, `beachhead-segment`.
4. **Find the risks**: `identify-assumptions-new`, `lean-canvas`.
5. **Talk to real customers**: `mom-test` for the interview script and reading the answers.
6. **Decide**: `llm-council` again with the interview evidence.

Save work for each idea under `ideas/<idea-name>/`.
