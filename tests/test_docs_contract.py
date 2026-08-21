from pathlib import Path


PUBLIC_DOCS = (
    "README.md",
    "README.en.md",
    "docs/index.md",
    "docs/index.en.md",
    "docs/cli-tree.md",
    "docs/cli-tree.en.md",
)


def test_mkdocs_material_bilingual_public_docs_contract():
    mkdocs = Path("mkdocs.yml").read_text(encoding="utf-8")
    pyproject = Path("pyproject.toml").read_text(encoding="utf-8")

    assert 'site_url: "https://arch.gh.wzhecnu.cn/ChatCube/"' in mkdocs
    assert "name: material" in mkdocs
    assert "mkdocs-static-i18n" in pyproject
    assert "pymdownx.emoji" in mkdocs
    assert "material.extensions.emoji.twemoji" in mkdocs
    assert "material.extensions.emoji.to_svg" in mkdocs
    assert "index.md" in mkdocs
    assert "cli-tree.md" in mkdocs
    assert Path("docs/index.en.md").exists()
    assert Path("docs/cli-tree.en.md").exists()

    assert 'Homepage = "https://arch.gh.wzhecnu.cn/ChatCube/"' in pyproject
    assert 'Documentation = "https://arch.gh.wzhecnu.cn/ChatCube/"' in pyproject
    assert 'Repository = "https://github.com/ChatArch/ChatCube"' in pyproject
    assert "chatstyle>=0.2.0,<0.3.0" in pyproject
    assert "chatenv>=0.2.10,<0.3.0" in pyproject


def test_public_docs_match_live_root_only_tree_and_no_material_literals():
    expected = [
        "chatcube",
        "├── --help  # Show this message and exit.",
        "├── --version  # Show the version and exit.",
        "├── --tree  # Print the registered CLI tree and exit.",
        "└── --tree-brief  # Print the registered CLI tree without parameter signatures and exit.",
    ]
    for rel in PUBLIC_DOCS:
        text = Path(rel).read_text(encoding="utf-8")
        assert ":material-" not in text, rel
        assert "sample-command" not in text.lower(), rel
        assert "ChatCube" in text, rel
        assert "--tree-brief" in text, rel
    for rel in PUBLIC_DOCS:
        if "cli-tree" in rel or rel.startswith("README"):
            text = Path(rel).read_text(encoding="utf-8")
            for line in expected:
                assert line in text, f"{rel} missing {line!r}"
