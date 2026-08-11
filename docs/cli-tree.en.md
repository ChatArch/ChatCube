# CLI Tree

ChatCube's current public CLI surface is the root command option set. It has no business subcommands and does not expose the scaffold sample command.

```text
chatcube  # ChatArch placeholder CLI for cube workflow packages.
├── --help  # Show this help message.
├── --version  # Show the installed package version.
└── --tree  # Print the registered command tree.
```

## Verification commands

```bash
chatcube --version
chatcube --tree
```
