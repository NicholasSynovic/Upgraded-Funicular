import praw
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

    def test(self)  ->  None:
        count: int = 0
        
        for subreddit in self.subredditSet:
            for submission in self.reddit.subreddit("writingprompts").new(limit=None):
                count += 1

        print(count)
Scraper().test()
