# ChatCube

ChatCube 是 ChatArch 的 cube workflow Python CLI 包。当前公开命令面是 root-only：根命令提供 `--help`、`--version`、`--tree`，没有保留脚手架示例命令。

## 安装

```bash
pip install ChatCube
chatcube --help
chatcube --version
chatcube --tree
```

## CLI 树

`chatcube --tree` 从真实 Click 注册表回读当前命令树：

```text
chatcube  # ChatArch placeholder CLI for cube workflow packages.
├── --help  # Show this help message.
├── --version  # Show the installed package version.
└── --tree  # Print the registered command tree.
```

## 开发

```bash
python -m pip install -e ".[dev,docs]"
python -m pytest -q
mkdocs build --strict
python -m build
```
