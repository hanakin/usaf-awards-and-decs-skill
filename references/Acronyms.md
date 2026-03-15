# Acronym Guidance

Use this reference to control acronym and abbreviation usage across performance reports, awards (`AF Form 1206`), and decorations.

Source reviewed: user-provided `Air Force Acronym & Abbreviation List`, dated `17 February 2026`.

## Core rule

- Default to spelling terms out.
- Performance statements should use plain language.
- Only use acronyms and abbreviations that are approved or clearly authorized by category.

## Guidance principles

- Performance statements should be standalone sentences with action plus impact and/or result.
- Readability matters more than functional familiarity.
- Inclusion on the approved list reflects broad understanding, not mere frequency of use.
- Even when an acronym is approved, that does not mean it must be used.

## Approved categories

The source says the following categories are generally acceptable when approved by category:

- Common ranks and tiers across services
- Common office symbols
- Common organizations at squadron level and above
- Common weapons and platforms
- Common symbols and measurements

Examples the skill should treat as category-approved additions:

- Unit shorthand such as `Sq`, `Flt`, `Gp`, and `Wg`
- Common enlisted and officer rank abbreviations such as `Amn`, `A1C`, `SrA`, `SSgt`, `TSgt`, `MSgt`, `SMSgt`, `CMSgt`, `2Lt`, `1Lt`, `Capt`, `Maj`, `Lt Col`, `Col`, and `Gen`
- Common office symbols and major organization shorthand such as `CC`, `CMSAF`, and `STRATCOM`
- Position abbreviations such as `NCOIC` and `OIC`
- Legacy and current department terms such as `SecDef`, `SecWar`, `DoD`, and `DoW`
- Organization abbreviations such as `ACC`, `CCMD`, `COCOM`, `USCYBERCOM`, `AF`, `IG`, `TF`, `CNMF`, `HAF`, and `CSS`
- Job-function and AFSC-style codes such as `1N8`

## Source of truth

- The full extracted list with definitions is stored in [data/approved_acronyms.tsv](../data/approved_acronyms.tsv).
- The validator allowlist is stored in [data/approved_acronyms.txt](../data/approved_acronyms.txt).

## Validator workflow

- Use [scripts/validate_acronyms.py](../scripts/validate_acronyms.py) to scan draft text.
- The validator uses the allowlist in [data/approved_acronyms.txt](../data/approved_acronyms.txt) plus category-based exceptions and normalization cases for common shorthand.
- Treat validator output as a review queue, not blind truth. Some office symbols, ranks, or platform names may still require human judgment.
- The validator also permits category-based shorthand for common ranks, office symbols, and unit labels that are broadly accepted under this guidance.

## Practical writing rule

- If an acronym is not obviously necessary for clarity or space, spell it out.
- If space is tight and the acronym is both approved and broadly readable, it may remain.
