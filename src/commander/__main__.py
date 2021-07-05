import getopt
import sys
from __version__ import __version__

from actions import init, script
from core import help
from core.exceptions import exceptions_resolver as eresolver


def main(argv):
    try:
        opts, args = getopt.getopt(
            argv, "i:x:hv", ["init", "execute", "help", "version"]
        )
    except getopt.GetoptError:
        sys.exit(help.MESSAGE)

    for opt, arg in opts:
        try:
            if opt == "-h" or opt == "--help":
                sys.exit(help.MESSAGE)
            elif opt == "-v" or opt == "--version":
                sys.exit(__version__)
            elif opt == "-i" or opt == "--init":
                init.run(arg)
            elif opt == "-x" or opt == "--execute":
                script.run(arg)
        except Exception as e:
            eresolver(e)


if __name__ == "__main__":
    main(sys.argv[1:])
