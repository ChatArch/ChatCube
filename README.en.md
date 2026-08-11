<div align="center">
    <a href="https://pypi.python.org/pypi/ChatCube">
        <img src="https://img.shields.io/pypi/v/ChatCube.svg" alt="PyPI version" />
    </a>
    <a href="https://github.com/ChatArch/ChatCube/actions/workflows/ci.yml">
        <img src="https://github.com/ChatArch/ChatCube/actions/workflows/ci.yml/badge.svg" alt="Tests" />
    </a>
</div>

<div align="center">

[English](README.en.md) | [简体中文](README.md)
</div>

# ChatCube

ChatCube: ChatArch placeholder package for cube workflows.

## Quick Start

```bash
pip install -e ".[dev]"
chatcube --help
chatcube --version
chatcube --tree
python -m pytest -q
python -m build
```


## CLI Tree

Run `chatcube --tree` to read back the current command tree from the live Click registry:

```text
chatcube  # ChatArch placeholder CLI for cube workflow packages.
├── --help  # Show this help message.
├── --version  # Show the installed package version.
└── --tree  # Print the registered command tree.
```

## CLI Contract

This template depends on `chatstyle>=0.1.0,<0.2.0` and `chatenv>=0.2.0,<0.3.0`. New commands should prefer:

- `CommandSchema` / `CommandField` for inputs.
- `add_interactive_option()` for the shared `-i/-I` switch.
- `resolve_command_inputs()` for missing args, defaults, TTY behavior, and validation.
- Generate `config.py` and a `chatenv.configs` entry point by default so the package is ChatEnv-discoverable; use `--without-chatenv-provider` only when ChatEnv integration is intentionally not needed.

## Layout

- `src/`: package source code
- `tests/code-tests/`: code tests and migrated historical tests
- `tests/cli-tests/`: real CLI tests, doc-first
- `tests/mock-cli-tests/`: mock/fake CLI tests, doc-first

## Development Notes

See `DEVELOP.md` and `AGENTS.md` before expanding the scaffold.
