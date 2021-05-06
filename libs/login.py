from argparse import Namespace
from cmdLineArgs import argumentHandler
import requests
import requests.auth

class Login:

    def __init__(self)  ->  None:
        self.tokenURL: str = "https://www.reddit.com/api/v1/access_token"
        self.identifyURL: str = "https://oauth.reddit.com/api/v1/me"
        self.cmdLineArgs: Namespace = argumentHandler()

    def getToken(self)  ->  str:
        # Code from https://github.com/reddit-archive/reddit/wiki/OAuth2-Quick-Start-Example#first-steps
        client_auth = requests.auth.HTTPBasicAuth(
                username=self.cmdLineArgs.client_id[0],
                password=self.cmdLineArgs.client_secret[0]
            )
        post_data = {
                "grant_type": "password",
                "username": self.cmdLineArgs.username[0],
                "password": self.cmdLineArgs.password[0]
            }
        headers = {
                "User-Agent": "GameJamStoryGen/0.1 by {}".format(self.cmdLineArgs.username[0])
            }

        response = requests.post(
                url=self.tokenURL,
                auth=client_auth,
                data=post_data,
                headers=headers
            ).json()

        return response["access_token"]
