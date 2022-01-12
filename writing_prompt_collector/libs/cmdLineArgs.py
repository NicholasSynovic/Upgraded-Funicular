import argparse
from argparse import Namespace


def argumentHandler() -> Namespace:
    parser = argparse.ArgumentParser(
        prog="Writng Prompt Collector (WPC)",
        usage="Collect and store writing prompts from Reddit subreddits"
        epilog="Created by Nicholas M. Synovic.",
    )

    parser.add_argument(
        "-c",
        "--client-id",
        nargs=1,
        type=str,
        required=True,
        help="""The Client ID for this application.
            Can be generated at https://www.reddit.com/prefs/apps""",
    )

    parser.add_argument(
        "-s",
        "--client-secret",
        nargs=1,
        type=str,
        required=True,
        help="""The Client Secret for this application.
            Can be generated at https://www.reddit.com/prefs/apps""",
    )

    parser.add_argument(
        "-i",
        "--input",
        nargs=1,
        type=str,
        required=False,
        default=None,
        help="""If specified, the content of this file is compared against the new scraped content.
            Must end in a .json format""",
    )

    parser.add_argument(
        "-o",
        "--output",
        nargs=1,
        type=str,
        required=True,
        help="""The outfile of where the scraped content will go.
            Must end in a .json format""",
    )

    return parser.parse_args()
