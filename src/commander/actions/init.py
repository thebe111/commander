import shutil
from pathlib import Path, PurePath

import config


def create_setup_folder(cwd: Path) -> None:
    Path.mkdir(PurePath.joinpath(cwd, "commander"))
    # TODO: create file with project path


def define_template_path(cwd: Path) -> PurePath:
    local = Path(__file__).parent.parent.absolute()

    if cwd.match("commander/template/"):
        path = PurePath(cwd)
    else:
        path = PurePath.joinpath(local, "_template")

    return path


def run(directory: str) -> None:
    cwd = Path.cwd()

    create_setup_folder(cwd)

    template_path = define_template_path(cwd)
    dest = PurePath.joinpath(cwd, directory)

    shutil.copytree(
        template_path,
        dest,
        ignore=shutil.ignore_patterns(*config.templates_excludes),
    )
