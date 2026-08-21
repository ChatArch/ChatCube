<div align="center">
    <a href="https://pypi.python.org/pypi/ChatCube">
        <img src="https://img.shields.io/pypi/v/ChatCube.svg" alt="PyPI version" />
    </a>
    <a href="https://github.com/ChatArch/ChatCube/actions/workflows/ci.yml">
        <img src="https://github.com/ChatArch/ChatCube/actions/workflows/ci.yml/badge.svg" alt="Tests" />
    </a>
</div>

<div align="center">

[Docs](https://arch.gh.wzhecnu.cn/ChatCube/en/) | [English](README.en.md) | [简体中文](README.md)
</div>

# ChatCube

ChatCube: ChatArch placeholder package for cube workflows.

## Quick Start

```bash
pip install ChatCube
chatcube --help
chatcube --version
chatcube --tree
chatcube --tree-brief
```

Development environment:

```bash
python -m pip install -e ".[dev,docs]"
python -m pytest -q
mkdocs build --strict
python -m build
```

## CLI Tree

Run `chatcube --tree` to read back the current command tree from the live Click registry through the shared ChatStyle runtime:

```text
chatcube
├── --help  # Show this message and exit.
├── --version  # Show the version and exit.
├── --tree  # Print the registered CLI tree and exit.
└── --tree-brief  # Print the registered CLI tree without parameter signatures and exit.
```

`--tree` keeps registered parameter signatures on command nodes by default. `--tree-brief` omits those signatures while retaining command nodes and descriptions. The current public surface is root-only, so its live output contains only the canonical `chatcube` root and its root-option nodes.

## CLI Contract

The current public command surface is root-only; the scaffold sample command is not present. New commands should prefer:

- `CommandSchema` / `CommandField` for inputs.
- `add_interactive_option()` for the shared `-i/-I` switch.
- `resolve_command_inputs()` for missing args, defaults, TTY behavior, and validation.
- `add_tree_option()` for shared `--tree` / `--tree-brief` readback on the top-level Click command.
- Generate `config.py` and a `chatenv.configs` entry point by default so the package is ChatEnv-discoverable; use `--without-chatenv-provider` only when ChatEnv integration is intentionally not needed.

## Layout

- `src/`: package source code
- `tests/code-tests/`: code tests and migrated historical tests
- `tests/cli-tests/`: real CLI tests, doc-first
- `tests/mock-cli-tests/`: mock/fake CLI tests, doc-first

## Development Notes

See `DEVELOP.md` and `AGENTS.md` before expanding the scaffold.
