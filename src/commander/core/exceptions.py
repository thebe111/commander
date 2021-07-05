import sys


class CustomException(Exception):
    def __init__(self, msg: str):
        super().__init__(f"custom message here")


def exceptions_resolver(instance):
    if "message" in instance:
        return sys.exit(f"Commander: {instance.message}")
    else:
        return sys.exit(f"Commander: {instance}")
