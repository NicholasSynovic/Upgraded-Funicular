import pandas
import praw
from pandas import DataFrame
from praw import Reddit
from progress.spinner import MoonSpinner

from libs.cmdLineArgs import argumentHandler


class Scraper:
    def __init__(self) -> None:
        args = argumentHandler()

        self.subredditSet: list = [
            "WritingPrompts",
            "DirtyWritingPrompts",
            "ShortStories",
            "SimplePrompts",
            "Worldprompts",
            "worldbuilding",
            "fantasywriters",
        ]
        self.reddit: Reddit = praw.Reddit(
            client_id=args.client_id[0],
            client_secret=args.client_secret[0],
            user_agent="Upgraded-Funicular/0.1 by NicholasSynovic",
        )

        self.outfile = args.outfile[0]

        try:
            self.outDF = pandas.read_json(args.in_file[0])
        except TypeError:
            columnNames: list = ["Name", "Subreddit", "NSFW", "Author", "Title", "URL"]
            self.outDF: DataFrame = pandas.DataFrame(columns=columnNames)

    def scrapeData(self) -> DataFrame:
        subreddit: str
        for subreddit in self.subredditSet:
            with MoonSpinner(
                message=f"Getting the latest 1000 posts from {subreddit}... "
            ) as spinner:

                for post in self.reddit.subreddit(display_name=subreddit).new(
                    limit=None
                ):
                    if post.name in self.outDF.values:
                        break

                    data: dict = {}

                    data["Name"] = post.name
                    data["Subreddit"] = subreddit
                    data["NSFW"] = post.over_18
                    data["Author"] = post.author
                    data["Title"] = post.title
                    data["URL"] = post.url

                    self.outDF = self.outDF.append(data, ignore_index=True)

                    spinner.next()

        self.outDF.to_csv(self.outfile)
        return self.outDF


if __name__ == "__main__":
    scraper = Scraper()
    data = scraper.scrapeData()
