"""
show_open_food_trucks

Usage:
  show_open_food_trucks
  show_open_food_trucks [--limit=<number>]
  show_open_food_trucks -h | --help
  show_open_food_trucks --version

Options:
  -h --help                         Show this screen.
  --version                         Show version.
  --limit=<number>                  A number of items to display [default: 10].

Examples:
  show_open_food_trucks
"""
from inspect import getmembers, isclass
from docopt import docopt
from . import __version__ as VERSION


def main():
    """
    Read all options of commands with docopt
    http://docopt.org/
    """
    import commands
    options = docopt(__doc__, version=VERSION)

    for name, val in options.iteritems():
        _command_run(commands, options, name)
    else:
        _command_run(commands, options, 'foodtruck')

def _command_run(commands, options, name):
    if hasattr(commands, name):
        module = getattr(commands, name)
        commands = getmembers(module, isclass)
        command = [command[1] for command in commands if command[0] != 'Base'][0]
        command = command(options)
        command.run()