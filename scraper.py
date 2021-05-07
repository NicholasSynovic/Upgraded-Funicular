import praw
import pandas
from pandas import DataFrame
from libs.cmdLineArgs import argumentHandler

class Scraper:

    def __init__(self)  ->  None:
        args = argumentHandler()
        
        self.subredditSet: list = ["WritingPrompts", "DirtyWritingPrompts"]
        self.reddit = praw.Reddit(
                client_id=args.client_id[0],
                client_secret=args.client_secret[0],
                user_agent="GameJamStoryGen/0.1 by {}".format(args.username[0])
            )

    def scrapeData(self)    ->  DataFrame:
        columnNames:list = ["Subreddit", "NSFW", "Author", "Title", "URL"]
        df: DataFrame = pandas.DataFrame(columns=columnNames)
        
        for subreddit in self.subredditSet:
            for post in self.reddit.subreddit(display_name=subreddit).new(limit=None):
                data: dict = {}
                
                data["Subreddit"] = subreddit
                data["NSFW"] = post.over_18
                data["Author"] = post.author
                data["Title"] = post.title
                data["URL"] = post.url
                
                df = df.append(data, ignore_index=True)

        df.to_csv("temp.csv")
        return df 

if __name__ == "__main__":
    scraper = Scraper()
    data = scraper.scrapeData()

