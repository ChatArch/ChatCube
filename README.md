<div align="center">
    <a href="https://pypi.python.org/pypi/ChatCube">
        <img src="https://img.shields.io/pypi/v/ChatCube.svg" alt="PyPI version" />
    </a>
    <a href="https://github.com/ChatArch/ChatCube/actions/workflows/ci.yml">
        <img src="https://github.com/ChatArch/ChatCube/actions/workflows/ci.yml/badge.svg" alt="Tests" />
    </a>
</div>

<div align="center">

[文档](https://arch.gh.wzhecnu.cn/ChatCube/) | [English](README.en.md) | [简体中文](README.md)
</div>

# ChatCube

ChatCube: ChatArch placeholder package for cube workflows.

## 快速开始

```bash
pip install ChatCube
chatcube --help
chatcube --version
chatcube --tree
chatcube --tree-brief
```

开发环境：

```bash
python -m pip install -e ".[dev,docs]"
python -m pytest -q
mkdocs build --strict
python -m build
```

## CLI 树

运行 `chatcube --tree` 可通过 ChatStyle 共享运行时从实际 Click 注册表回读当前命令树：

```text
chatcube
├── --help  # Show this message and exit.
├── --version  # Show the version and exit.
├── --tree  # Print the registered CLI tree and exit.
└── --tree-brief  # Print the registered CLI tree without parameter signatures and exit.
```

`--tree` 默认在命令节点中保留已注册的参数签名；`--tree-brief` 省略参数签名，但保留命令节点和描述。当前公开命令面是 root-only，因此实时输出只有规范根名 `chatcube` 及其根选项节点。

## CLI 规范

当前公开命令面是 root-only；没有保留脚手架示例命令。新的命令应优先使用：

- `CommandSchema` / `CommandField` 描述输入。
- `add_interactive_option()` 提供统一 `-i/-I`。
- `resolve_command_inputs()` 统一缺参补问、默认值、TTY 与校验。
- `add_tree_option()` 为顶层 Click 命令提供共享的 `--tree` / `--tree-brief` 回读。
- 默认生成 `config.py` 和 `chatenv.configs` entry point，使包可被 ChatEnv 发现；只有明确不需要 ChatEnv 接入时才使用 `--without-chatenv-provider`。

## 目录结构

- `src/`：包源码
- `tests/code-tests/`：代码测试和历史测试迁移
- `tests/cli-tests/`：真实 CLI 测试，doc-first
- `tests/mock-cli-tests/`：mock/fake CLI 测试，doc-first

## 开发说明

扩展脚手架前，先阅读 `DEVELOP.md` 和 `AGENTS.md`。
