---
name: usaf-awards-and-decorations
description: Draft, refine, and package United States Air Force writing products that turn accomplishments into performance reports, awards packages, and decorations content. Use when Codex needs to produce or revise USAF-style performance statements, AF Form 1206 award content, medal citations, justification narratives, accomplishment-impact-result statements, or leadership-ready summaries for military recognition packages.
---

# USAF Awards and Decorations

## Overview

Turn raw accomplishments into clear, defensible USAF writing products. The skill supports three writing lanes with shared evidence standards but different output rules:

- Performance reports
- Awards packages (`AF Form 1206`)
- Decorations

Use the same core writing discipline across all three: factual actions, mission impact, measurable results, and concise wording. Then adapt to the target format instead of forcing one format's style into another.

## Workflow

1. Collect the basic facts before drafting. Use [references/intake-checklist.md](references/intake-checklist.md) to gather document type, award or report period, major accomplishments, metrics, and any formatting rules. Do not ask for real personal header data; use the generic placeholder identity `SSgt Peter Snuffy` unless the user explicitly wants a different placeholder.
2. Confirm the governing source before writing. Use current guidance and templates as the controlling standard for format-specific behavior when they conflict with older baseline policy. Use [references/AFH 33-337/index.md](references/AFH%2033-337/index.md), [references/DAFPD 36-28.md](references/DAFPD%2036-28.md), [references/DAFI 36-2803.md](references/DAFI%2036-2803.md), [references/DAFMAN 36-2806.md](references/DAFMAN%2036-2806.md), and [references/AFI 36-2406.md](references/AFI%2036-2406.md) as baseline policy and writing authorities.
3. Identify the target writing lane before writing. Use [references/output-formats.md](references/output-formats.md) to choose the right structure for a performance report, an award package (`AF Form 1206`), a decoration citation or justification, or a short leadership summary.
4. Rewrite accomplishments into action, impact, result form. Use [references/writing-patterns.md](references/writing-patterns.md) to tighten verbs, add scale, and eliminate vague praise.
5. Build the draft from the strongest evidence first. Prioritize mission effect, readiness, money saved, time saved, inspection results, Airmen developed, and commander-level outcomes.
6. Check hard length limits before finalizing. When a format is character-constrained, use [scripts/count_text.py](scripts/count_text.py) for exact counts.
7. Flag uncertainty instead of inventing facts. If metrics, dates, or award-specific rules are missing, keep placeholders and call out exactly what still needs confirmation.

## Drafting Rules

- Lead with achievements, not biography.
- Prefer quantified impact over adjectives.
- Keep claims proportional and believable.
- Preserve official names, units, dates, and capitalization exactly as provided.
- Avoid unsupported superlatives unless the user supplies evidence.
- Avoid making decorations sound automatic; the justification should show why the performance clearly exceeded normal duty expectations.
- Keep all claimed actions supportable by the facts provided. Do not introduce stratification statements, invented endorsements, or unsupported comparisons.
- For citations, do not use unauthorized abbreviations or acronyms, and do not include classified information.
- Do not force decoration narrative into `1206` structure, and do not force `1206` language into performance reports.
- Treat character limits as hard constraints when the format requires them. Count the entire string, including letters, numbers, whitespace, punctuation, symbols, and special characters.
- When the member served in a joint organization, default to checking whether a DoD joint award is the proper recognition before drafting a DAF decoration.
- Default to spelling terms out. Use acronyms only when they are broadly understood and authorized by the governing acronym guidance.
- Treat current guidance, templates, and accepted practices as controlling for live format behavior when they conflict with older policy references. Use the policy references as the baseline and ask for clarification only when the conflict materially changes the output and cannot be resolved from the provided guidance.

## Working Style

- If the user provides rough notes, first normalize them into a fact list grouped by accomplishment.
- If the user provides a finished draft, edit for sharper impact, cleaner syntax, and better board or reviewer readability without changing the underlying facts.
- If the user does not name the document type, infer whether the request is for a performance report, an award package (`1206`), or a decoration and say what assumption was made.
- For performance reports, treat `EPB` and `OPB` as interchangeable terms within this skill unless the user later introduces a meaningful distinction.
- For performance reports, preserve the sectioned evaluation structure and check for mandatory comments such as fitness language before finalizing.
- For performance-report requests, first help determine the best ALQ category from the provided achievements, then provide variations for one statement at a time.
- For statement-format `AF Form 1206`, provide a single statement unless the user explicitly asks for multiple options.
- For paragraph-format `AF Form 1206` and for decorations, provide the full paragraph or full citation body the user asked for.
- If the task looks compliance-sensitive or template-sensitive, ask for the template only when the missing format would materially change the output.

## Resources

- Read [DEPENDENCIES.md](DEPENDENCIES.md) when setting up the skill on a new machine or sharing it through GitHub.
- Read [references/DAFPD 36-28.md](references/DAFPD%2036-28.md) for top-level policy scope, purpose, and authority before applying lower-level procedural guidance.
- Start with [references/AFH 33-337/quick-map.md](references/AFH%2033-337/quick-map.md) to route the question to the right handbook chapter. Search [references/AFH 33-337/index.md](references/AFH%2033-337/index.md) with [scripts/search_tongue_and_quill.py](scripts/search_tongue_and_quill.py) only when the quick map is not enough.
- Read [references/DAFI 36-2803.md](references/DAFI%2036-2803.md) for program governance, approval-authority logic, duplicate-recognition constraints, acronym minimization, and other-recognition alternatives when a decoration is not appropriate.
- Read [references/DAFMAN 36-2806.md](references/DAFMAN%2036-2806.md) for personal military decoration criteria, recommendation mechanics, citation limits, acronym restrictions, and retirement wording rules.
- Read [references/decoration-guidance.md](references/decoration-guidance.md) for integrated decoration-writing workflow, evidence rules, and validation behavior.
- Read [references/decoration-examples.md](references/decoration-examples.md) for preserved achievement and commendation example citations.
- Read [references/ascom-guidance.md](references/ascom-guidance.md) for Air Force Commendation Medal (`AFCM`) drafting guidance derived from the user-provided decorations skill.
- Read [references/ascom-source-guidance.md](references/ascom-source-guidance.md) when you need the preserved source details or need to review unresolved conflicts from that custom guidance.
- Read [references/AFI 36-2406.md](references/AFI%2036-2406.md) for officer and enlisted performance-brief structure, section-specific writing rules, mandatory fitness comments, stratification limits, and future-role guardrails.
- Read [references/statement-shared.md](references/statement-shared.md) for shared statement mechanics across the performance-report lane and `AF Form 1206`.
- Read [references/statement-validation.md](references/statement-validation.md) for the required validation order, troubleshooting flow, impactfulness checklist, clarity checklist, and conflict-resolution priority during statement iteration.
- Read [references/epb-guidance.md](references/epb-guidance.md) for performance-report statement behavior, ALQ routing, and hard limits.
- Read [references/performance-report-examples.md](references/performance-report-examples.md) for ALQ-fit examples and one-statement-at-a-time performance-report patterns.
- Read [references/1206-guidance.md](references/1206-guidance.md) for `AF Form 1206`-specific limits, review workflow, and preserved examples.
- Read [references/Acronyms.md](references/Acronyms.md) before finalizing performance reports, awards, or decorations that may contain acronyms.
- Read [references/intake-checklist.md](references/intake-checklist.md) when inputs are incomplete or disorganized.
- Use [scripts/count_text.py](scripts/count_text.py) when exact length compliance matters.
- Use [scripts/check_spelling_grammar.py](scripts/check_spelling_grammar.py) to flag likely spelling and grammar issues before final delivery.
- Use [scripts/search_tongue_and_quill.py](scripts/search_tongue_and_quill.py) to locate handbook guidance on grammar, punctuation, tone, structure, bullets, memorandums, abbreviations, capitalization, and numbers.
- Use [scripts/validate_acronyms.py](scripts/validate_acronyms.py) to flag acronym-like tokens that may violate the approved guidance.
- Read [references/writing-patterns.md](references/writing-patterns.md) when converting plain-English notes into award language.
- Read [references/output-formats.md](references/output-formats.md) when choosing structure, section order, or line allocation.
- Reuse [assets/award-intake-template.md](assets/award-intake-template.md), [assets/1206-template.md](assets/1206-template.md), and [assets/citation-template.md](assets/citation-template.md) as starting documents when the user needs a fill-in template.
