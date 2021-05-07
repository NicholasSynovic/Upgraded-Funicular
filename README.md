# Upgraded Funicular
> A *creative* name for a creative project!

## About
Upgraded Funicular (a really bad name I know) is an attempt at creating a web scraper to create a `.csv` file of writing prompts. These prompts at the moment come from several different subreddits!

In the future, I would like to make a webpage that randomly selects prompts from this file.

## Purpose
To allow for those in the creative spirit to start writing from a premade prompt! These prompts are great for short stories, poems, game jams, and other forms of authorship!

On a selfish note, these prompts give me something to base game-jam games off of.

As these prompts come from Reddit right now, there is no copyright or license associated with the prompt. Also, this program does collect the URL of the prompt. So please do contribute in the comments of the post (as long as it isn't locked).

This program does collect NSFW prompts as well. These prompts are listed as NSFW **only** if the Reddit API has a mark saying that they are 18+. I do not moderate or control the content that this program scrapes.

## How to Run

I am currently in the process of setting up GitHub actions to automatically generate a list of prompts daily. Until then, a Python command line tool is availible to generate the lists.

### To Run:

1. Download this project as a `.zip` file
2. Extract the `.zip` file somewhere convienant
3. Make sure that you have `Python 3.9+` installed!
4. In the extracted project folder run `pip install -r requirements.txt`
5. In the extracted project folder run `python3 scraper.py --help`

* This will give you the complete list of arguements needed to run the program. Just put them in the the command line and you'll be downloading the list in no time!
