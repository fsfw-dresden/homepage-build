#!/usr/bin/python3
import pathlib

import jinja2


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-b",
        dest="base",
        type=pathlib.Path,
        default=pathlib.Path.cwd(),
        help="Base directory with respect to which paths are resolved. This"
        " defaults to the current working directory."
    )

    parser.add_argument(
        "template",
        type=pathlib.Path,
        help="Template to render"
    )

    parser.add_argument(
        "output",
        type=argparse.FileType("w"),
    )

    args = parser.parse_args()

    loader = jinja2.FileSystemLoader(str(args.base.resolve()))
    env = jinja2.Environment(loader=loader)

    tpl = env.get_template(str(args.template))
    with args.output as f:
        f.write(tpl.render())
