# Documentation Index

Primary reader: AI coding agents. Human readers start with `README.md`.
Agent rules live in `AGENTS.md` in the repository root.

## Topic docs (current state)

| File | Purpose |
| --- | --- |
| `docs/architecture.md` | Server and client, protocol, file map, known issues |

## Change records

One file per change set in `docs/changes/`, named `YYYY-MM-DD-<short-slug>.md`.
Never rewrite an existing change file; add a new one.

| File | Purpose |
| --- | --- |
| `docs/changes/2026-11-25-ai-ready-docs.md` | Adds `docs/`, `AGENTS.md`, `CLAUDE.md` and the `document-change` skill |

## Maintenance rules

- Add, rename or remove a doc: update this index in the same change.
- Change behaviour: update `docs/architecture.md` in the same change.
- Every change set: add a file in `docs/changes/` and list it above.
