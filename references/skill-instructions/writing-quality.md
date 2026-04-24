# Writing Quality Pass — Skill Instruction File
# Version: 1.0.0 | Nativized from Phase 5 of job-application-engine
# This file documents the inline Writing Quality module embedded in SKILL.md.
# Read when extending or adapting Phase 5 for a new use case.

---
## Purpose

The Writing Quality Pass removes AI-generated writing patterns from all
application output before it reaches the user. Two passes run internally.
Only the final version is presented — never the draft.

## What It Replaces

This module nativizes the logic of the humanizer skill (25-pattern audit).
It operates without that external skill file. All 25 pattern categories are
embedded here across five families.

## Execution

Pass 1: scan for and remove all instances of the five pattern families below.

Pass 2: ask internally — "What still makes this obviously AI-generated?" List
remaining tells. Resolve each. Vary sentence length and rhythm. Add specificity
where vague claims remain. Match the writing voice to the candidate's level:
direct and delivery-focused for mid-level; strategic and systems-oriented for
senior and executive levels.

## The 25 Pattern Categories (5 Families)

Family 1 — Significance Inflation (10 categories)
These patterns inflate the importance of events, roles, or achievements
beyond what the evidence supports. Remove all of them.
"stands as" | "serves as" | "is a testament to" | "marks a pivotal moment" |
"underscores" | "highlights its importance" | "reflects broader" |
"evolving landscape" | "indelible mark" | "setting the stage for" |
"key turning point" | "shaping the future of" | "deeply rooted" |
"contributing to the"

Family 2 — Promotional Language (8 categories)
These patterns make application text read like marketing copy rather than
professional communication. Remove all of them.
"boasts" | "vibrant" | "groundbreaking" | "renowned" | "breathtaking" |
"nestled" | "in the heart of" | "showcasing" | "exemplifies" |
"commitment to excellence" | "rich experience" | "stunning" |
"dynamic" (used vaguely without a specific referent)

Family 3 — Structural AI Patterns (5 categories)
These patterns reveal the underlying generation method through syntactic
structure rather than word choice.
Rule of three: three-item lists used for rhetorical effect rather than
genuine enumeration. Rewrite as prose or reduce to the two strongest items.
Em dash overuse: more than one em dash per paragraph used for stylistic
effect rather than grammatical purpose. Replace excess instances with
commas, colons, or sentence breaks.
Negative parallelism: "not just X, but Y." Rewrite as a direct claim.
Synonym cycling: three different words used in sequence to express the same
concept. Remove the cycle and state the concept once.
False ranges: "from X to Y, from A to B." Rewrite as a single clear claim
with the most important data point foregrounded.

Family 4 — Voice and Attribution Patterns (7 categories)
These patterns either avoid a direct voice or attribute claims to unnamed
authorities that cannot be verified.
Vague attributions: "experts argue", "industry reports suggest", "observers
have noted." Replace with a named source or remove entirely.
Copula avoidance: "serves as" or "functions as" instead of "is" or "works
as." Use the simpler form.
Superficial -ing phrases: present participle clauses tacked onto sentence
endings to add false depth — "contributing to...", "highlighting...",
"reflecting...". Remove or rewrite as a separate declarative sentence.
Chatbot artifacts: "Great question!", "I hope this helps!", "Let me know
if you need anything else." Remove entirely.
Excessive hedging: "could potentially possibly", "might arguably be",
"may have some effect." Choose one qualifier or remove all of them.
Knowledge cutoff hedging: "based on available information", "to the best of
my knowledge." Remove entirely from application output.
Pronoun overuse: "I" beginning more than 40% of sentences in any paragraph.
Restructure affected paragraphs to vary the sentence subject.

Family 5 — Technical AI Tells (5 categories)
These patterns are detectable through statistical regularity — the uniformity
that human writers naturally vary but LLMs apply consistently.
Hyphenated word pair overuse: "cross-functional", "data-driven", "end-to-end",
"client-facing" used with perfect consistency throughout. Humans hyphenate
these inconsistently — match that natural variation.
Filler openers: "In order to", "It is important to note that", "At its core",
"First and foremost." Cut these and begin with the substantive claim.
Generic positive conclusions: "The future looks bright", "exciting times
ahead", "a major step in the right direction." Cut entirely or replace with
a specific fact.
Over-formatted output: excessive bold text, bullet points, or headers in
contexts where prose would communicate more naturally and professionally.
Passive voice in evidence sections: "the project was delivered" instead of
"Alex delivered the project." Use active voice in all evidence paragraphs.

## Example Before and After

Before (Family 1 + 3 + 5):
"At DataFlow GmbH, the team serves as a testament to the power of cross-
functional collaboration, highlighting the importance of data-driven decision-
making and setting the stage for end-to-end product ownership."

After:
"At DataFlow GmbH, I led a cross-functional team that reduced churn by 18%
in six months through a friction-audit-led onboarding redesign."

## Quality Criteria for the Final Version

The output sounds natural when read aloud. Sentence lengths vary across the
piece — some short, some longer. Specific details replace vague claims.
The writing voice matches the candidate's seniority level and sector.
No sentence from Pass 1 pattern families remains. No chatbot artifacts.
No passive voice in evidence paragraphs.
