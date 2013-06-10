import argparse
from pkg_resources import EntryPoint as ep, iter_entry_points
import types

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(
    title="subcommands", description="", help="")


def find_tasks(mod="tasks"):
    entrypoints = list()

    print mod

    try:
        _temp = __import__(mod, globals(), locals(), ['*'], 0)

        print _temp

    except Exception as e:
        print e

    entrypoints = [str(ep(n, mod, (n, ))) for n, v
                   in _temp.__dict__.iteritems()
                   if isinstance(v, types.FunctionType)]

    print entrypoints

    return entrypoints


def register_subtasks(func):
    (subparsers.add_parser(
        func.__name__, description=func.__doc__)
        .set_defaults(func=func))

points = list(iter_entry_points('subcommander.tasks'))

for entry in points:
    try:
        register_subtasks(entry.load())
    except Exception as e:
        print 'Warning: could not load entry point %s (%s: %s)' % (
            entry.name, e.__class__.__name__, e)


def main():
    args = parser.parse_args()
    args.func(args)
