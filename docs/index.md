# ChatCube

ChatCube 是 ChatArch 的 cube workflow Python CLI 包。当前公开命令面是 root-only：根命令提供 `--help`、`--version`、`--tree`、`--tree-brief`，没有保留脚手架示例命令。

## 安装

```bash
pip install ChatCube
chatcube --help
chatcube --version
chatcube --tree
chatcube --tree-brief
```

## CLI 树

`chatcube --tree` 通过 ChatStyle 共享运行时从真实 Click 注册表回读当前命令树：

```text
chatcube
├── --help  # Show this message and exit.
├── --version  # Show the version and exit.
├── --tree  # Print the registered CLI tree and exit.
└── --tree-brief  # Print the registered CLI tree without parameter signatures and exit.
```

`--tree` 默认保留命令节点的参数签名；`--tree-brief` 省略参数签名，但保留命令节点和描述。当前 root-only CLI 的规范根名是 `chatcube`。

## 开发

```bash
python -m pip install -e ".[dev,docs]"
python -m pytest -q
mkdocs build --strict
python -m build
```
