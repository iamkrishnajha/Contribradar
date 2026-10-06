import argparse
import json

from .core import scan_repo, render_report


def main():
    parser = argparse.ArgumentParser(
        prog="contribradar",
        description=(
            "Find and prioritize meaningful "
            "open-source contribution opportunities."
        ),
    )

    subparsers = parser.add_subparsers(
        dest="command",
        required=True,
    )

    scan_parser = subparsers.add_parser(
        "scan",
        help="Scan a local repository",
    )

    scan_parser.add_argument(
        "path",
        nargs="?",
        default=".",
        help="Path to the repository to scan",
    )

    scan_parser.add_argument(
        "--json",
        action="store_true",
        dest="as_json",
        help="Output machine-readable JSON",
    )

    args = parser.parse_args()

    if args.command == "scan":
        result = scan_repo(args.path)

        if args.as_json:
            print(json.dumps(result, indent=2))
        else:
            print(render_report(result))


if __name__ == "__main__":
    main()
