@AGENTS.md

## Claude Code specifics

- `.claude/settings.json` allows the syntax check and denies reading
  `key.pem`.
- Run `python3 -m py_compile backend.py client_backend.py` before reporting a
  task as done.
