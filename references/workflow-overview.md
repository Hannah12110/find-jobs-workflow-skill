# Workflow Overview

## Purpose

Use this file as the maintenance-oriented overview of `find-jobs-workflow`.

This document is not the main runtime instruction file. It is the high-level map of:
- what the skill currently covers
- what order the workflow runs in
- which files support which stages
- what has already been validated in real use
- where future iteration is most valuable

Use it when:
- maintaining the skill
- onboarding yourself back into the workflow
- checking whether a new change belongs in the main skill or a reference file
- reviewing whether the skill has drifted from real usage

## What the Skill Covers

`find-jobs-workflow` is no longer just a resume-rewrite skill.

It currently covers the full job-search workflow:
- background profiling
- project layering
- JD analysis
- resume tailoring
- interviewer-question generation
- gap diagnosis
- application tracking
- interview-prep file generation
- interview-review handoff

Core framing:

This is a reusable job-search workflow skill, not a single-task resume helper.

## Current End-to-End Flow

### 1. Read or Build the Master Profile

First check whether the user already has:
- an old resume
- a portfolio
- project links
- prior application materials
- an existing master profile

If materials exist:
- extract the obvious facts first

If materials do not exist or are incomplete:
- run structured intake

Goal:
- create a reusable master profile rather than immediately writing a role-specific resume

Primary references:
- [background-intake-strategy.md](background-intake-strategy.md)
- [master-profile-template.md](master-profile-template.md)

### 2. Probe Hidden Experience

Do not only ask:
- what projects have you done

Probe from multiple angles:
- internships and role changes
- competitions and programs
- self-built tools, skills, agents, demos
- content creation
- workflow improvements
- experiments, comparisons, and A/B tests

Goal:
- surface experiences the user may not naturally classify as projects

Primary reference:
- [background-intake-strategy.md](background-intake-strategy.md)

### 3. Layer the Experience Pool

After collecting materials, classify them into:
- core projects
- backup high-potential projects
- exploratory projects
- supporting experiences

Important rules:
- unfinished work is not automatically useless
- project priority is not fixed forever
- one internship may contain multiple narrative versions

Primary reference:
- [project-layering-rules.md](project-layering-rules.md)

### 4. Analyze the JD

Before rewriting the resume, decide:
- whether the role is worth applying to
- strongest match points
- risks and missing pieces
- which storyline fits best
- which project order should be used
- which narrative version should be used

Goal:
- support decision-making before editing

Primary reference:
- [jd-analysis-output-template.md](jd-analysis-output-template.md)

### 5. Generate the Tailored Resume

Once the JD is judged worth pursuing:
- choose the main storyline
- choose which experiences move up or down
- choose the right internship narrative version
- write the role-specific resume draft

Important rules:
- prefer evidence-backed phrasing
- do not flatten multi-role internships
- do not keep project order static across roles

Primary references:
- [jd-analysis-output-template.md](jd-analysis-output-template.md)
- [project-layering-rules.md](project-layering-rules.md)

### 6. Generate Likely Interviewer Questions

After a tailored resume is produced:
- generate a likely interviewer-style question set

Rules:
- first search for company-specific interview style
- if found, shape questions to that style
- if not found, explicitly fall back to a large-tech-company style
- keep the default scope to a 30 to 45 minute interview
- anchor the questions in the tailored resume and JD

Primary reference:
- [interview-question-generation.md](interview-question-generation.md)

### 7. Produce the Interview Prep File

Default delivery behavior:
- do not dump the full prep script in chat
- write the prep artifact to `job-search-data/interview-prep/`
- use the filename format `公司-岗位-面试备考稿.md`

Typical contents:
- company-style basis
- likely questions
- high-risk follow-up points
- suggested answer framing

Primary reference:
- [interview-question-generation.md](interview-question-generation.md)

### 8. Diagnose Gaps

For each serious JD, identify:
- hard gaps
- improvable gaps
- bonus gaps

Across dimensions:
- skills
- experience types
- evidence
- metrics
- narrative fit

Goal:
- tell the user what to improve next, and in what order

Primary reference:
- [gap-diagnosis-rules.md](gap-diagnosis-rules.md)

### 9. Update the Application Tracker

When the user analyzes, tailors, or applies:
- update the tracker entry

Typical tracker data includes:
- company
- role
- resume version
- fit judgment
- status
- next action
- exposed gaps
- actual file name used

Primary reference:
- [application-tracker-schema.md](application-tracker-schema.md)

### 10. Hand Off to Interview Review

If the user reaches an interview stage:
- keep the tailored resume and JD as the anchor
- hand off deep interview preparation or review work to the interview skill

Current handoff target:
- [$interview-coaching-assistant](/Users/asus/.codex/skills/interview-coaching-assistant/SKILL.md)

Goal:
- preserve continuity while using the more specialized interview workflow

## Current File Map

### Main skill
- [SKILL.md](/Users/asus/Documents/New%20project/find-jobs-workflow/SKILL.md)

### Core references
- [background-intake-strategy.md](/Users/asus/Documents/New%20project/find-jobs-workflow/references/background-intake-strategy.md)
- [project-layering-rules.md](/Users/asus/Documents/New%20project/find-jobs-workflow/references/project-layering-rules.md)
- [jd-analysis-output-template.md](/Users/asus/Documents/New%20project/find-jobs-workflow/references/jd-analysis-output-template.md)
- [gap-diagnosis-rules.md](/Users/asus/Documents/New%20project/find-jobs-workflow/references/gap-diagnosis-rules.md)
- [master-profile-template.md](/Users/asus/Documents/New%20project/find-jobs-workflow/references/master-profile-template.md)
- [application-tracker-schema.md](/Users/asus/Documents/New%20project/find-jobs-workflow/references/application-tracker-schema.md)
- [interview-question-generation.md](/Users/asus/Documents/New%20project/find-jobs-workflow/references/interview-question-generation.md)

### This overview file
- [workflow-overview.md](/Users/asus/Documents/New%20project/find-jobs-workflow/references/workflow-overview.md)

## What Has Been Validated Already

The workflow has already been tested against real use cases and supports:
- background profiling
- project layering
- multi-role internship narrative splitting
- JD analysis
- tailored resume generation
- application tracker updates
- company-style interview-question generation
- interview-prep file output

This means the skill is already beyond concept stage and is operating as a usable beta workflow.

## Stable Conventions

### Resume and output naming
- tailored resume files should reflect company and role
- tracker entries should store the actual file name used

### Interview prep output
- save by default under `job-search-data/interview-prep/`
- use `公司-岗位-面试备考稿.md`

### Workflow order
- JD analysis comes before resume drafting
- interviewer-question generation comes after resume drafting
- interview review comes after actual interview events

## Current Strengths

The strongest aspects of the workflow today are:
- dynamic project ranking by JD
- handling of multi-role internships
- preservation of unfinished but useful projects
- explicit gap diagnosis
- transition from resume tailoring into interview preparation

## Current Weak Spots or Open Design Choices

These areas may still evolve:
- whether interviewer-question generation should always include answer frameworks by default
- whether JD analysis results should also be saved as separate files under a dedicated directory
- whether some outputs should be split into a second skill in the future

## Recommended Next Iteration Areas

If the skill is iterated further, the most valuable directions are:

1. More real-use JD testing
- especially AI product, growth, operations, and obvious low-fit roles

2. Stronger integration between question generation and answer drafting
- especially when the user wants a ready-to-practice prep file

3. More standardized file output rules
- for resumes
- for JD analyses
- for interview-prep artifacts

## Maintenance Rule

When adding new workflow steps:
- prefer keeping `SKILL.md` lightweight
- put durable detail into reference files
- update this overview so the actual workflow remains easy to inspect

This file should stay readable as the single best overview of the skill's current design.
