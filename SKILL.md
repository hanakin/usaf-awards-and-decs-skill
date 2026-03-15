---
name: usaf-awards-and-decorations
description: Draft, refine, and package United States Air Force writing products that turn accomplishments into performance reports, awards packages, and decorations content. Use when Codex needs to produce or revise USAF-style performance statements, AF Form 1206 award content, medal citations, accomplishment-impact-result statements, or leadership-ready summaries for military recognition packages.
---

# USAF Awards and Decorations

## Overview

Turn raw accomplishments into clear, defensible USAF writing help. The skill supports three writing lanes with shared evidence standards but different output rules:

- Performance reports
- Awards packages (`AF Form 1206`)
- Decorations

Use the same core writing discipline across all three: factual actions, mission impact, measurable results, and concise wording. Then adapt to the target format instead of forcing one format's style into another.

This skill is assistive and incremental by default. Do not assume the user wants a full package from start to finish. Provide only the specific piece requested, using only the inputs needed for that piece, and ask for clarification or feedback along the way when it materially improves the result.

## Workflow

1. Identify the specific help requested. Determine whether the user wants a duty description, one performance statement, ALQ-category help, one `AF Form 1206` statement, a full `1206` paragraph, a decoration citation, or some other discrete piece.
2. Collect only the facts needed for that requested piece. Use [references/intake-checklist.md](references/intake-checklist.md) only as a lane router, then follow the lane-specific intake file. Do not ask for real personal header data; use the generic placeholder identity `SSgt Peter Snuffy` unless the user explicitly wants a different placeholder.
3. Confirm the governing source before writing. Use current guidance and templates as the controlling standard for format-specific behavior when they conflict with older baseline policy. Use [references/AFH 33-337/index.md](references/AFH%2033-337/index.md), [references/DAFPD 36-28.md](references/DAFPD%2036-28.md), [references/DAFI 36-2803.md](references/DAFI%2036-2803.md), [references/DAFMAN 36-2806.md](references/DAFMAN%2036-2806.md), and [references/AFI 36-2406.md](references/AFI%2036-2406.md) as baseline policy and writing authorities.
4. Identify the target writing lane before writing. Use [references/output-formats.md](references/output-formats.md) to choose the right structure for a performance report, an award package (`AF Form 1206`), a decoration citation, or a short leadership summary.
5. Rewrite the provided material into action, impact, result form when the requested piece requires it. Use [references/writing-patterns.md](references/writing-patterns.md) to tighten verbs, add scale, and eliminate vague praise.
6. Build only the requested output. Do not expand into additional sections unless the user asks for them.
7. Check hard length limits before finalizing. When a format is character-constrained, use [scripts/count_text.py](scripts/count_text.py) for exact counts.
8. Flag uncertainty instead of inventing facts. If metrics, dates, or award-specific rules are missing, keep placeholders or ask for targeted clarification only when it materially affects the requested output.

## Drafting Rules

- Lead with achievements, not biography.
- Prefer quantified impact over adjectives.
- Keep claims proportional and believable.
- Preserve official names, units, dates, and capitalization exactly as provided.
- Avoid unsupported superlatives unless the user supplies evidence.
- Avoid making decorations sound automatic; the citation should show why the performance clearly exceeded normal duty expectations.
- Keep all claimed actions supportable by the facts provided. Do not introduce stratification statements, invented endorsements, or unsupported comparisons.
- For citations, do not use unauthorized abbreviations or acronyms, and do not include classified information.
- Do not force decoration narrative into `1206` structure, and do not force `1206` language into performance reports.
- Treat character limits as hard constraints when the format requires them. Count the entire string, including letters, numbers, whitespace, punctuation, symbols, and special characters.
- When the member served in a joint organization, default to checking whether a Department of War joint award is the proper recognition before drafting a DAF decoration.
- Default to spelling terms out. Use acronyms only when they are broadly understood and authorized by the governing acronym guidance.
- Treat current guidance, templates, and accepted practices as controlling for live format behavior when they conflict with older policy references. Use the policy references as the baseline and ask for clarification only when the conflict materially changes the output and cannot be resolved from the provided guidance.

## Working Style

- If the user provides rough notes, first normalize them into a fact list grouped by accomplishment.
- If the user provides a finished draft, edit for sharper impact, cleaner syntax, and better board or reviewer readability without changing the underlying facts.
- If the user does not name the document type, infer whether the request is for a performance report, an award package (`1206`), or a decoration and say what assumption was made.
- Default to helping with the exact piece the user asks for rather than building the whole document.
- Ask only for the additional facts needed for that piece.
- Expect the user to iterate with feedback and clarification between steps.
- When working through a multi-step task, use the approved example data actively at each step to show what right looks like.
- For example-driven help, provide short concrete examples during splitting, consolidation, ranking, and drafting rather than treating the example files as passive background only.
- For performance reports, treat `EPB` and `OPB` as interchangeable terms within this skill unless the user later introduces a meaningful distinction.
- For performance reports, preserve the sectioned evaluation structure and check for mandatory comments such as fitness language before finalizing.
- For performance reports, treat the Duty Description as a required `450` character paragraph when the user asks for Duty Description help or when drafting a full report. It should summarize the key responsibilities reflected in the ALQs, including additional duties when they materially belong in the report.
- For performance-report requests, help determine the best ALQ category from the provided achievements when that is what the user is asking, then provide variations for one statement at a time.
- For statement-format `AF Form 1206`, provide a single statement unless the user explicitly asks for multiple options.
- For paragraph-format `AF Form 1206` and for decorations, provide the full paragraph or full citation body the user asked for.
- For decorations, keep review references stable by using the first-column split numbers in the split-review table, merge IDs like `M1`, and rank numbers in the ranking table; do not invent any other numbering scheme during review.
- For decorations, default to asking for the full EPB or OPB statement set covering the medal period; use rough accomplishment bullets only as fallback when those statements are unavailable.
- For decorations, ask for that EPB or OPB content in categorized form by report year and ALQ section, such as `EPB23` or `EPB 2023`, then `E`, `L`, `M`, `I`, `H`.
- For decorations, the default first response should be a short request to paste the year-tagged EPB or OPB sections in the exact `EPB23` or `EPB 2023` plus `E`, `L`, `M`, `I`, `H` format; do not expand the ALQ letters into prose labels.
- For decorations, do not ask the user to pre-rank the strongest accomplishments or choose between citation and justification; default to citation drafting and do the split, consolidation, and ranking work inside the skill.
- For decorations, if the user already identified the medal family, do not ask them to restate the exact medal label unless they later indicate a different service or a different medal family.
- For decorations, if EPB or OPB source is unavailable, use a narrow fallback ask for accomplishment statements with metrics and scope only; do not fall back to asking for rank, name, duty title, unit, base, or dates.
- For decorations, do not offer a starter citation shell, direct draft, or accomplishment-order recommendation before the user provides source material and completes the split and ranking reviews.
- For decorations, follow this mandatory citation workflow:
  - request the necessary categorized EPB or OPB statements first
  - split those statements into numbered accomplishment splits and show any proposed consolidations or merges
  - stop for user feedback before ranking
  - then rank the approved consolidated and unconsolidated accomplishments together and show that ranking for review
  - stop for user feedback on final selection and order before drafting the citation
  - only build the citation after both review gates are complete, unless the user explicitly tells you to skip them
- For decorations, treat the split table as a mechanical review artifact, not as the merge-candidate definition of the work.
- For decorations, consolidation means combining distinct source accomplishments that are explicitly part of the same broader contribution; it never means restoring the 2 required split rows from the same original EPB entry back into 1 row.
- For decorations, do not propose a merge based only on broad theme overlap such as training, readiness, production, leadership, volunteerism, or impact; require explicit source linkage.
- For decorations, before proposing any merge, apply this proof test: the merged accomplishment must still read as one coherent broader contribution without adding connective assumptions that are not already supported by the source text.
- For decorations, if explicit linkage is not clear from the source text, default to no merge.
- For decorations, the split-review step must use the exact split-review table from `decoration-splitting.md`; do not replace it with prose lists, alternate headers, likely-cut notes, or ranking commentary.
- For decorations, if the split count math or split-review format is wrong, loop back and rebuild the split stage before showing it to the user.
- For decorations, use the Python split helper once per source statement for raw sentence-based splits, then manually review any returned 4-sentence split for a possible `3+1` override and resolve flagged edge cases and opener repairs before building the split-review table.
- For decorations, do not treat the raw split table as a completed review step; after splitting, the agent must still check for valid consolidation candidates and fill the `Proposed Merges` section before showing split review.
- For decorations, do not ask for award period, role, unit, rank, name, or other intro metadata unless the user explicitly wants help filling the intro line.
- If the task looks compliance-sensitive or template-sensitive, ask for the template only when the missing format would materially change the output.

## Resources

- Read [DEPENDENCIES.md](DEPENDENCIES.md) when setting up the skill on a new machine or sharing it through GitHub.
- Read [references/DAFPD 36-28.md](references/DAFPD%2036-28.md) for top-level policy scope, purpose, and authority before applying lower-level procedural guidance.
- Start with [references/AFH 33-337/quick-map.md](references/AFH%2033-337/quick-map.md) to route the question to the right handbook chapter. Search [references/AFH 33-337/index.md](references/AFH%2033-337/index.md) with [scripts/search_tongue_and_quill.py](scripts/search_tongue_and_quill.py) only when the quick map is not enough.
- Read [references/DAFI 36-2803.md](references/DAFI%2036-2803.md) for program governance, approval-authority logic, duplicate-recognition constraints, acronym minimization, and other-recognition alternatives when a decoration is not appropriate.
- Read [references/DAFMAN 36-2806.md](references/DAFMAN%2036-2806.md) for personal military decoration criteria, recommendation mechanics, citation limits, acronym restrictions, and retirement wording rules.
- Read [references/decoration-guidance.md](references/decoration-guidance.md) for the master decoration workflow and stage map.
- Read [references/decoration-intake.md](references/decoration-intake.md) for the exact first-response intake for decoration work.
- Read [references/decoration-splitting.md](references/decoration-splitting.md) for split logic and the split-review template.
- Read [references/decoration-consolidation.md](references/decoration-consolidation.md) for merge logic and merge-review expectations.
- Read [references/decoration-ranking.md](references/decoration-ranking.md) before choosing which accomplishments to carry into a decoration citation body. Use it for ranking-specific logic, scoring, and the ranking-review template after split and merge review are complete.
- Read [references/decoration-drafting.md](references/decoration-drafting.md) for citation drafting order, line logic, and final validation after the user approves the final ranked order.
- Read [references/decoration-examples.md](references/decoration-examples.md) for preserved achievement and commendation example citations.
- Read [references/AFI 36-2406.md](references/AFI%2036-2406.md) for officer and enlisted performance-brief structure, section-specific writing rules, mandatory fitness comments, stratification limits, and future-role guardrails.
- Read [references/shared-guidance.md](references/shared-guidance.md) for shared mechanics across the performance-brief lane and `AF Form 1206`.
- Read [references/shared-validation.md](references/shared-validation.md) for the required validation order, troubleshooting flow, impactfulness checklist, clarity checklist, and conflict-resolution priority during statement iteration.
- Read [references/performance-brief-guidance.md](references/performance-brief-guidance.md) for performance-report statement behavior, ALQ routing, and hard limits.
- Read [references/performance-brief-examples.md](references/performance-brief-examples.md) for ALQ-fit examples and one-statement-at-a-time performance-report patterns.
- Read [references/award-guidance.md](references/award-guidance.md) for award-package limits, review workflow, and preserved examples.
- Read [references/Acronyms.md](references/Acronyms.md) before finalizing performance reports, awards, or decorations that may contain acronyms.
- Read [references/intake-checklist.md](references/intake-checklist.md) when you need to route intake to the correct lane-specific intake file.
- Read [references/performance-brief-intake.md](references/performance-brief-intake.md) for performance-brief intake.
- Read [references/award-intake.md](references/award-intake.md) for award-package intake.
- Use [scripts/count_text.py](scripts/count_text.py) when exact length compliance matters.
- Use [scripts/build_decoration_splits.py](scripts/build_decoration_splits.py) once per source statement to generate deterministic decoration splits before manually handling edge cases and building the split-review table.
- Use [scripts/check_spelling_grammar.py](scripts/check_spelling_grammar.py) to flag likely spelling and grammar issues before final delivery.
- Use [scripts/search_tongue_and_quill.py](scripts/search_tongue_and_quill.py) to locate handbook guidance on grammar, punctuation, tone, structure, bullets, memorandums, abbreviations, capitalization, and numbers.
- Use [scripts/validate_acronyms.py](scripts/validate_acronyms.py) to flag acronym-like tokens that may violate the approved guidance.
- Read [references/writing-patterns.md](references/writing-patterns.md) when converting plain-English notes into award language.
- Read [references/output-formats.md](references/output-formats.md) when choosing structure, section order, or line allocation.
- Reuse [assets/performance-brief-template.md](assets/performance-brief-template.md), [assets/award-template.md](assets/award-template.md), and [assets/decoration-template.md](assets/decoration-template.md) as starting documents when the user needs a fill-in template.
