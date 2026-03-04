#!/usr/bin/env python3
"""Render interview coaching reports from JSON input.

Supported modes:
- pre: pre-interview prep guide (HTML)
- post: post-interview review report (HTML)
- aggregate: multi-interview personal prep guide (HTML)
- simulation: mock interview feedback (plain text)
"""

from __future__ import annotations

import argparse
import html
import json
from datetime import datetime
from pathlib import Path
from typing import Any


def esc(value: Any) -> str:
    if value is None:
        return ""
    return html.escape(str(value), quote=True)


def as_list(value: Any) -> list[Any]:
    if value is None:
        return []
    if isinstance(value, list):
        return value
    return [value]


def li(items: list[Any]) -> str:
    if not items:
        return "<li>暂无</li>"
    return "".join(f"<li>{esc(item)}</li>" for item in items)


def section_facts(payload: dict[str, Any]) -> str:
    facts = as_list(payload.get("facts"))
    inferences = as_list(payload.get("inferences"))
    missing = as_list(payload.get("data_needed"))
    return f"""
    <div class=\"section\">
      <h2>🧭 事实与推断</h2>
      <p><strong>事实：</strong>{esc('; '.join(str(x) for x in facts)) or '暂无'}</p>
      <p><strong>推断：</strong>{esc('; '.join(str(x) for x in inferences)) or '暂无'}</p>
      <p><strong>仍需补充数据：</strong>{esc('; '.join(str(x) for x in missing)) or '暂无'}</p>
    </div>
    """


def html_shell(title: str, body: str) -> str:
    return f"""<!DOCTYPE html>
<html lang=\"zh-CN\">
<head>
  <meta charset=\"UTF-8\" />
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\" />
  <title>{esc(title)}</title>
  <style>
    body {{ font-family: -apple-system, BlinkMacSystemFont, \"Segoe UI\", Roboto, sans-serif; line-height: 1.6; color: #333; max-width: 1200px; margin: 0 auto; padding: 20px; background: #f6f8fb; }}
    .header {{ background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: #fff; padding: 28px; border-radius: 12px; margin-bottom: 20px; }}
    .header h1 {{ margin: 0; font-size: 28px; }}
    .meta p {{ margin: 6px 0; opacity: 0.95; }}
    .section {{ background: #fff; border-radius: 12px; padding: 22px; margin-bottom: 16px; box-shadow: 0 2px 10px rgba(0,0,0,0.05); }}
    .section h2 {{ margin-top: 0; color: #667eea; border-bottom: 2px solid #667eea; padding-bottom: 8px; }}
    .grid2 {{ display: grid; grid-template-columns: 1fr 1fr; gap: 12px; }}
    .grid3 {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: 10px; }}
    .q-item,.qa,.topic {{ border: 1px solid #e8e8e8; border-radius: 10px; padding: 16px; margin-bottom: 12px; }}
    .star {{ background: #f3e5f5; border-left: 4px solid #9c27b0; border-radius: 8px; padding: 12px; margin-top: 10px; }}
    .warn {{ background: #fff3e0; border-left: 4px solid #ff9800; padding: 12px; border-radius: 8px; }}
    .ok {{ background: #e8f5e9; border-left: 4px solid #4caf50; padding: 12px; border-radius: 8px; margin-top: 10px; }}
    .chip {{ display: inline-block; background: #f0f0f0; border-radius: 999px; padding: 4px 10px; font-size: 12px; margin: 2px 6px 2px 0; }}
    .badge {{ display: inline-block; border-radius: 999px; padding: 3px 10px; font-size: 12px; margin-right: 6px; }}
    .source {{ background: #e3f2fd; color: #1565c0; }}
    .high {{ background: #ffebee; color: #c62828; }}
    .medium {{ background: #fff3e0; color: #e65100; }}
    .low {{ background: #e8f5e9; color: #2e7d32; }}
    .cards {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(170px, 1fr)); gap: 10px; }}
    .card {{ background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); color: #fff; border-radius: 10px; padding: 14px; text-align: center; }}
    .card .n {{ font-size: 28px; font-weight: 700; }}
    @media (max-width: 768px) {{ .grid2, .grid3 {{ grid-template-columns: 1fr; }} }}
  </style>
</head>
<body>
{body}
</body>
</html>
"""


def render_pre(payload: dict[str, Any]) -> str:
    meta = payload.get("meta", {})
    highlights = as_list(payload.get("resume_highlights"))
    match = payload.get("match_analysis", {})
    questions = as_list(payload.get("question_bank"))
    styles = as_list(payload.get("interviewer_style"))
    checklist = as_list(payload.get("prep_checklist"))

    highlights_html = "".join(
        f"<li><strong>{esc(h.get('type', '亮点'))}：</strong>{esc(h.get('text', ''))}"
        f"（对应：{esc(h.get('source', '未知'))}；可关联题：{esc(h.get('question_map', '待补充'))}）</li>"
        for h in highlights
    ) or "<li>暂无</li>"

    q_html = "".join(_render_pre_question(q) for q in questions) or "<div class=\"q-item\">暂无题目</div>"

    body = f"""
    <div class=\"header\">
      <h1>🎯 面试备考指南</h1>
      <div class=\"meta\">
        <p><strong>公司：</strong>{esc(meta.get('company', '未提供'))}</p>
        <p><strong>岗位：</strong>{esc(meta.get('role', '未提供'))}</p>
        <p><strong>轮次：</strong>{esc(meta.get('round', '通用'))}</p>
        <p><strong>生成时间：</strong>{esc(meta.get('generated_at', now_ts()))}</p>
      </div>
    </div>

    <div class=\"section\">
      <h2>🧾 简历亮点清单（必含）</h2>
      <ul>{highlights_html}</ul>
    </div>

    <div class=\"section\">
      <h2>📌 简历与岗位匹配度</h2>
      <p><strong>整体匹配度：</strong>{esc(match.get('score', '未评估'))}</p>
      <div class=\"grid2\">
        <div>
          <h3>✅ 高匹配项</h3>
          <ul>{li(as_list(match.get('high_matches')))}</ul>
        </div>
        <div>
          <h3>⚠️ 低匹配项</h3>
          <ul>{li(as_list(match.get('low_matches')))}</ul>
        </div>
      </div>
      <h3>🎯 备考策略</h3>
      <ul>{li(as_list(match.get('prep_advice')))}</ul>
    </div>

    <div class=\"section\">
      <h2>💡 高频题库（按优先级）</h2>
      {q_html}
    </div>

    <div class=\"section\">
      <h2>🎭 面试官风格分析</h2>
      <ul>{li(styles)}</ul>
    </div>

    <div class=\"section\">
      <h2>✅ 备考清单</h2>
      <ul>{li(checklist)}</ul>
    </div>

    {section_facts(payload)}
    """
    return html_shell("面试备考指南", body)


def _render_pre_question(q: dict[str, Any]) -> str:
    star = q.get("star", {}) if isinstance(q.get("star"), dict) else {}
    freq = str(q.get("frequency", "中频")).lower()
    freq_class = "high" if "高" in freq or "high" in freq else "medium" if "中" in freq or "med" in freq else "low"
    points = as_list(q.get("score_points"))
    return f"""
    <div class=\"q-item\">
      <h3>{esc(q.get('title', '题目'))}</h3>
      <p>
        <span class=\"badge source\">来源：{esc(q.get('source', '未标注'))}</span>
        <span class=\"badge {freq_class}\">频率：{esc(q.get('frequency', '中频'))}</span>
      </p>
      <p><strong>考察意图：</strong>{esc(q.get('intent', '待分析'))}</p>
      <div class=\"star\">
        <p><strong>STAR参考回答：</strong></p>
        <p><strong>S：</strong>{esc(star.get('s', ''))}</p>
        <p><strong>T：</strong>{esc(star.get('t', ''))}</p>
        <p><strong>A：</strong>{esc(star.get('a', ''))}</p>
        <p><strong>R：</strong>{esc(star.get('r', ''))}</p>
        <p><strong>关键得分点：</strong>{esc('；'.join(str(x) for x in points)) or '暂无'}</p>
      </div>
    </div>
    """


def render_post(payload: dict[str, Any]) -> str:
    meta = payload.get("meta", {})
    qa_reviews = as_list(payload.get("qa_reviews"))
    summary = payload.get("summary", {})
    resume_diag = payload.get("resume_diagnosis", {})
    revisions = as_list(payload.get("resume_revisions"))
    resume_checklist = as_list(payload.get("resume_checklist"))

    qa_html = "".join(_render_qa_item(i + 1, item) for i, item in enumerate(qa_reviews)) or "<div class=\"qa-card\">暂无问答数据</div>"

    score_rows = []
    for item in qa_reviews:
        sc = item.get("scores", {}) if isinstance(item.get("scores"), dict) else {}
        vals = [sc.get("accuracy"), sc.get("completeness"), sc.get("logic"), sc.get("communication"), sc.get("fit")]
        nums = [int(v) for v in vals if isinstance(v, (int, float))]
        if nums:
            score_rows.append(sum(nums) / len(nums))
    avg_score = round(sum(score_rows) / len(score_rows), 1) if score_rows else 0.0

    before_after = "".join(
        f"""
        <div class=\"rev-grid\">
          <div class=\"rev-before\"><h4>修改前</h4><p>{esc(r.get('before', ''))}</p></div>
          <div class=\"rev-after\"><h4>推荐改写</h4><p>{esc(r.get('after', ''))}</p></div>
        </div>
        <p><strong>修改要点：</strong>{esc('；'.join(str(x) for x in as_list(r.get('tips')))) or '暂无'}</p>
        <p><strong>数据补充：</strong>{esc('；'.join(str(x) for x in as_list(r.get('data_needed')))) or '暂无'}</p>
        """
        for r in revisions
    ) or "<p>暂无前后对比示例</p>"

    strengths_html = "".join(f"<li>{esc(x)}</li>" for x in as_list(summary.get("strengths"))) or "<li>暂无</li>"
    weaknesses_html = "".join(f"<li>{esc(x)}</li>" for x in as_list(summary.get("weaknesses"))) or "<li>暂无</li>"
    priorities_html = "".join(f"<li>{esc(x)}</li>" for x in as_list(summary.get("priorities"))) or "<li>暂无</li>"
    path_html = "".join(f"<li>{esc(x)}</li>" for x in as_list(summary.get("learning_path"))) or "<li>暂无</li>"
    checklist_html = "".join(f"<li>{esc(x)}</li>" for x in resume_checklist) or "<li>暂无</li>"
    facts_html = "".join(f"<li>{esc(x)}</li>" for x in as_list(payload.get("facts"))) or "<li>暂无</li>"
    inf_html = "".join(f"<li>{esc(x)}</li>" for x in as_list(payload.get("inferences"))) or "<li>暂无</li>"
    data_html = "".join(f"<li>{esc(x)}</li>" for x in as_list(payload.get("data_needed"))) or "<li>暂无</li>"

    return f"""<!DOCTYPE html>
<html lang=\"zh-CN\">
<head>
  <meta charset=\"UTF-8\" />
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\" />
  <title>面试复盘报告</title>
  <style>
    :root {{
      --bg: #f1f0ec;
      --panel: #f7f7f4;
      --card: #ffffff;
      --ink: #2f3a30;
      --muted: #6d746d;
      --line: #d8ddd3;
      --primary: #556b52;
      --primary-soft: #e6ece3;
      --danger-soft: #f8ebe8;
      --ok-soft: #e9f1e7;
      --radius-xl: 24px;
      --radius-lg: 18px;
      --radius-md: 12px;
      --shadow: 0 16px 40px rgba(68, 79, 67, 0.10);
    }}
    * {{ box-sizing: border-box; }}
    html, body {{ margin: 0; padding: 0; }}
    body {{
      font-family: "PingFang SC", "Noto Sans SC", "Microsoft YaHei", "Source Han Sans SC", sans-serif;
      color: var(--ink);
      background:
        radial-gradient(circle at 20% 10%, #ffffff 0, #f1f0ec 36%),
        radial-gradient(circle at 100% 0, #f9faf7 0, rgba(249,250,247,0) 45%),
        var(--bg);
      min-height: 100vh;
    }}
    .layout {{
      display: grid;
      grid-template-columns: 272px 1fr;
      min-height: 100vh;
    }}
    .sidebar {{
      background: #ecebe7;
      border-right: 1px solid var(--line);
      padding: 28px 16px;
      position: sticky;
      top: 0;
      height: 100vh;
    }}
    .brand {{
      font-size: 24px;
      font-weight: 800;
      letter-spacing: 0.04em;
      color: var(--primary);
      margin: 6px 10px 28px;
    }}
    .meta-box {{
      background: #f7f7f3;
      border: 1px solid var(--line);
      border-radius: var(--radius-lg);
      padding: 14px;
      margin: 0 8px 18px;
    }}
    .meta-box p {{
      margin: 6px 0;
      color: var(--muted);
      font-size: 13px;
      line-height: 1.4;
    }}
    .meta-box b {{ color: var(--ink); }}
    .nav {{
      display: flex;
      flex-direction: column;
      gap: 8px;
      padding: 0 8px;
    }}
    .nav a {{
      text-decoration: none;
      color: #3d4740;
      background: #f3f4ef;
      border: 1px solid transparent;
      border-radius: 999px;
      padding: 10px 14px;
      font-size: 14px;
      transition: all .2s ease;
    }}
    .nav a:hover {{
      border-color: #c6d1c2;
      background: #e9efe6;
    }}
    .content {{
      padding: 28px clamp(14px, 2.4vw, 36px);
      max-width: 1200px;
      width: 100%;
      margin: 0 auto;
    }}
    .hero {{
      background:
        radial-gradient(circle at 50% 0, rgba(213, 224, 209, 0.8), rgba(213, 224, 209, 0)),
        repeating-radial-gradient(circle at center, rgba(107,126,105,0.06) 0 2px, transparent 2px 28px),
        var(--panel);
      border: 1px solid var(--line);
      border-radius: 30px;
      padding: clamp(14px, 1.8vw, 22px);
      box-shadow: var(--shadow);
      margin-bottom: 14px;
      display: grid;
      gap: 12px;
      grid-template-columns: 1.5fr 200px;
      align-items: center;
    }}
    .hero h1 {{
      margin: 0 0 8px;
      font-size: clamp(24px, 3.2vw, 38px);
      line-height: 1.12;
      letter-spacing: 0.02em;
      color: var(--primary);
      font-weight: 800;
      white-space: nowrap;
    }}
    .hero p {{
      margin: 0;
      color: #4d594d;
      font-size: 14px;
      line-height: 1.5;
      max-width: 56ch;
    }}
    .score-panel {{
      background: #f3f6f0;
      border: 1px solid #d7dfd3;
      border-radius: 22px;
      padding: 12px;
      text-align: center;
    }}
    .score-label {{
      font-size: 12px;
      color: #627064;
      letter-spacing: .08em;
      text-transform: uppercase;
    }}
    .score-val {{
      margin: 5px 0 3px;
      font-size: 34px;
      line-height: 1;
      color: var(--primary);
      font-weight: 800;
    }}
    .score-sub {{
      color: #6f786f;
      font-size: 13px;
    }}
    .section {{
      background: var(--card);
      border: 1px solid var(--line);
      border-radius: var(--radius-xl);
      padding: 20px;
      margin-bottom: 14px;
      box-shadow: 0 8px 20px rgba(86, 101, 82, 0.06);
    }}
    .section h2 {{
      margin: 0 0 14px;
      color: var(--primary);
      font-size: 24px;
      letter-spacing: 0.01em;
    }}
    .grid {{
      display: grid;
      grid-template-columns: repeat(2, minmax(0, 1fr));
      gap: 14px;
    }}
    .mini {{
      border-radius: var(--radius-lg);
      border: 1px solid var(--line);
      background: #f9faf8;
      padding: 14px;
    }}
    .mini h3 {{
      margin: 0 0 8px;
      font-size: 17px;
      color: #3f5141;
    }}
    ul, ol {{ margin: 8px 0 0 20px; padding: 0; }}
    li {{ margin: 5px 0; line-height: 1.6; }}
    .qa-card {{
      border: 1px solid var(--line);
      border-radius: var(--radius-lg);
      background: linear-gradient(180deg, #ffffff, #fbfcfa);
      padding: 16px;
      margin-bottom: 12px;
    }}
    .qa-card h3 {{
      margin: 0 0 8px;
      font-size: 18px;
      color: #334133;
    }}
    .chip-row {{
      display: flex;
      flex-wrap: wrap;
      gap: 8px;
      margin: 8px 0 10px;
    }}
    .chip {{
      display: inline-flex;
      align-items: center;
      border-radius: 999px;
      border: 1px solid #d2dacd;
      background: #eff4ed;
      color: #465444;
      padding: 4px 10px;
      font-size: 12px;
      white-space: nowrap;
    }}
    .score-low {{
      background: #f8ecea;
      border-color: #ebd3cf;
      color: #805553;
    }}
    .score-mid {{
      background: #f8f1e7;
      border-color: #eadbc5;
      color: #7d6645;
    }}
    .score-high {{
      background: #eaf3e7;
      border-color: #cfe0c8;
      color: #4c6a49;
    }}
    .intent-chip {{
      background: #e5ece1;
      border-color: #c7d2c0;
    }}
    .panel {{
      border-radius: 14px;
      padding: 12px;
      margin-top: 10px;
      border: 1px solid;
    }}
    .warn {{ background: var(--danger-soft); border-color: #f0d3cb; }}
    .ok {{ background: #edf1fb; border-color: #d4dced; }}
    .star {{
      background: #f6f1e6;
      border: 1px solid #e4d8bf;
      border-left: 4px solid #98835a;
      border-radius: 14px;
      padding: 12px;
      margin-top: 10px;
    }}
    .rev-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 12px;
    }}
    .rev-before, .rev-after {{
      border-radius: 14px;
      padding: 12px;
      border: 1px solid;
      min-height: 104px;
    }}
    .rev-before {{ background: #f8eeea; border-color: #eed7d0; }}
    .rev-after {{ background: #ecf4e9; border-color: #d2e2cc; }}
    .facts-grid {{
      display: grid;
      grid-template-columns: repeat(3, minmax(0, 1fr));
      gap: 12px;
    }}
    .facts-card {{
      border: 1px solid var(--line);
      border-radius: 14px;
      padding: 12px;
      background: #f8faf6;
    }}
    .facts-card h3 {{
      margin: 0 0 8px;
      color: #3e4e3f;
      font-size: 16px;
    }}
    @media (max-width: 1024px) {{
      .layout {{ grid-template-columns: 1fr; }}
      .sidebar {{
        position: static;
        height: auto;
        border-right: 0;
        border-bottom: 1px solid var(--line);
      }}
      .hero {{ grid-template-columns: 1fr; }}
      .facts-grid {{ grid-template-columns: 1fr; }}
      .grid {{ grid-template-columns: 1fr; }}
    }}
  </style>
</head>
<body>
  <div class=\"layout\">
    <aside class=\"sidebar\">
      <div class=\"brand\">面试复盘</div>
      <div class=\"meta-box\">
        <p><b>公司</b>：{esc(meta.get('company', '未提供'))}</p>
        <p><b>岗位</b>：{esc(meta.get('role', '未提供'))}</p>
        <p><b>轮次</b>：{esc(meta.get('round', '未提供'))}</p>
        <p><b>时间</b>：{esc(meta.get('generated_at', now_ts()))}</p>
      </div>
      <nav class=\"nav\">
        <a href=\"#qa\">逐题复盘</a>
        <a href=\"#summary\">综合总结</a>
        <a href=\"#resume\">简历诊断</a>
        <a href=\"#checklist\">检查清单</a>
        <a href=\"#facts\">事实与推断</a>
      </nav>
    </aside>

    <main class=\"content\">
      <section class=\"hero\">
        <div>
          <h1>聚焦关键短板，拿下下一轮</h1>
          <p>这份复盘围绕“逐题表现、简历叙事、可量化证据”三条主线，帮助你把回答从“经历陈述”升级为“结果证明”。</p>
        </div>
        <div class=\"score-panel\">
          <div class=\"score-label\">平均面试表现</div>
          <div class=\"score-val\">{esc(avg_score)}</div>
          <div class=\"score-sub\">满分 5.0</div>
        </div>
      </section>

      <section class=\"section\" id=\"qa\">
        <h2>逐题复盘</h2>
        {qa_html}
      </section>

      <section class=\"section\" id=\"summary\">
        <h2>综合总结</h2>
        <div class=\"grid\">
          <div class=\"mini\"><h3>优势</h3><ul>{strengths_html}</ul></div>
          <div class=\"mini\"><h3>待改进</h3><ul>{weaknesses_html}</ul></div>
        </div>
        <div class=\"grid\" style=\"margin-top:12px;\">
          <div class=\"mini\"><h3>改进优先级</h3><ol>{priorities_html}</ol></div>
          <div class=\"mini\"><h3>学习路径</h3><ul>{path_html}</ul></div>
        </div>
      </section>

      <section class=\"section\" id=\"resume\">
        <h2>简历问题诊断与修改建议</h2>
        <div class=\"mini\">
          <ul>
            <li>数据缺失问题：{esc(resume_diag.get('missing_metrics', '暂无'))}</li>
            <li>技术深度不足：{esc(resume_diag.get('tech_depth', '暂无'))}</li>
            <li>成果闭环不完整：{esc(resume_diag.get('result_loop', '暂无'))}</li>
            <li>竞争优势不突出：{esc(resume_diag.get('differentiation', '暂无'))}</li>
            <li>逻辑结构问题：{esc(resume_diag.get('narrative', '暂无'))}</li>
          </ul>
        </div>
        <h3 style=\"margin:14px 0 8px; color:#425443;\">修改前后对比</h3>
        {before_after}
        <h3 style=\"margin:14px 0 8px; color:#425443;\">2 分钟自我介绍优化</h3>
        <div class=\"mini\"><p style=\"margin:0;\">{esc(resume_diag.get('self_intro_2min', '暂无'))}</p></div>
      </section>

      <section class=\"section\" id=\"checklist\">
        <h2>简历修改检查清单</h2>
        <ul>{checklist_html}</ul>
      </section>

      <section class=\"section\" id=\"facts\">
        <h2>事实与推断</h2>
        <div class=\"facts-grid\">
          <div class=\"facts-card\"><h3>事实</h3><ul>{facts_html}</ul></div>
          <div class=\"facts-card\"><h3>推断</h3><ul>{inf_html}</ul></div>
          <div class=\"facts-card\"><h3>仍需补充数据</h3><ul>{data_html}</ul></div>
        </div>
      </section>
    </main>
  </div>
</body>
</html>
"""


def _to_cn_num(n: int) -> str:
    mapping = {
        1: "一", 2: "二", 3: "三", 4: "四", 5: "五",
        6: "六", 7: "七", 8: "八", 9: "九", 10: "十",
        11: "十一", 12: "十二", 13: "十三", 14: "十四", 15: "十五",
        16: "十六", 17: "十七", 18: "十八", 19: "十九", 20: "二十",
    }
    return mapping.get(n, str(n))


def _render_qa_item(index: int, item: dict[str, Any]) -> str:
    scores = item.get("scores", {}) if isinstance(item.get("scores"), dict) else {}
    star = item.get("star", {}) if isinstance(item.get("star"), dict) else {}
    def _score_chip(label: str, raw: Any) -> str:
        cls = ""
        if isinstance(raw, (int, float)):
            if raw <= 3:
                cls = " score-low"
            elif raw == 4:
                cls = " score-mid"
            elif raw >= 5:
                cls = " score-high"
        return f"<span class=\"chip{cls}\">{esc(label)}：{esc(raw)}/5</span>"

    chips_html = "".join(
        [
            _score_chip("准确性", scores.get("accuracy", "-")),
            _score_chip("完整性", scores.get("completeness", "-")),
            _score_chip("逻辑性", scores.get("logic", "-")),
            _score_chip("表达力", scores.get("communication", "-")),
            _score_chip("匹配度", scores.get("fit", "-")),
        ]
    )
    return f"""
    <div class=\"qa-card\">
      <h3>问题{esc(_to_cn_num(index))}：{esc(item.get('question', ''))}</h3>
      <p><strong>你的回答：</strong>{esc(item.get('answer', ''))}</p>
      <div class=\"chip-row\"><span class=\"chip intent-chip\">考察意图：{esc(item.get('intent', '待分析'))}</span>{chips_html}</div>
      <div class=\"panel warn\"><strong>存在问题：</strong><ul>{li(as_list(item.get('problems')))}</ul></div>
      <div class=\"panel ok\"><strong>改进建议：</strong><ul>{li(as_list(item.get('suggestions')))}</ul></div>
      <div class=\"star\">
        <strong>STAR优化回答：</strong>
        <p><strong>S：</strong>{esc(star.get('s', ''))}</p>
        <p><strong>T：</strong>{esc(star.get('t', ''))}</p>
        <p><strong>A：</strong>{esc(star.get('a', ''))}</p>
        <p><strong>R：</strong>{esc(star.get('r', ''))}</p>
      </div>
    </div>
    """


def render_aggregate(payload: dict[str, Any]) -> str:
    meta = payload.get("meta", {})
    overview = payload.get("overview", {})
    topics = as_list(payload.get("high_frequency_topics"))
    swot = payload.get("swot", {})
    plan = payload.get("plan", {})
    resources = as_list(payload.get("resources"))
    bank = as_list(payload.get("personalized_question_bank"))

    topics_html = "".join(_render_topic(t) for t in topics) or "<div class=\"topic\">暂无高频考点</div>"
    bank_html = "".join(
        f"<li><strong>{esc(x.get('question', ''))}</strong>（优先级：{esc(x.get('priority', '中'))}；掌握：{esc(x.get('mastery', '中'))}）</li>"
        for x in bank
    ) or "<li>暂无</li>"

    body = f"""
    <div class=\"header\">
      <h1>📊 个人备考指南</h1>
      <div class=\"meta\">
        <p><strong>分析基于：</strong>{esc(meta.get('interview_count', overview.get('interviews', '未提供')))}次面试记录</p>
        <p><strong>目标岗位：</strong>{esc(meta.get('role', '未提供'))}</p>
        <p><strong>生成时间：</strong>{esc(meta.get('generated_at', now_ts()))}</p>
      </div>
    </div>

    <div class=\"section\">
      <h2>📈 数据概览</h2>
      <div class=\"cards\">
        <div class=\"card\"><div class=\"n\">{esc(overview.get('interviews', 0))}</div><div>面试次数</div></div>
        <div class=\"card\"><div class=\"n\">{esc(overview.get('companies', 0))}</div><div>涉及公司</div></div>
        <div class=\"card\"><div class=\"n\">{esc(overview.get('questions', 0))}</div><div>问题总数</div></div>
        <div class=\"card\"><div class=\"n\">{esc(overview.get('high_freq_points', 0))}</div><div>高频考点</div></div>
      </div>
    </div>

    <div class=\"section\">
      <h2>🎯 高频考点清单</h2>
      {topics_html}
    </div>

    <div class=\"section\">
      <h2>🔍 SWOT</h2>
      <div class=\"grid3\">
        <div class=\"topic\"><h3>💪 Strengths</h3><ul>{li(as_list(swot.get('strengths')))}</ul></div>
        <div class=\"topic\"><h3>⚠️ Weaknesses</h3><ul>{li(as_list(swot.get('weaknesses')))}</ul></div>
        <div class=\"topic\"><h3>🚀 Next Actions</h3><ul>{li(as_list(swot.get('next_actions')))}</ul></div>
      </div>
    </div>

    <div class=\"section\">
      <h2>📋 个人化备考计划</h2>
      <ul>
        <li><strong>紧急：</strong>{esc('；'.join(str(x) for x in as_list(plan.get('urgent')))) or '暂无'}</li>
        <li><strong>重点巩固：</strong>{esc('；'.join(str(x) for x in as_list(plan.get('important')))) or '暂无'}</li>
        <li><strong>长期：</strong>{esc('；'.join(str(x) for x in as_list(plan.get('longterm')))) or '暂无'}</li>
      </ul>
      <h3>🎯 个人化题库</h3>
      <ul>{bank_html}</ul>
      <h3>📚 学习资源</h3>
      <ul>{li(resources)}</ul>
    </div>

    {section_facts(payload)}
    """
    return html_shell("个人备考指南", body)


def _render_topic(topic: dict[str, Any]) -> str:
    freq = esc(topic.get("count", 0))
    mastery = esc(topic.get("mastery", "中"))
    return f"""
    <div class=\"topic\">
      <h3>{esc(topic.get('name', '考点'))}</h3>
      <p><span class=\"chip\">出现{freq}次</span><span class=\"chip\">掌握：{mastery}</span></p>
      <p><strong>考察意图：</strong>{esc(topic.get('intent', '待分析'))}</p>
      <p><strong>涉及问题：</strong>{esc('；'.join(str(x) for x in as_list(topic.get('questions')))) or '暂无'}</p>
      <p><strong>你的表现：</strong>{esc(topic.get('performance', '待评估'))}</p>
    </div>
    """


def render_simulation(payload: dict[str, Any]) -> str:
    scores = payload.get("scores", {}) if isinstance(payload.get("scores"), dict) else {}
    star = payload.get("star", {}) if isinstance(payload.get("star"), dict) else {}
    lines = [
        "🎤 模拟面试反馈",
        "",
        "【评分】",
        f"准确性：{scores.get('accuracy', '-')}/5",
        f"完整性：{scores.get('completeness', '-')}/5",
        f"逻辑性：{scores.get('logic', '-')}/5",
        f"表达力：{scores.get('communication', '-')}/5",
        f"匹配度：{scores.get('fit', '-')}/5",
        "",
        "【存在的问题】",
    ]
    problems = as_list(payload.get("problems")) or ["暂无"]
    lines.extend([f"{idx}. {item}" for idx, item in enumerate(problems, start=1)])
    lines.extend(["", "【改进建议】"])
    suggestions = as_list(payload.get("suggestions")) or ["暂无"]
    lines.extend([f"{idx}. {item}" for idx, item in enumerate(suggestions, start=1)])
    lines.extend(
        [
            "",
            "【标准回答参考】",
            f"Situation：{star.get('s', '')}",
            f"Task：{star.get('t', '')}",
            f"Action：{star.get('a', '')}",
            f"Result：{star.get('r', '')}",
            "",
            "【事实与推断】",
            f"- 事实：{'；'.join(str(x) for x in as_list(payload.get('facts'))) or '暂无'}",
            f"- 推断：{'；'.join(str(x) for x in as_list(payload.get('inferences'))) or '暂无'}",
            f"- 仍需补充数据：{'；'.join(str(x) for x in as_list(payload.get('data_needed'))) or '暂无'}",
        ]
    )
    return "\n".join(lines)


def detect_mode(payload: dict[str, Any], mode_arg: str | None) -> str:
    if mode_arg:
        return mode_arg
    mode = payload.get("mode")
    if isinstance(mode, str) and mode:
        return mode
    if payload.get("qa_reviews"):
        return "post"
    if payload.get("high_frequency_topics"):
        return "aggregate"
    return "pre"


def now_ts() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M")


def output_path(input_path: Path, out_arg: str | None, mode: str) -> Path:
    if out_arg:
        return Path(out_arg)
    suffix = ".txt" if mode == "simulation" else ".html"
    return input_path.with_name(f"{input_path.stem}-{mode}{suffix}")


def render(payload: dict[str, Any], mode: str) -> str:
    if mode == "pre":
        return render_pre(payload)
    if mode == "post":
        return render_post(payload)
    if mode == "aggregate":
        return render_aggregate(payload)
    if mode == "simulation":
        return render_simulation(payload)
    raise ValueError(f"Unsupported mode: {mode}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Render interview coaching reports from JSON")
    parser.add_argument("--input", required=True, help="Path to input JSON file")
    parser.add_argument("--output", help="Path to output file (.html or .txt)")
    parser.add_argument(
        "--mode",
        choices=["pre", "post", "aggregate", "simulation"],
        help="Force mode; otherwise auto-detect from JSON",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    input_path = Path(args.input)
    payload = json.loads(input_path.read_text(encoding="utf-8"))
    mode = detect_mode(payload, args.mode)
    content = render(payload, mode)
    out_path = output_path(input_path, args.output, mode)
    out_path.write_text(content, encoding="utf-8")
    print(f"Rendered {mode} report -> {out_path}")


if __name__ == "__main__":
    main()
