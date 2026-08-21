# CLI Tree

ChatCube uses `chatstyle.add_tree_option` for shared Click tree readback. Its current public CLI surface is the root command option set. It has no business subcommands and does not expose the scaffold sample command.

```text
chatcube
├── --help  # Show this message and exit.
├── --version  # Show the version and exit.
├── --tree  # Print the registered CLI tree and exit.
└── --tree-brief  # Print the registered CLI tree without parameter signatures and exit.
```

The canonical root is fixed as `chatcube`. `--tree` shows parameter signatures on command nodes by default; `--tree-brief` omits those signatures while preserving command nodes and descriptions. Because the current CLI is root-only, both modes contain only root-option nodes.

## Verification commands

```bash
chatcube --version
chatcube --tree
chatcube --tree-brief
```
