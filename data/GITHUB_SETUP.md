# GitHub Setup Guide (JSON Blueprint Repo)

This guide covers publishing and maintaining the Zürich mobility blueprint on GitHub so tools can consume it as a remote JSON source.

## 1) Repository Configuration

- Repository: `waitwhatco/cai-zurich-urbanmobility`
- Visibility: Private
- Default branch: `main`
- Data location: `data/`

## 2) Required Files

Ensure these are present:

- `data/zurich_mobility_system.json`
- `data/BLUEPRINT_README.md`
- `README.md`
- `LICENSE`

## 3) Commit and Push

From repo root:

```bash
git add data/zurich_mobility_system.json data/BLUEPRINT_README.md data/GITHUB_SETUP.md README.md LICENSE scripts/generate_blueprint.py
git commit -m "Add production Zürich mobility blueprint and documentation"
git push origin main
```

## 4) Get Raw JSON URL

After push, compute the raw URL with this format:

```text
https://raw.githubusercontent.com/<owner>/<repo>/<branch>/data/zurich_mobility_system.json
```

For this repository:

```text
https://raw.githubusercontent.com/waitwhatco/cai-zurich-urbanmobility/main/data/zurich_mobility_system.json
```

## 5) Maintenance Workflow

When updating data:

1. Edit generation logic in `scripts/generate_blueprint.py`.
2. Regenerate:
   - `python3 scripts/generate_blueprint.py`
3. Validate:
   - `python3 -m json.tool data/zurich_mobility_system.json > /dev/null`
4. Commit and push to `main`.

## 6) Troubleshooting

- JSON parse error:
  - Run `python3 -m json.tool data/zurich_mobility_system.json`.
- Missing node references:
  - Check `from` and `to` values against element labels.
- Unexpected values in visual layers:
  - Confirm numeric fields are not quoted.
