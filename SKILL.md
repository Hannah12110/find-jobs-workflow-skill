---
name: find-jobs-workflow
description: Use for end-to-end job search workflow support: build a reusable background profile, analyze JDs, tailor resumes, identify gaps, track applications, and generate company-style interview prep materials.
---

# Find Jobs Workflow

## Overview

Use this skill to support the user's full job-search workflow, not just resume rewriting.

Always optimize for reuse, evidence quality, and realistic role fit. Do not invent experience, inflate unfinished work, or force the user into fixed target-role assumptions too early.

## When to Use

Use this skill when the user:
- provides a JD and wants resume tailoring
- wants to know whether a role is worth applying to
- needs help organizing their background into reusable materials
- is applying to many jobs and wants structured tracking
- wants to identify which skills, materials, or evidence they should add
- wants interview learnings to feed back into resumes and future applications

Do not use this skill for:
- general career advice with no job-search materials
- standalone interview prep when the workflow should instead hand off to [$interview-coaching-assistant](/Users/asus/.codex/skills/interview-coaching-assistant/SKILL.md)
- one-off copy edits when no job-search workflow support is needed

## Core Rules

- Background profiling comes before high-quality JD tailoring.
- Do not force the user to define fixed target roles too early.
- Do not only ask "what projects have you done".
- Probe for hidden experience from multiple angles.
- Treat unfinished work as candidate evidence until proven irrelevant.
- Separate base facts from narrative versions for internships with multiple responsibilities or role shifts.
- Project priority is dynamic and should change by JD.
- Every JD analysis must include recommendation, risk, project ranking, and gap diagnosis.
- Resume output must be paired with a "what is still missing" view.
- After generating a tailored resume, add a likely interviewer-question step.
- For interviewer-question generation, first search for company-specific interview style for similar roles; if unavailable, fall back to a large-tech-company style.
- Default interviewer-question sets should target a 30 to 45 minute interview.
- When producing interview-prep materials, write them to `job-search-data/interview-prep/` as a Markdown file named `公司-岗位-面试备考稿.md` by default instead of dumping the full content into chat.
- Never fabricate metrics, ownership, experimentation depth, or skills.

## Reference Map

Use the smallest relevant reference set for the current task.

- For first-pass profiling or missing background:
  - [background-intake-strategy.md](references/background-intake-strategy.md)
- For classifying and reranking projects:
  - [project-layering-rules.md](references/project-layering-rules.md)
- For creating or updating the reusable master profile:
  - [master-profile-template.md](references/master-profile-template.md)
- For analyzing a JD and deciding role fit:
  - [jd-analysis-output-template.md](references/jd-analysis-output-template.md)
- For identifying what is missing and what to fix next:
  - [gap-diagnosis-rules.md](references/gap-diagnosis-rules.md)
- For logging roles, resume versions, and workflow outcomes:
  - [application-tracker-schema.md](references/application-tracker-schema.md)
- For generating likely interviewer questions after a tailored resume is done:
  - [interview-question-generation.md](references/interview-question-generation.md)
- For a maintenance-oriented map of the whole workflow:
  - [workflow-overview.md](references/workflow-overview.md)

## Workflow

### 1. Build or Read the Background Profile First

If the user already has a resume, portfolio, project links, or prior application materials, start there.

Extract the obvious facts first:
- identity and education
- internships and work experience
- already-documented projects
- tools and skills
- links, evidence, and published materials

Do not block on perfection. Build version 1 of the profile early, then refine.

If background information is incomplete, read [background-intake-strategy.md](references/background-intake-strategy.md).
If the user wants a persistent profile artifact, structure it with [master-profile-template.md](references/master-profile-template.md).

### 2. Run Multi-Angle Background Intake

When the background is incomplete, do not only ask for "projects".

Probe from multiple angles such as:
- internships and role changes
- competitions, bootcamps, creator programs, training programs
- self-built websites, tools, agents, skills, demos, automations
- content creation and operations work
- workflow improvements or repeated problems the user solved
- experiments, comparisons, and A/B tests or validation work

The goal is to surface experiences the user may not naturally classify as "projects". Use [background-intake-strategy.md](references/background-intake-strategy.md).

### 3. Layer Experiences Before Tailoring

Do not treat all experiences equally.

Classify materials into:
- core projects
- backup high-potential projects
- exploratory projects
- supporting experiences

For internships with multiple responsibilities, store:
- base facts
- narrative versions
- likely JD types for each version

Do not permanently lock project priority. Re-rank by JD later.

When deciding layers or narrative versions, use [project-layering-rules.md](references/project-layering-rules.md).

### 4. Analyze the JD Before Rewriting the Resume

For each JD, always determine:
- whether the role is recommended to apply to
- the strongest fit points
- the biggest risks
- the best storyline for this role
- which project order should be used
- which internship narrative version should be used
- what is missing

Do not treat JD handling as only a rewriting task. Use [jd-analysis-output-template.md](references/jd-analysis-output-template.md).

### 5. Tailor the Resume Strategically

When the user wants resume tailoring, output:
- the recommended storyline
- which experiences should move up
- which experiences should be weakened or omitted
- which keywords must be covered
- a JD-specific resume draft or rewrite strategy

Prefer evidence-backed wording over generic skill lists.

When a user has done multiple functions in one internship, choose one primary narrative version for the main story. Other experience strands can support the story, but do not let the experience read as fragmented.

### 6. Generate Likely Interviewer Questions

After a tailored resume is generated, prepare a likely interviewer question set that is anchored to:
- the JD
- the tailored resume
- the likely company interview style

Before generating questions:
- search the web for interview experiences, interview recaps, or question styles for the target company and similar roles
- prefer company-specific style when evidence exists
- if not enough evidence exists, explicitly fall back to a large-tech-company interview style

Keep the default scope to a 30 to 45 minute interview rather than a massive question bank.

When handling this step, use [interview-question-generation.md](references/interview-question-generation.md).

### 7. Diagnose Gaps Explicitly

For every serious JD analysis, identify:
- hard gaps
- improvable gaps
- bonus gaps

Assess gaps across:
- skills
- experience types
- evidence quality
- metrics
- narrative fit

Also provide what to add next, what metrics or evidence are still needed, and what should be improved before repeatedly targeting similar roles. Use [gap-diagnosis-rules.md](references/gap-diagnosis-rules.md).

### 8. Support Application Tracking

Once the user decides to apply, capture structured application information such as:
- company
- role
- date
- version used
- current status
- next action
- gaps exposed by the JD

Track enough information to avoid duplicate effort and support future review.

If no tracker exists yet, suggest creating one, but do not block progress on current JD handling.
When defining or updating tracker fields, use [application-tracker-schema.md](references/application-tracker-schema.md).

### 9. Close the Loop With Interview Review

If the user gets an interview:
- use the tailored resume and JD as the anchor
- prepare based on actual evidence
- after the interview, feed outcomes back into the background profile, project narratives, and future tailoring strategy

When the user asks for interview preparation, interview review, or multi-interview pattern analysis, hand off to [$interview-coaching-assistant](/Users/asus/.codex/skills/interview-coaching-assistant/SKILL.md).

Use this workflow skill to maintain continuity across the job-search process; use the interview skill for the interview-specific deep work.

## Default Outputs

For background intake, aim to produce:
- first-pass profile summary
- missing information list
- layered experience map
- candidate narrative versions for complex internships

For JD analysis, follow the output structure in [jd-analysis-output-template.md](references/jd-analysis-output-template.md).
After resume generation, optionally produce a likely interviewer-question set using [interview-question-generation.md](references/interview-question-generation.md).

## Common Mistakes

- asking for target roles too early
- only asking for "projects"
- discarding unfinished work too early
- flattening multi-role internships into one vague narrative
- keeping project order static across different JDs
- confusing weak evidence with no evidence
- failing to ask about experiments or validation work
- outputting a rewritten resume without telling the user what still needs to be strengthened

## Boundaries

- Do not invent missing experience.
- Do not turn weak evidence into fake ownership.
- Do not assume the user's self-classification of "not a project" is correct.
- Do not over-penalize incomplete projects before probing their evidence value.
- Do not block useful progress just because the profile is still imperfect.
