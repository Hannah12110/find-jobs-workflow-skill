# Interview Question Generation

## Purpose

Use this reference after a tailored resume has been generated and the user is preparing for likely screening or interview conversations.

The goal is to produce a realistic interviewer-style question set anchored to:
- the tailored resume
- the JD
- the likely company interview style

Core principle:

Do not generate generic interview questions by default. First try to identify how this company tends to ask questions for similar roles, then generate a focused question set that matches the user's actual materials.

Default delivery rule:

Write the interview-prep artifact to `job-search-data/interview-prep/` as `公司-岗位-面试备考稿.md` by default instead of expanding the full prep script in chat, unless the user explicitly asks for inline output.

## When to Run

Run this step after:
- a tailored resume is completed
- the user wants to prepare for likely interview questions
- or the workflow is trying to make the tailored output more action-ready

This step should usually happen after resume generation, not before.

## Required Inputs

Minimum inputs:
- company name
- role name
- JD
- tailored resume or tailored resume storyline

Helpful inputs:
- interview stage if known
- team / function details
- whether the role is more product, growth, operations, or mixed

## Company-Style Search Rule

Before generating questions, first search the web for:
- the target company
- similar role titles
- interview experiences / interview recaps / 面经 / question styles

Prioritize signals about:
- question style
- depth level
- whether the company prefers pressure questioning, resume deep dives, scenario questions, product sense questions, or business/data questions
- whether the role emphasizes execution, growth, user experience, or strategy

If company-specific interview experience cannot be found:
- explicitly fall back to a large-tech-company style
- use a balanced format with resume deep dive, product thinking, data sense, execution questions, and behavioral follow-ups

Do not pretend that company-specific style was found if it was not.

## Interview Length Rule

Default target length:
- 30 to 45 minutes

This usually means preparing:
- 8 to 12 primary questions
- selected follow-up questions under high-pressure items

Do not generate an overly long bank unless the user asks for more.

## Question Mix

A strong question set should usually include:

### 1. Resume Deep-Dive Questions
Questions that pressure-test:
- role ownership
- key decisions
- tradeoffs
- metrics
- what the user actually did

### 2. JD-Fit Questions
Questions that test:
- direct fit for responsibilities in the JD
- missing experience areas
- why this role fits the user's background

### 3. Company-Style Questions
Questions shaped by the likely company style found from search.

### 4. Scenario or Case Questions
Questions about:
- product optimization
- user experience issues
- growth ideas
- prioritization
- cross-functional collaboration

### 5. Behavioral and Reflection Questions
Questions on:
- conflict
- iteration
- failure
- changing direction
- incomplete information

## Generation Rules

- Anchor questions in the tailored resume, not in invented experience.
- Use the user's strongest projects first.
- Push on weak spots that the JD is likely to expose.
- Prefer realistic interviewer phrasing over textbook prompts.
- Include likely follow-up questions where pressure-testing is natural.
- If a company style is found, briefly state what style was inferred before listing questions.
- If falling back to big-tech style, state that explicitly.

## Suggested Output Structure

### A. Style Basis
- what company/role was searched
- whether company-specific style was found
- if found: short style summary
- if not found: explicit fallback to large-tech-company style

### B. Interview Plan
- target duration: 30 to 45 minutes
- question count
- emphasis areas

### C. Likely Questions
List the questions in likely interview order.

For selected questions, add:
- why the interviewer may ask this
- what part of the resume or JD it is testing
- likely follow-up questions

### D. Main Risk Areas
Call out:
- where the user is likely to get pressed
- which answers need stronger evidence
- which metrics or examples must be ready

## Common Mistakes

- generating generic questions without searching company style first
- claiming a company-specific style without evidence
- producing too many questions for a normal interview
- asking questions unrelated to the tailored resume
- avoiding the user's weak spots
- making the set so broad that it is not usable in practice

## Exit Criteria

This step is complete when it has produced:
- a clear company-style basis or fallback statement
- a 30 to 45 minute interview question set
- realistic ordering
- pressure points tied to the tailored resume and JD
- key risk areas the user should prepare for
- a saved Markdown prep file in the default interview-prep location unless the user requested another format
