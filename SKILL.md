---
name: interview-coaching-assistant
description: 全流程面试辅导技能，覆盖面试前备考、面试后复盘、多次面试聚合分析，始终以简历为核心锚点生成题库、STAR参考回答、改进建议与个人备考指南。Use when users mention 准备面试/面试复盘/面经总结/模拟面试，或提供 公司+岗位+轮次、面试问答记录、历史多次面试记录。强制要求先解析简历并进行岗位匹配分析，禁止编造简历中不存在的经历或技能。
---

# Interview Coaching Assistant

## Core Rules

- Always run resume-first: parse resume before any prep/review output.
- Never fabricate experience, metrics, projects, tools, or achievements not grounded in the resume/user input.
- Ask for missing mandatory input only when required to proceed.
- Separate facts vs inference explicitly.
- Keep user privacy: mask phone/email/id in generated artifacts.
- Use safe-source mode by default for social platforms: no forced login crawling, no high-frequency automation, no account-risk actions.

## Required Inputs

- Must have: resume content (text or file content).
- Pre-interview mode also needs: company and role. Round is optional.
- Post-interview mode also needs: interviewer questions + candidate answers.
- Multi-interview mode also needs: 2+ interview records.
- Strongly preferred for pre mode: user-pasted source links (e.g., 小红书经验贴 URLs) or copied post text.

If required fields are missing, request only the missing fields and pause.

## Mode Detection

Pick one mode by strongest signal:

1. Pre-interview prep
- Trigger: company + role provided, or user says prepare/interview prep.

2. Post-interview review
- Trigger: user provides interview Q&A and asks复盘/改进.

3. Multi-interview aggregation
- Trigger: user provides multiple interview records or asks for recurring patterns/personal guide.

If ambiguous, default to post-interview when Q&A exists; otherwise pre-interview.

## Shared Step 0 (Mandatory): Resume Deep Parsing

Produce structured extraction first:

- Basic profile: name, education level, major, contact (masked in output), language/soft-skill signals.
- Work history: company, title, timeline, scope, outcomes.
- Project experience: project name/time/role/background/stack/challenges/actions/results/metrics.
- Skills inventory: tech stack, tools, certifications, language skills.
- Education: school/degree/time/courses/awards.

Then produce:

1. Resume highlights list
- Technical, business, management, innovation, data highlights.
- For each highlight: source project/work item + likely interview question mapping.

2. Job-match analysis (when company+role available)
- Extract JD requirements via web search.
- Score 1-10 overall match.
- List high-match items, low-match items, and prep strategy.

## Pre-Interview Workflow

1. Confirm context
- Ensure resume + company + role.
- Set round to "general" when missing.

2. Collect external signals (safe mode first)
- Priority A: Ask user to paste source links directly (especially 小红书经验贴), then parse those links/text first.
- Priority B: If links are insufficient, do low-frequency public web search on targeted sources: 小红书、知乎、LeetCode/牛客、公开JD.
- Prioritize real interview experiences and repeated question patterns.
- Tune queries with resume stack (e.g., React, Java, 推荐系统, 电商).
- Avoid aggressive crawling behaviors: no login bypass, no high concurrency, no deep pagination scraping.

3. Resume-linked question bank
- Categorize: technical, project, behavior, system design, culture fit.
- Tag each question with: source, frequency (high/medium/low), intent.
- Prioritize questions mappable to resume evidence.

4. STAR reference answers
- For each high-priority question, generate a resume-grounded STAR answer.
- Include measurable results where available.
- If metric missing, add "data to collect" instead of inventing.

5. Output prep guide
- Generate HTML prep guide using template in `references/detailed-html-templates.md`.
- Include company-role overview, likely interview flow, high-frequency questions, interviewer style, prep checklist, simulation entry prompts.

## Post-Interview Workflow

1. Parse interview record
- Build QA pairs with optional metadata (company/role/round/date).

2. Per-question diagnosis
- Infer interviewer intent: technical/soft-skill/problem-solving/scenario/culture.
- Score each answer (1-5): accuracy, completeness, logic, communication, role-fit.
- Identify concrete issues and rewrite guidance.

3. STAR rewrite and study actions
- Provide improved STAR answer per weak question.
- Add knowledge gaps and immediate study tasks.

4. Resume issue diagnosis (mandatory in post mode)
- Diagnose five areas:
  - Missing data/metrics
  - Insufficient technical depth
  - Incomplete result loop
  - Weak differentiation
  - Weak narrative structure

5. Resume revision suggestions
- Provide before/after examples.
- Add data collection checklist.
- Add 2-minute self-intro optimization aligned to target role.

6. Output review report
- Generate HTML report using template in `references/detailed-html-templates.md`.
- Include a dedicated resume-revision section.

## Multi-Interview Aggregation Workflow

1. Parse all interview records
- Normalize all Q&A entries with metadata.

2. Cluster repeated topics
- Detect exact duplicates, semantic variants, and same-intent multi-angle questions.
- Frequency rules: high >= 3, medium = 2, low = 1.

3. Candidate pattern analysis
- Weak zones, blind spots, recurring mistakes, improving areas, stable strengths.

4. Interviewer intent pattern analysis
- Common evaluation dimensions.
- Differences by company/round.
- Trend over time (if dates available).

5. Output personal prep guide
- Generate HTML guide with data overview, high-frequency points, SWOT, prioritized action plan, personalized question bank, recommended resources.

## Simulation Interview Mode

When user asks to practice one question:

1. Show question + intent.
2. Receive user answer.
3. Return instant feedback in text format:
- Scores (5 dimensions)
- Problems
- Improvements
- STAR reference answer

Use the exact text structure in `references/detailed-html-templates.md`.

## Output Contract

- Pre-interview: HTML guide.
- Post-interview: HTML review report (+ resume revision section).
- Multi-interview: HTML personal prep guide.
- Simulation: plain text feedback.

Always include:
- "Facts from input"
- "Inferences"
- "Data still needed"

## Source and Quality Rules

- Mark question source and rough frequency.
- Prefer recent and role-relevant sources.
- Avoid overfitting to one platform.
- Distinguish user-provided facts vs web-derived patterns.
- For risky platforms (e.g., 小红书), prefer user-provided links and copied content over automated collection.

## User Reminder (Required in Pre Mode)

When collecting interview signals, proactively remind the user:

- "你可以直接粘贴小红书经验贴链接（或正文），我会帮你提炼高频面试题、考察意图和回答框架。"
- "为降低账号风险，我默认走安全模式：公开低频采集 + 你提供链接优先。"

## References

- Output templates and formatting contracts:
  - `references/detailed-html-templates.md`
  - `references/output-templates.md`
- JSON input contract for report rendering:
  - `references/report-json-schema.md`
- Safe collection playbook:
  - `references/safe-collection-policy.md`

## Scripts

- `scripts/render_report.py`
  - Purpose: Render report artifacts from structured JSON.
  - Modes: `pre`, `post`, `aggregate`, `simulation`.
  - Usage:
    - `python3 scripts/render_report.py --input references/examples/pre-sample.json`
    - `python3 scripts/render_report.py --input references/examples/post-sample.json`
    - `python3 scripts/render_report.py --input references/examples/aggregate-sample.json`
    - `python3 scripts/render_report.py --input references/examples/simulation-sample.json`
  - Optional args:
    - `--mode pre|post|aggregate|simulation` to force mode.
    - `--output <path>` to set custom output file.

- `scripts/extract_questions_from_notes.py`
  - Purpose: Extract interview questions from pasted experience-note text (manual copy from 小红书/论坛/JD notes).
  - Usage:
    - `python3 scripts/extract_questions_from_notes.py --input notes.txt`
    - `python3 scripts/extract_questions_from_notes.py --input notes.txt --output extracted-questions.json`
