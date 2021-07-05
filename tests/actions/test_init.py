import shutil
import tempfile
from pathlib import Path, PurePath

from src.commander.actions import init


def test_if_the_template_path_was_coming_from_the_local_template_scope():
    path = Path("/tmp/")

    template_path = init.define_template_path(path)

    assert template_path.match("_template/")


def test_if_the_template_path_was_coming_from_the_custom_template_scope():
    base = "/tmp/commander_test"
    _dir = Path(f"{base}/commander/template/")

    Path.mkdir(_dir, parents=True)

    template_path = init.define_template_path(_dir)

    shutil.rmtree(base)

    assert template_path.match("commander/template/")
