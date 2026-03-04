#!/usr/bin/env python3
"""Extract interview-question candidates from pasted notes text.

Usage:
  python3 scripts/extract_questions_from_notes.py --input notes.txt
  python3 scripts/extract_questions_from_notes.py --input notes.txt --output extracted-questions.json
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


QUESTION_PATTERNS = [
    re.compile(r"^\s*(?:Q\d+[\.:：]?\s*)?(.+[?？])\s*$"),
    re.compile(r"^\s*(?:面试官(?:问|追问)[:：]\s*)(.+)$"),
    re.compile(r"^\s*(?:问题[:：]\s*)(.+)$"),
]


def normalize(text: str) -> str:
    text = text.strip()
    text = re.sub(r"\s+", " ", text)
    return text


SMALL_TALK_HINTS = [
    "能听见吗",
    "还在吗",
    "没有其他问题",
    "拜拜",
    "谢谢",
]


def likely_question(line: str, max_len: int = 90) -> str | None:
    line = normalize(line)
    if not line:
        return None
    if len(line) > max_len:
        return None
    if any(h in line for h in SMALL_TALK_HINTS):
        return None

    for pat in QUESTION_PATTERNS:
        m = pat.match(line)
        if m:
            q = normalize(m.group(1))
            if len(q) >= 6 and len(q) <= max_len:
                return q

    # Fallback heuristics for question-like Chinese lines.
    hints = ["为什么", "怎么", "如何", "是否", "哪些", "区别", "优缺点", "介绍一下", "谈谈"]
    if any(h in line for h in hints) and len(line) >= 6:
        if not line.endswith(("?", "？")):
            return line + "？"
        return line

    return None


def extract_questions(text: str, max_len: int = 90) -> list[str]:
    seen: set[str] = set()
    out: list[str] = []
    for raw in text.splitlines():
        q = likely_question(raw, max_len=max_len)
        if not q:
            continue
        if q not in seen:
            seen.add(q)
            out.append(q)
    return out


def to_records(questions: list[str]) -> list[dict[str, str]]:
    records = []
    for i, q in enumerate(questions, start=1):
        records.append(
            {
                "id": f"Q{i:03d}",
                "question": q,
                "intent": "待标注",
                "source": "用户粘贴内容",
                "frequency": "待统计",
            }
        )
    return records


def main() -> None:
    parser = argparse.ArgumentParser(description="Extract interview question candidates from notes.")
    parser.add_argument("--input", required=True, help="Path to notes text file")
    parser.add_argument("--output", help="Output json path (default: <input>-questions.json)")
    parser.add_argument("--max-len", type=int, default=90, help="Maximum question length to keep")
    args = parser.parse_args()

    in_path = Path(args.input)
    text = in_path.read_text(encoding="utf-8")
    questions = extract_questions(text, max_len=args.max_len)
    payload = {
        "total": len(questions),
        "questions": to_records(questions),
    }

    out_path = Path(args.output) if args.output else in_path.with_name(f"{in_path.stem}-questions.json")
    out_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"Extracted {len(questions)} questions -> {out_path}")


if __name__ == "__main__":
    main()
