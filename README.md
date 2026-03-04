# interview-coaching-assistant

`interview-coaching-assistant` is a resume-first interview coaching skill.

It supports:

- Pre-interview prep
- Post-interview review
- Multi-interview aggregation
- Simulation feedback
- Safe-source collection mode for social interview notes (link-paste first)

## Repository Structure

- `SKILL.md`: main skill instructions
- `references/`: templates, schema, and examples
- `scripts/render_report.py`: JSON-to-report renderer
- `agents/`: helper agent prompt files

## Quick Start

```bash
python3 scripts/render_report.py --input references/examples/post-sample.json
```

## Safe Collection (Recommended)

- Prefer user-pasted Xiaohongshu links or copied post text.
- Avoid aggressive automated crawling.
- Use helper extractor:

```bash
python3 scripts/extract_questions_from_notes.py --input notes.txt
```

## GitHub Pages

This repo is configured with GitHub Actions to auto-deploy Pages from the root files.
The landing page is `index.html`.

### First-time setup (required)

If workflow fails with errors like `Get Pages site failed` or `HttpError: Not Found`, use branch-based Pages:

1. Open repository `Settings -> Pages`
2. In `Build and deployment`, set `Source` to `Deploy from a branch`
3. Select branch `gh-pages` and folder `/(root)`
4. Go back to `Actions` and re-run `Deploy GitHub Pages`

After this one-time setup, every push to `main` will auto-deploy to `gh-pages`.
