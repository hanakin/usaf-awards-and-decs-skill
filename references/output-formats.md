# Output Formats

Use the format the user or unit requires. If none is provided, choose the nearest fit and state the assumption.

## Performance report

Use for evaluation-style writing that captures sustained performance over a reporting period.

Recommended structure:

- Duty context only as needed to frame the accomplishment
- Strong performance statements placed in the required evaluation sections rather than merged into one narrative
- Evidence of leadership, followership, improvement, and readiness as relevant to the report format
- Tight language that reads like evaluation content, not like a citation
- Mandatory comments handled separately when required, especially fitness language

Focus on sustained contribution, scope, and effect across the reporting period.

Policy anchors:

- `AFI 36-2406` for section structure, mandatory comments, stratification, and future-role rules
- `AFH 33-337` chapters 7, 8, 19, 26, 27, and 28 for writing style and mechanics
- `statement-shared.md` for common statement mechanics
- `epb-guidance.md` for performance-report statement rules

Workflow notes:

- When the user wants statement options, generate multiple materially different phrasings rather than minor verb swaps.
- Keep the member name near the front of the statement when the format expects named statements.
- Treat `EPB` and `OPB` as interchangeable terms in this skill.
- Apply the current performance-report statement limits even if the user does not restate them.

Performance-report length rule:

- Use `350` characters for `E`, `L`, `M`, and `I`
- Use `250` characters for `H`
- Use exact counting when the user is drafting statement text to fit those blocks

## Medal citation

Use for achievement, commendation, meritorious service decorations for recognition when the user asks for citation language.

Recommended structure:

- Award-specific opening sentence
- Brief narrative description covering the strongest supportable accomplishments
- Award-specific closing sentence

Keep the tone formal and citation-ready. Favor polished narrative over board-style shorthand.

Policy anchors:

- `DAFMAN 36-2806` Attachment 5 for citation structure, opening sentences, closing sentences, fonts, and limits
- `DAFI 36-2803` for appropriateness, duplicate recognition, and governance
- `AFH 33-337` for sentence clarity, punctuation, capitalization, abbreviations, and numbers
- `decoration-guidance.md` for integrated decoration drafting and validation behavior
- `ascom-guidance.md` for Air Force Commendation Medal (`AFCM`) handling in this skill's current medal set

Critical rules:

- Do not invent a generic citation formula across all decorations
- Do not use unsupported stratification or promotion-style language
- Check award-specific limits before finalizing
- Use placeholders instead of fabricating missing required facts
- Run spelling and grammar review before final delivery
- Spell terms out in decoration prose; do not rely on abbreviations or acronyms

## AF Form 1206 style content

This is the default meaning of `awards` in this skill unless the user clearly means a medal or decoration.

Use when the package needs either statement-style or paragraph-style award justification.

Default to statement format unless the user or template explicitly requires paragraph format.

Recommended structure:

- Statement format:
  - strongest accomplishment first
  - remaining accomplishments ordered by mission impact
  - each statement handled as its own constrained unit
  - total number of statements varies by award or template
- Paragraph format:
  - one or more narrative blocks sized to the required line count
  - strongest accomplishment still leads
  - remaining content ordered by mission impact
  - total allowed lines vary by award or template

Treat line count and character count as hard constraints.

Policy anchors:

- `AFH 33-337` chapter 19 for bullet construction and polish
- `Acronyms.md` and validator rules for abbreviation control
- `statement-shared.md` for common statement construction rules
- `1206-guidance.md` for `AF Form 1206`-specific hard limits, review flow, and examples
- Unit template or scoring model when provided

Current length rule:

- Apply the `195-220` character requirement only for `AF Form 1206` individual statement work
- Apply the required statement count for the specific award or template when using statement format
- Apply the required line-count limit for `AF Form 1206` paragraph-format work

## Quarterly or annual nomination

Use when the package is competitive and board-read.

Recommended structure:

- Job performance and mission execution
- Leadership or followership
- Improvement initiatives
- Community involvement only if part of the scoring model

Select accomplishments that compare well against peers. One major result usually beats several minor activities.

## Leadership summary

Use when a supervisor needs a short paragraph, cover note, or talking points.

Recommended structure:

- One-sentence overall thesis
- Three strongest accomplishments
- One sentence on why the member stands out for the award

## Format guardrails

- Do not force performance report language into citation style
- Do not force bullet style into citation style
- Do not force citation prose into `AF Form 1206` blocks
- Do not use decoration-level wording when the facts support only lower recognition
- Do not let community service crowd out mission impact unless the award criteria requires it
- If the unit uses a house format, mirror it exactly

## Length handling

- Treat character and line limits as hard constraints.
- When a format uses a character count, count the complete string.
- Include all letters, numbers, whitespace, punctuation, symbols, and special characters in the count.
- Do not estimate by word count or editor display width.
- Use `python3 scripts/count_text.py` from the skill directory when exact counts matter.

## Acronym handling

- Default to spelling terms out, especially in performance statements.
- Use only approved or clearly authorized acronyms.
- When in doubt, spell it out.
- Use `python3 scripts/validate_acronyms.py` from the skill directory to flag suspicious acronym usage before final delivery.
