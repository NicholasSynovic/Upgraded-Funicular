import argparse
from argparse import Namespace


def argumentHandler() -> Namespace:
    parser = argparse.ArgumentParser(
        prog="Game Jame Story Gen Scraper",
        usage="A tool to scrape writing prompt forumns for ideas and to store them in a database.",
        epilog="Created by Nicholas M. Synovic.",
    )

    parser.add_argument(
        "-u",
        "--username",
        nargs=1,
        type=str,
        required=True,
        help="Your Reddit account's username",
    )

    parser.add_argument(
        "-p",
        "--password",
        nargs=1,
        type=str,
        required=True,
        help="Your Reddit account's password",
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

    return parser.parse_args()


if __name__ == "__main__":
    print(
        """This file is not meant to be ran as a standalone program.
    Please import this file into your application"""
    )
