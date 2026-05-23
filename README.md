# AESPD Deliverables

Advanced Systems Engineering – Proposal Development. Source for the
deliverables documentation site.

**Live site:** https://takhleeq-asepd.github.io/AdvancedSystemsEngineering-ProposalDevelopment/

**Deployment status:** https://github.com/Takhleeq-ASEPD/AdvancedSystemsEngineering-ProposalDevelopment/actions/workflows/deploy.yml — every push to `main` triggers a build here. Green check = live site is up to date with `main`; red X = the most recent push failed to deploy and the site still shows the previous version.

## What lives here

- `docs/` – the markdown content rendered as the public site
  - `stages/1-requirements/` through `stages/4-later-deliverables/`
  - `assets/images/`, `assets/diagrams/`, `assets/data/`
- `source/` – immutable reference: the original `.docx` the site was
  migrated from
- `mkdocs.yml` – site configuration (theme, nav, plugins)
- `CLAUDE.md` – conventions any AI assistant must follow when editing
- `.github/workflows/deploy.yml` – builds and publishes the site on push
  to `main`

## New editor? Start here

If you've never set this up before, follow [`SETUP.md`](SETUP.md). It
walks you through everything — installing VSCode, Python, Git, Claude
Code, cloning the repo, and making your first published edit. Takes
about 30 minutes.

## Local preview (once setup is complete)

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
mkdocs serve
```

Open `http://127.0.0.1:8000` — the site hot-reloads on every file save.

## Editing workflow

1. `git checkout main && git pull`
2. `git checkout -b edit/<short-description>` (one branch per editing
   session; not for review, just save-state)
3. Run `mkdocs serve` in one terminal, open Claude Code in another, edit
4. Commit to the branch as save points (`git add` + `git commit`)
5. When satisfied, publish: `git checkout main && git merge edit/<branch>
   && git push`
6. The GitHub Action deploys the site (~60 s)

The branch is the editor's private workspace; nothing reaches the public
site until the push to `main`.

## Conventions

See [`CLAUDE.md`](CLAUDE.md) for the file/naming conventions, comment
format, table tiers, and image/diagram rules. Both human editors and AI
assistants should follow it.
