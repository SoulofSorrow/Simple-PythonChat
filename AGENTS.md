# AGENTS.md

Instructions for AI coding agents working in this repository. Tool-agnostic;
`CLAUDE.md` imports this file.

## Project

Simple-PythonChat: minimal TLS chat. `backend.py` is a socket server that
relays every message to all other connected clients; `client_backend.py` is a
Tkinter client. Standard library only (`socket`, `ssl`, `threading`,
`logging`, `argparse`, `tkinter`). License GPL (`LICENSE.md`).

## Read first

| Area | Doc |
| --- | --- |
| Components, protocol, file map, known issues | `docs/architecture.md` |
| Doc index and change records | `docs/README.md` |

## Commands

```bash
python3 backend.py [--debug]   # server on localhost:12345, needs cert.pem + key.pem in the CWD
python3 client_backend.py      # Tkinter client, asks for server IP and nickname
python3 -m py_compile backend.py client_backend.py   # syntax check
```

No dependencies to install, no tests, no linter configuration, no build.

## Definition of done

- `python3 -m py_compile backend.py client_backend.py` passes.
- `docs/architecture.md` updated if behaviour changes.
- New file `docs/changes/YYYY-MM-DD-<slug>.md` (template in
  `.claude/skills/document-change/SKILL.md`), listed in `docs/README.md`.
- `README.md` updated for user-visible changes.

## Hard rules

- `key.pem` is a committed private key. Never print, copy or reuse it; never
  commit new keys or certificates.
- Server and client must agree on the port (`12345` in both files) and on
  UTF-8 text messages of at most 1024 bytes per `recv`.
- Do not push to `main` unless the user asks.
- No emojis in code, logs or docs.

## Language

| Artifact | Language |
| --- | --- |
| Code, log messages | English |
| Existing comments | German; write new ones in English |
| `README.md` | German (existing) |
| Commit messages, `docs/` | English |

## Project skills

| Skill | Use for |
| --- | --- |
| `document-change` | Writing the `docs/changes/` record |
