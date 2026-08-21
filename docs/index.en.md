# ChatCube

ChatCube is a ChatArch cube-workflow Python CLI package. Its public command surface is currently root-only: the root command exposes `--help`, `--version`, `--tree`, and `--tree-brief`; the scaffold sample command is not present.

## Install

```bash
pip install ChatCube
chatcube --help
chatcube --version
chatcube --tree
chatcube --tree-brief
```

## CLI Tree

`chatcube --tree` reads the current command tree from the live Click registry through the shared ChatStyle runtime:

```text
chatcube
├── --help  # Show this message and exit.
├── --version  # Show the version and exit.
├── --tree  # Print the registered CLI tree and exit.
└── --tree-brief  # Print the registered CLI tree without parameter signatures and exit.
```

`--tree` retains parameter signatures on command nodes by default. `--tree-brief` omits those signatures while keeping command nodes and descriptions. The canonical root name of the current root-only CLI is `chatcube`.

## Development

```bash
python -m pip install -e ".[dev,docs]"
python -m pytest -q
mkdocs build --strict
python -m build
```
