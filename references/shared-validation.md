# Statement Validation And Iteration

Use this reference when generating, reviewing, and revising performance-report statements or `AF Form 1206` statements. This is the operational discipline that trains the model how to iterate, not just how to phrase.

## Core workflow

1. Start from the raw accomplishment details
2. Review for missing facts, metrics, and framing problems
3. Ask targeted clarifying questions only when the missing information materially affects strength or accuracy
4. Apply the lane-specific workflow:
   - performance reports: determine the best ALQ category first, then generate one statement at a time
   - `1206` statement format: generate a single statement unless the user asks for multiple options
   - `1206` paragraph format and decorations: this file's single-statement workflow does not control; use the lane-specific paragraph workflow
5. Run the validation sequence below and fix issues in order
6. Revise until the user approves

## Iteration handling

- There is no hard maximum number of iterations; continue until approval
- For performance reports, work one statement at a time after category selection
- For statement-format `1206`, default to one final statement unless the user asks for alternatives
- After 3 unsuccessful rounds, stop doing micro-edits and offer a reset path:
  - emphasize a different ALQ
  - rebuild from a different mission effect
  - rewrite from scratch
  - ask which dimension is still wrong: length, tone, clarity, or impact

## Validation order

Run checks in this order:

1. Character length
2. Word repetition
3. Acronym validation
4. Name presence and format
5. Spelling and grammar
6. Impactfulness
7. Clarity

Do not skip earlier checks and hope later edits will solve them.

## Impactfulness checklist

A statement passes impactfulness only when it:

- feels unique rather than generic
- uses varied, strong language instead of recycled phrasing
- uses impactful word choice instead of weak or overused verbs
- grabs attention and sells the accomplishment credibly
- leaves the reader with an immediate positive impression
- preserves clarity while staying persuasive

For performance reports, judge impactfulness against the approved example set for the target ALQ. Do not reject approved push-statement style in `H` merely because it is more promotive or emphatic than the other sections.

## Clarity checklist

A statement passes clarity only when it:

- uses well-formed sentence structure
- reads cleanly on first pass
- communicates a clear, unambiguous meaning
- has no grammatical or flow problems
- uses words appropriately for the audience and context

For `H`, clarity means the push is direct and understandable. It does not need to mirror the tone or sentence balance of `E`, `L`, `M`, or `I`.

## Conflict-resolution priority

If a statement cannot satisfy every goal at once, resolve conflicts in this order:

1. Name presence and approved format
2. Required character limit
3. Acronym compliance
4. Word-repetition cleanup
5. Spelling and grammar
6. Clarity
7. Impactfulness

That means clarity outranks flash, and compliance outranks stylistic preference.

## Tradeoff guidance

- If length conflicts with impact, meet the length requirement first and then maximize impact inside the limit
- If clarity conflicts with impact, choose clarity
- If metrics conflict with length, keep the most decisive metrics and ask for shorter alternatives if needed
- If verb variety conflicts with the hard limit, keep enough variation to avoid repetition but do not break compliance
- If generic validation logic conflicts with an approved example pattern for the same lane, follow the approved example pattern

## Troubleshooting

### Statement is too long

- Replace long approved phrases with approved acronyms
- Find shorter synonyms that preserve meaning and tone
- Remove redundant setup language
- Condense number formatting
- Prioritize the most important action and effect

### Statement is too short

- Add more specific metrics
- Add more concrete impact detail
- Expand the action with relevant scope
- Ask the user for more mission-effect detail if needed

### Acronym not approved

- Check the approved list
- Spell the term out if it is not approved
- Ask for a different authorized short form only if the output cannot fit otherwise

### Name format fails

- Convert the name to one of the approved patterns
- Confirm the rank abbreviation is approved
- Check capitalization and placement near the front

### Word repetition persists

- Replace repeated terms with better synonyms
- Reorder the sentence
- Swap structure instead of only swapping verbs

### Spelling or grammar fails

- Run `check_spelling_grammar.py`
- Fix misspellings before making style edits
- Correct doubled words, article usage, punctuation spacing, and other mechanical issues
- Re-run the check after every substantive rewrite because compression edits often introduce new mistakes

### Statement lacks impact

- Add exact metrics
- Sharpen the action verb
- Add the operational, resource, readiness, or people effect
- Make the consequence explicit
- For `H`, strengthen the push, readiness, or advocacy framing when that is what the category is supposed to convey

### Statement is unclear

- Simplify the structure
- Break overpacked phrasing into cleaner clauses
- Remove filler words
- Read it as if a board member sees it cold

### Missing metrics

- Ask for specific numbers once
- Use supported qualitative effect if no further numbers exist
- Never estimate

### User rejects multiple rounds

- After 3 iterations, offer a new angle instead of micro-edits
- Suggest emphasizing a different ALQ or different mission effect
- Offer a full rewrite from scratch
- Ask what specifically is still wrong: length, tone, clarity, or punch

## Output discipline

- Keep Python and validation steps internal
- Do not expose debug output, commands, or raw validator results unless the user explicitly asks
- Present review sets only after the full option batch is ready
- Match final output suffix rules only when the requested format requires them
- Use `check_spelling_grammar.py` before final delivery when the text is intended to be ready for use
- Treat approved examples as fact and authoritative style references when resolving tone and structure questions across performance reports, `AF Form 1206`, and decorations

## Review-phase output rules

- Present review options as a numbered list
- Each review option should include the statement and the character count
- Include the required prefix in the count
- Do not show raw validator output
- Do not show partial work; wait until the full set is ready
- Do not append quality-ranking suffixes during review unless the user or template explicitly requires them

## Final-output rules

- Present the final approved statement as a standalone final candidate
- Keep the required prefix if the format expects it
- Append the final character count when the format expects count display
- Append quality-ranking suffixes only when the requested format explicitly uses them
- Keep the final output ready to drop into the target product without extra explanation
