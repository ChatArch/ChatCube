"""CLI entrypoint for chatcube."""

import click

from chatcube import __version__


def render_cli_tree(command: click.Command) -> str:
    """Render the registered ChatCube Click command tree."""

    root_help = (command.help or "").strip().rstrip(".")
    root = command.name or "chatcube"
    lines = [f"{root}  # {root_help}."]
    synthetic = [
        ("--help", "Show this help message"),
        ("--version", "Show the installed package version"),
        ("--tree", "Print the registered command tree"),
    ]
    nodes: list[tuple[str, str]] = list(synthetic)
    if isinstance(command, click.Group):
        nodes.extend(
            (name, (cmd.short_help or cmd.help or "Run this command.").strip().rstrip("."))
            for name, cmd in command.commands.items()
            if not cmd.hidden
        )
    for index, (name, purpose) in enumerate(nodes):
        connector = "└──" if index == len(nodes) - 1 else "├──"
        lines.append(f"{connector} {name}  # {purpose}.")
    return "\n".join(lines)


def _print_tree(ctx: click.Context, _param: click.Option, value: bool) -> None:
    if not value or ctx.resilient_parsing:
        return
    click.echo(render_cli_tree(ctx.command))
    ctx.exit()


@click.group(name="chatcube")
@click.version_option(__version__, prog_name="chatcube")
@click.option("--tree", is_flag=True, is_eager=True, expose_value=False, callback=_print_tree, help="Print the registered command tree.")
def main() -> None:
    """ChatArch placeholder CLI for cube workflow packages."""


if __name__ == "__main__":
    main()
