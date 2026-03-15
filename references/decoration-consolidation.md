# Decoration Consolidation

Use this file for the merge-review stage of decoration work.
The split table is not a final review product by itself. After splitting, always check the table for valid consolidation candidates before showing split review to the user.

## Consolidation rule

Consolidate only explicitly related accomplishments.
Consolidation merges distinct source accomplishments into 1 stronger broader contribution.
Consolidation never means recombining the 2 required split rows from the same original EPB entry.

Before testing merges, take a first pass at grouping the split pool.
Assign each split:

- a broad category
- a specific working bucket

Common broad categories include:

- mission
- exercise
- admin
- volunteer

Those are common anchors, not a closed list.
If a split clearly fits a different broad category, infer it from the source text.

The specific working bucket is also inferred from the source text.
It is not a fixed approved list.
Use it to surface likely merge candidates before applying the proof test.

Good consolidation candidates are:

- training-program development plus training integration plus analyst development
- targeting-tool modernization events tied to the same tool effort
- readiness and exercise efforts tied to the same readiness line
- senior-leader engagement efforts tied to the same explicit issue set

Consolidate only when the grouped items:

- reinforce the same broader contribution
- are explicitly related in content, not just loosely similar in theme
- can be rewritten into one stronger accomplishment statement without losing the core facts
- preserve the strongest metrics from the component items
- preserve the strongest counts, scale, roll-up math, dollars, hours, percentages, or supported population from the component items
- would still obviously read as 1 broader contribution to a reviewer who only saw the source text

Use this proof test before proposing a merge:

- first ask whether the items fall into the same broad category and specific working bucket
- ask whether the linkage is explicit in the source text or clearly inherent in the same sustained effort
- ask whether the source relationship supports a merge
- if the items came from the same original statement, treat that as a warning sign and usually do not merge them, but do not treat it as an absolute bar if the source still supports 1 broader contribution
- ask whether the merged line can be written without inventing connective reasoning such as "both support readiness" or "both involve production"
- ask whether the merged line preserves the strongest source math instead of dropping it, weakening it, or re-expanding a stronger rolled-up fact into weaker subcounts
- if either answer is no, do not merge

Category overlap helps surface candidates.
It does not prove the merge is valid by itself.

Do not consolidate items that are only thematically similar.
Do not consolidate items that would make the final citation sentence confusing or bloated.
Do not simply stack the original statements together and call that consolidation.
Do not merge items merely because they share a year, ALQ category, or repeated metric pattern.
Do not merge unrelated mission production and training items.
Do not merge unrelated readiness, volunteer, or leadership items unless the source makes them part of the same sustained effort.
Do not skip the merge check just because the split table already looks complete.

## How to consolidate

1. assign each split a broad category and a specific working bucket
2. look for likely candidates inside those buckets first
3. check whether the source relationship actually supports a merge
4. pull out the most important facts from each source accomplishment
5. keep the strongest metrics, scale, consequence, and rolled-up math
6. remove duplicate setup language
7. rewrite the material into one stronger accomplishment statement

## Review-stage wording rule

- Preserve source wording as much as possible during merge review
- Do not rewrite merge-review text into final citation prose
- Preserve source numbers, acronyms, abbreviations, and shorthand where possible

## Consolidation validation

Before accepting a merged accomplishment, verify:

- the rewritten accomplishment is stronger than either source item alone
- no source fact is double-counted
- no rolled-up source fact is re-expanded into weaker subcounts
- no strongest count, scale, roll-up, or other core math was omitted
- no critical qualifier was dropped
- no unrelated event was pulled in just because it sounded similar
- the final rewritten accomplishment still reads as one coherent accomplishment

## Invalid merge examples

- invalid: split `5` plus split `6` when those are simply the 2 required split rows from one original `M23` entry
- invalid: analytic production plus Tactical Combat Casualty Care instruction just because both are strong and citation space is limited
- invalid: 2 unrelated training items merged only because both improve readiness
- invalid: 2 unrelated intelligence products merged only because both involve reporting or production

## Worked example

Source accomplishments:

- Split `7` (`I23`): `TSgt Snuffy was by name requested to coordinate with DoD targeting tool team. His knowledge was integral to $41.5M upgrade to 25-yr old app. His feedback was lauded by DoD joint staff as "most detailed ever".`
- Split `16` (`I24`): `TSgt Snuffy participated in 2 DoD Joint Staff development initiatives to re-design the tool of record for targeting. His expertise and knowledge was lauded as best feedback they have ever received.`

Proposed merge:

- `M2`: `TSgt Snuffy supported 3 DoD targeting-tool modernization events, helped drive a $41.5M upgrade to a 25-yr old app, and delivered feedback lauded by joint staff as the strongest ever.`

Why this works:

- both source accomplishments are explicitly tied to the same targeting-tool modernization effort
- the merge preserves the strongest rolled-up scale and metric
- duplicate praise language is collapsed into one stronger result
- the rewritten text stays close to source wording instead of jumping straight to final citation prose
