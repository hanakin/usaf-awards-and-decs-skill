# Decoration Splitting

Use this file for the split-review stage of decoration work.

## Split workflow

Apply splitting in this order.

### 1. Identify the ALQ type

- `E`, `L`, `M`, and `I` may split
- `H` does not split

### 2. Hard stop for `H`

- `H` always stays whole as 1 accomplishment with no splitting
- Do not count sentences for `H`
- Do not apply edge-case rules to `H`
- If an `H` entry is shown as more than 1 split item, treat that as invalid output and correct it before proceeding

### 3. Check for the single-sentence run-on exception

- Use this check before sentence counting
- If the source uses a single run-on sentence but clearly contains two accomplishments, normalize it into 2 sentence-level split items before review
- Do not use this rule for entries that already contain 2 or 4 sentences
- Use meaning, not trigger words, to identify the break
- If the downstream effect is grammatically attached to the first clause but functionally describes a separate accomplishment or result, still split it
- Keep the first accomplishment together in split `1`
- Move the second distinct accomplishment, result, recognition, or follow-on effect into split `2`

### 4. Apply the normal sentence-count rule

- If the entry contains 2 sentences, split sentence `1` into split `1` and sentence `2` into split `2`
- If the entry contains 4 sentences, split sentences `1+2` into split `1` and sentences `3+4` into split `2`

### 5. Check for the 4-sentence edge case

- If a 4-sentence entry clearly reads as one sustained accomplishment across sentences `1+2+3`, and sentence `4` is a separate result, recognition, or follow-on effect, split it as sentences `1+2+3` into split `1` and sentence `4` into split `2`
- Use this edge case only when the normal `1+2` and `3+4` split would break the meaning

### 6. Preserve wording during split review

- Preserve the source wording as much as possible
- Do not rewrite split review text into citation prose
- Preserve source numbers, acronyms, abbreviations, and shorthand
- Only make the minimum wording change needed for a split to stand alone, such as changing the opening of a second split to `He`, `She`, or the member's name
- Do not use weak opener repairs like `This`, `That`, or `These` for a second split
- Strip transition-only intros like `Also` and `Additionally`

### 7. Reject invalid split behavior

- Never split at the clause, phrase, semicolon, or metric level
- Never split one sentence into multiple mini-actions, except for the approved run-on edge case above
- Never split a 4-sentence accomplishment into more than 2 split items

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
