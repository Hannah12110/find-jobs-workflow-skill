# Report JSON Input Contract

Use `scripts/render_report.py` with this JSON contract.

## Common fields

```json
{
  "mode": "pre|post|aggregate|simulation",
  "meta": {
    "company": "字节跳动",
    "role": "前端开发工程师",
    "round": "二面",
    "generated_at": "2026-03-04 19:40"
  },
  "facts": ["来自简历或面试记录的事实"],
  "inferences": ["分析推断"],
  "data_needed": ["仍需补充的数据"]
}
```

## Pre mode

- `resume_highlights`: array of `{type,text,source,question_map}`
- `match_analysis`: `{score,high_matches[],low_matches[],prep_advice[]}`
- `question_bank`: array of `{title,source,frequency,intent,star:{s,t,a,r},score_points[]}`
- `interviewer_style`: string[]
- `prep_checklist`: string[]

## Post mode

- `qa_reviews`: array of
  - `question`, `answer`, `intent`
  - `scores`: `{accuracy,completeness,logic,communication,fit}`
  - `problems`: string[]
  - `suggestions`: string[]
  - `star`: `{s,t,a,r}`
- `summary`: `{strengths[],weaknesses[],priorities[],learning_path[]}`
- `resume_diagnosis`: `{missing_metrics,tech_depth,result_loop,differentiation,narrative,self_intro_2min}`
- `resume_revisions`: array of `{before,after,tips[],data_needed[]}`
- `resume_checklist`: string[]

## Aggregate mode

- `overview`: `{interviews,companies,questions,high_freq_points}`
- `high_frequency_topics`: array of `{name,count,mastery,intent,questions[],performance}`
- `swot`: `{strengths[],weaknesses[],next_actions[]}`
- `plan`: `{urgent[],important[],longterm[]}`
- `resources`: string[]
- `personalized_question_bank`: array of `{question,priority,mastery}`

## Simulation mode

- `scores`: `{accuracy,completeness,logic,communication,fit}`
- `problems`: string[]
- `suggestions`: string[]
- `star`: `{s,t,a,r}`
