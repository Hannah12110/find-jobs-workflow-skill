# Safe Collection Policy (Xiaohongshu / Social Sources)

This skill uses a safety-first sourcing strategy for interview-prep signal collection.

## Goal

- Gather useful interview patterns with minimal account/platform risk.
- Prefer verifiable, user-provided sources over aggressive automation.

## Risk Tiers

1. Low risk (default, recommended)
- Public pages only.
- No login-required crawling.
- Low-frequency access with throttling and caching.
- Collect title/summary/question cues, then human-check.

2. Medium risk
- Semi-manual browsing with user session and explicit consent.
- Still avoid high-frequency requests and bulk page traversal.

3. High risk (disallowed by default)
- Automated login-state crawling.
- High-concurrency harvesting or deep pagination scraping.

## Default Runtime Rules

- Prefer user-pasted links first.
- If links are missing, ask user to paste links or text excerpts.
- If still insufficient, perform low-frequency public web search.
- Always label source confidence and recency in output.

## User-Facing Reminder Template

- 你可以直接粘贴小红书经验贴链接（或正文），我会帮你提炼高频面试题、考察意图和回答框架。
- 为降低账号风险，我默认走安全模式：公开低频采集 + 你提供链接优先。
