# Decoration Splitting

Use this file for the split-review stage of decoration work.

Use `python3 scripts/run_decoration_split_workflow.py` as the default split-stage helper. It should build the non-edge-case split rows first, then validate the split-review table before it is shown.
The agent must still manually resolve flagged edge cases, repair second-split openings when needed, and rerun validation before showing the final split review.

## Split workflow

Apply splitting in this order.

### 1. Identify the ALQ type

- `E`, `L`, `M`, and `I` may split
- `H` does not split
- For non-edge-case source entries, use the split helper script first instead of doing the split by hand

### 2. Hard stop for `H`

- `H` always stays whole as 1 accomplishment with no splitting
- Do not count sentences for `H`
- Do not apply edge-case rules to `H`
- If an `H` entry is shown as more than 1 split item, treat that as invalid output and correct it before proceeding
- In the split-review table, one `H` source entry may appear only once
- If one `H` source entry shows up as two numbered rows, that output is invalid and must be rebuilt

### 3. Check for the single-sentence run-on exception

- This is an edge case that the split helper should flag for manual review
- Use this check before sentence counting
- If the source uses a single run-on sentence but clearly contains two accomplishments, normalize it into 2 sentence-level split items before review
- Do not use this rule for entries that already contain 2 or 4 sentences
- Use meaning, not trigger words, to identify the break
- If the downstream effect is grammatically attached to the first clause but functionally describes a separate accomplishment or result, still split it
- Keep the first accomplishment together in split `1`
- Move the second distinct accomplishment, result, recognition, or follow-on effect into split `2`
- After resolving this edge case manually, confirm that the source entry still produces exactly `2` split rows

### 4. Apply the normal sentence-count rule

- If the entry contains 2 sentences, split sentence `1` into split `1` and sentence `2` into split `2`
- If the entry contains 4 sentences, split sentences `1+2` into split `1` and sentences `3+4` into split `2`

### 5. Check for the 4-sentence edge case

- This is an edge case that may require manual review after the helper produces the default split
- If a 4-sentence entry clearly reads as one sustained accomplishment across sentences `1+2+3`, and sentence `4` starts a separate accomplishment, result, recognition, or follow-on effect, split it as sentences `1+2+3` into split `1` and sentence `4` into split `2`
- Use this edge case only when the normal `1+2` and `3+4` split would break the meaning
- This includes cases where sentences `1+2+3` stay together as one volunteer, mission, modernization, or development accomplishment, and sentence `4` introduces a different standalone accomplishment
- After resolving this edge case manually, confirm that the source entry still produces exactly `2` split rows

### 6. Preserve wording during split review

- Preserve the source wording as much as possible
- Do not rewrite split review text into citation prose
- Preserve source numbers, acronyms, abbreviations, and shorthand
- Only make the minimum wording change needed for a split to stand alone, such as changing the opening of a second split to `He`, `She`, or the member's name
- Do not use weak opener repairs like `This`, `That`, or `These` for a second split
- Strip transition-only intros like `Also` and `Additionally`
- The agent is responsible for these opener repairs when resolving flagged edge cases

### 7. Reject invalid split behavior

- Never split at the clause, phrase, semicolon, or metric level
- Never split one sentence into multiple mini-actions, except for the approved run-on edge case above
- Never split a 4-sentence accomplishment into more than 2 split items
- Never show one `H` source entry as more than one numbered split row

### 8. Validate the split count before review

- Check the final split-review table against the source-entry count before presenting it
- Use this equation:
  - expected split rows per EPB = (`E` x `2`) + (`L` x `2`) + (`M` x `2`) + (`I` x `2`) + (`H` x `1`)
  - total expected split rows = the sum of the expected split rows for every EPB included in the medal period
- For the standard intake format used by this skill, one complete EPB with `E`, `L`, `M`, `I`, and `H` should always produce `9` split rows
- If the medal period covers `3` complete EPBs, the split-review table should therefore contain `27` split rows
- This is a fixed-count check:
  - every `E`, `L`, `M`, and `I` source entry should produce `2` split rows
  - every `H` source entry should produce `1` split row
- The normal split rule, 4-sentence edge case, and single-sentence run-on rule only change how the `2` rows are formed for `E`, `L`, `M`, and `I`
- They do not change the expected row count
- If the split-review table row count does not match this equation, the split output is invalid and must be corrected before review
- If any `E`, `L`, `M`, or `I` source entry produces anything other than `2` split rows, the split output is invalid
- If any `H` source entry produces anything other than `1` split row, the split output is invalid
- If the total split-table math fails, stop and loop back to the split step before showing the table
- If any individual source entry fails its required count, stop and loop back to re-split that entry before showing the table
- Do not proceed to merge review until both the total count check and the per-entry count checks pass
- This applies to manually resolved edge cases too; they are not exempt from the `2`-row requirement for `E`, `L`, `M`, and `I`

### 9. Validate the review-stage format before review

- The split stage must use the exact split-review display template in this file
- Do not replace the required table with a prose list, numbered outline, alternate table headers, or freeform commentary
- The split-review table must use these exact columns:
  - `Split #`
  - `EPB Ref`
  - `Merged ID`
  - `Split`
- `EPB Ref` must use the compact format like `E23`, `L24`, or `H25`
- Do not rewrite that source reference into alternate forms like `EPB23 E` or `2023 M`
- The split stage may show only:
  - the split-review table
  - `Proposed Merges`
  - `Review Needed`
- Do not add ranking advice, likely cuts, citation-order recommendations, or keep/drop recommendations during split review
- If the output does not match this display format, stop and rebuild it before showing the review
- Run `python3 scripts/run_decoration_split_workflow.py` against the year-tagged EPB input as the default split-stage command
- If the workflow flags edge cases, manually resolve them in the table, rerun validation, and only then show the split review
- If the validator fails, loop back and rebuild or manually correct the split review before showing it

## Split review template

Use this exact display template:

Split Review

| Split # | EPB Ref | Merged ID | Split |
|---|---|---|---|
| 1 | E23 | M1 | [full split text] |
| 2 | E23 | M1 | [full split text] |
| 3 | L24 |  | [full split text] |
| 4 | I25 | M2 | [full split text] |

Proposed Merges

- `M1` [rewritten merged accomplishment]
- `M2` [rewritten merged accomplishment]

Review Needed
- Valid merges:
- Invalid merges:
- Missing merges:

For feedback on this table, the user should always reply using the first-column numbers, not the `EPB Ref` or `Merged ID` values.
