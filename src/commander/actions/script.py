import os


def run(key: str) -> None:
    # TODO: read script file as json
    scripts = {}

    commands = scripts[key]

    [os.system(cmd) for cmd in commands]
