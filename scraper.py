import pandas
import praw
from pandas import DataFrame
from praw import Reddit
from progress.spinner import MoonSpinner

from libs.cmdLineArgs import argumentHandler
from libs.login import Login


class Scraper:
    def __init__(self) -> None:
        args = argumentHandler()

        self.subredditSet: list = ["WritingPrompts", "DirtyWritingPrompts"]
        self.reddit: Reddit = praw.Reddit(
            client_id=args.client_id[0],
            client_secret=args.client_secret[0],
            user_agent="Game Jam Story Gen/0.1 by _Art1c_", 
        )

    def scrapeData(self) -> DataFrame:
        columnNames: list = ["Name", "Subreddit", "NSFW", "Author", "Title", "URL"]
        df: DataFrame = pandas.DataFrame(columns=columnNames)

        for subreddit in self.subredditSet:
            with MoonSpinner(message="Getting the latest 1000 posts from {}...".format(subreddit)) as spinner:
                
                for post in self.reddit.subreddit(display_name=subreddit).new(limit=None):
                    data: dict = {}

                    data["Name"] = post.name
                    data["Subreddit"] = subreddit
                    data["NSFW"] = post.over_18
                    data["Author"] = post.author
                    data["Title"] = post.title
                    data["URL"] = post.url

                    df = df.append(data, ignore_index=True)
                    
                    spinner.next()

        df.to_csv("temp.csv")
        return df


if __name__ == "__main__":
    scraper = Scraper()
    data = scraper.scrapeData()
