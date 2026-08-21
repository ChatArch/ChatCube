# Changelog

## 0.1.3 - 2026-08-21

### Added
- Add `chatcube --tree-brief` for command-tree readback without parameter signatures.

### Changed
- Use ChatStyle's shared Click tree runtime for the canonical `chatcube` root, with signatures enabled by default for command nodes.
- Require `chatstyle>=0.2.0,<0.3.0` and `chatenv>=0.2.10,<0.3.0`.

## 0.1.2 - 2026-08-12

### Added
- Add ChatArch MkDocs Material bilingual documentation at `https://arch.gh.wzhecnu.cn/ChatCube/`.
- Add Preview Docs and Deploy Docs workflows for PR preview and production Pages publishing.
- Add docs and workflow contract tests for Material emoji rendering, root-only CLI tree docs, OIDC publishing guard, and installed CLI CI smoke.

### Changed
- Harden package publishing with a default-branch ancestry guard before OIDC PyPI publishing.
- Expand CI to Python 3.10 / 3.11 / 3.12 and smoke the installed `chatcube --version` and `chatcube --tree` entry points.
- Point package metadata homepage/documentation at the ChatArch docs domain.

## 0.1.1 - 2026-08-11

### Added
- Add runtime-generated `chatcube --tree` support backed by the registered Click command tree.
- Cover `--help`, `--tree`, version output, and scaffold sample command absence in CLI tests.
- Sync README and package metadata with the `0.1.1` patch release.

## 0.1.0 - 2026-07-08

### Added
- Publish the first ChatArch workflow-verified ChatCube release after the 0.0.1 PyPI placeholder.

## 0.0.1 - 2026-07-08

### Added
- Register the initial PyPI placeholder package.
