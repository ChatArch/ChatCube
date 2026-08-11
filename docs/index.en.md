# ChatCube

ChatCube is a ChatArch cube-workflow Python CLI package. Its public command surface is currently root-only: the root command exposes `--help`, `--version`, and `--tree`; the scaffold sample command is not present.

## Install

```bash
pip install ChatCube
chatcube --help
chatcube --version
chatcube --tree
```

## CLI Tree

`chatcube --tree` reads the current command tree from the live Click registry:

```text
chatcube  # ChatArch placeholder CLI for cube workflow packages.
├── --help  # Show this help message.
├── --version  # Show the installed package version.
└── --tree  # Print the registered command tree.
```

## Development

```bash
python -m pip install -e ".[dev,docs]"
python -m pytest -q
mkdocs build --strict
python -m build
```
