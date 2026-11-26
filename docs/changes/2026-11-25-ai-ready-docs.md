---
date: 2026-11-25
type: docs
scope: docs, agent tooling
files: [AGENTS.md, CLAUDE.md, .claude/settings.json, .claude/skills/document-change/SKILL.md, docs/README.md, docs/architecture.md, docs/changes/2026-11-25-ai-ready-docs.md, README.md]
breaking: false
---
# Agent-ready documentation and project skills

## Context

- Two-file Python chat with only a German `README.md`; no docs or agent
  instructions.
- Goal: an agent understands server, client and protocol without guessing.

## Change

- `docs/README.md`: index and maintenance rules.
- `docs/architecture.md`: file map, server and client flow, protocol, known
  issues.
- `AGENTS.md`: tool-agnostic agent instructions.
- `CLAUDE.md`: imports `AGENTS.md`, Claude Code notes.
- `.claude/settings.json`: allows `python3 -m py_compile`, asks before
  `git push`, denies reading `key.pem` and `.env`.
- `.claude/skills/document-change/SKILL.md`: change record template.
- `README.md`: "Documentation" section.

## Decisions

- Docs sized to the repository: one topic doc, one skill.
- No additional skills: no recurring multi-step tasks in this codebase.

## Usage / Verification

```bash
python3 -m json.tool .claude/settings.json
python3 -m py_compile backend.py client_backend.py
```

## Follow-ups

- Committed secret, rotate: `key.pem` contains a private key (line 1). Remove
  it from the repository and its history and issue a new certificate.
- Missing standard files: `.editorconfig`, `Makefile` (build/test/tag
  targets), `CHANGELOG.md`, `CONTRIBUTING.md`, `.pre-commit-config.yaml`,
  `README.de.md` (the existing `README.md` is German), `.gitignore`.
  `LICENSE.md` exists (not `LICENSE`).
- `README.md` names non-existent scripts `EncryptedP2PServer.py` and
  `EncryptedP2PClient.py`.
- Client disables certificate verification (`ssl.CERT_NONE`); server binds
  `localhost` only.
