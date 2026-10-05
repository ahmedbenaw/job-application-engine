# Country Profiles (GAP-07, Q-03, Q-16)
# job-application-engine v2.2.0 (generic)
# Read when: Phase 3 (choosing the profile for the application), Phase 3B (writing to the profile), Phase 3C (GATE-11 checks)

Every application uses exactly one profile. Pick the profile for the country the job is in. Use **General International** for any country without its own profile. More profiles are added on demand, using the same fields.

**Status:** these profiles follow widely used conventions. GAP-07 requires each one to be checked against current local sources before release. Until a row is marked *Checked*, treat it as the default and let the person override any field.

**Fixed rules for every profile (the spec wins, INQ-06):**
- Single column, no tables, text boxes or images, contact details in the body (GAP-02). Local styles that use tables, such as a tabular German CV, are written as plain single-column text.
- Photo and personal details are printed only when the profile allows them **and** the person agrees (INQ-07, privacy class *Ask*).
- Government ID numbers are never printed or collected.

| Field | US | UK | Germany | Netherlands | UAE / GCC | Saudi Arabia | General International |
|---|---|---|---|---|---|---|---|
| Document name | Resume | CV | Lebenslauf / CV | CV | CV | CV | CV |
| Length | 1 page under 10 years, 2 max | 2 pages | 1–2 pages | 1–2 pages | 2 pages | 2 pages | 2 pages max |
| Photo | Never | Never | Allowed (Ask) | Allowed, uncommon (Ask) | Allowed (Ask) | Allowed (Ask) | Never |
| Date of birth | Never | Never | Allowed (Ask) | Never | Allowed (Ask) | Allowed (Ask) | Never |
| Nationality | Never | Never, use a right-to-work line if relevant | Optional (Ask) | Never, use a right-to-work line if relevant | Allowed (Ask) | Allowed (Ask) | Never |
| Marital status | Never | Never | Never | Never | Allowed (Ask) | Allowed (Ask) | Never |
| Work permit / visa line (GAP-04) | If relevant | If relevant | If relevant | If relevant | Common: visa or residency status | Common: residency status | If relevant |
| Language of the CV | US English | UK English | German or English, as in the ad | English or Dutch, as in the ad | English | English or Arabic, as in the ad | Language of the ad |
| Page size | Letter | A4 | A4 | A4 | A4 | A4 | A4 |
| Date format (REQ-25) | Mon YYYY | Mon YYYY | MM/YYYY | Mon YYYY | Mon YYYY | Mon YYYY | Mon YYYY |
| Phone format | +1 | +44 | +49 | +31 | +971 / country code | +966 | International (+ country code) |
| First-job section order (Q-16) | Education first | Education first | Education first | Education first | Education first | Education first | Education first |
| Everyone else | Experience first | Experience first | Experience first | Experience first | Experience first | Experience first | Experience first |
| Signature or date line | No | No | Optional | No | No | No | No |
| Default file type (Q-01) | DOCX main, PDF too if 2 files allowed | Same | Same | Same | Same | Same | Same |
| Status | Default | Default | Default | Default | Default | Default | Default |

## Adding a profile

1. Copy the General International column.
2. Change only the fields that differ, each with a source and date.
3. Mark it *Checked* once a person has confirmed it against current local sources.
4. Add a line to the spec's Change log and to CHANGELOG.md.
