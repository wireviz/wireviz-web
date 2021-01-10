import shlex
import subprocess

import click


@click.command(
    help="""A little release script.
    Cut a release and publish it.
    """
)
@click.option(
    "--bump",
    type=str,
    required=True,
    help="""
        The version label for bumping.\n
        Use either "major", "minor", "patch" or the version number.\n
        Will be passed to `poetry version {bump}`.""",
)
def start(bump: str):
    """
    Run the whole shebang.

    :param bump: The version bump identifier (major, minor, patch) or the version number.
    :return:
    """

    # Bump version.
    run(f"poetry version {bump}")

    # Get new version.
    version = run("poetry version --short").strip()

    # Commit version in "pyproject.toml".
    run(f'git commit pyproject.toml CHANGES.rst -m "Bump version to {version}"')

    # Tag repository.
    run(f"git tag {version}")

    # Push repository.
    run("git push")
    run("git push --tags")

    # Build wheels and publish to PyPI.
    run("poetry build")
    run("poetry publish")


def run(cmd, **kwargs) -> str:
    """
    Wrapper around ``subprocess.check_output()`` for conveniently running commands.

    :param cmd:    The command.
    :param kwargs: **kwargs will get passed through to ``subprocess.Popen()``.
    :return:       The content on stdout.
    """
    cmd = shlex.split(cmd)
    try:
        stdout = subprocess.check_output(cmd, **kwargs)
    except subprocess.CalledProcessError as ex:
        print(ex.stdout.decode("utf-8"))
        if ex.stderr:
            print(ex.stderr.decode("utf-8"))
        raise

    outcome = stdout.decode("utf-8")
    print(outcome)

    return outcome
