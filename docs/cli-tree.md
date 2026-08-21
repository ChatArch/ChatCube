# CLI 树

ChatCube 使用 `chatstyle.add_tree_option` 提供共享 Click 树回读。当前公开 CLI surface 是根命令参数集合，不包含业务二级命令，也不包含脚手架示例命令。

```text
chatcube
├── --help  # Show this message and exit.
├── --version  # Show the version and exit.
├── --tree  # Print the registered CLI tree and exit.
└── --tree-brief  # Print the registered CLI tree without parameter signatures and exit.
```

规范根名固定为 `chatcube`。`--tree` 默认在命令节点显示参数签名；`--tree-brief` 省略参数签名，同时保留命令节点及其描述。由于当前 CLI 是 root-only，两种模式都只显示根选项节点。

## 验证命令

```bash
chatcube --version
chatcube --tree
chatcube --tree-brief
```
