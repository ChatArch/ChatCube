# CLI 树

ChatCube 的当前公开 CLI surface 是根命令参数集合，不包含业务二级命令，也不包含脚手架示例命令。

```text
chatcube  # ChatArch placeholder CLI for cube workflow packages.
├── --help  # Show this help message.
├── --version  # Show the installed package version.
└── --tree  # Print the registered command tree.
```

## 验证命令

```bash
chatcube --version
chatcube --tree
```
