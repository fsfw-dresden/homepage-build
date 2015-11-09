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
        "--staging",
        default=False,
        action='store_true',
        help="Set the staging flag (this has to be handled by the template)."
    )

    parser.add_argument(
        "template",
        type=pathlib.Path,
        help="Template to render"
    )

    parser.add_argument(
        "output"
    )

    args = parser.parse_args()

    loader = jinja2.FileSystemLoader(str(args.base.resolve()))
    env = jinja2.Environment(loader=loader)
    env.globals["staging"] = args.staging

    tpl = env.get_template(str(args.template))
    with open(args.output, "w", encoding="utf-8") as f:
        f.write(tpl.render())
