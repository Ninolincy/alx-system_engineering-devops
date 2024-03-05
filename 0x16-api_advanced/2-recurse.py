#!/usr/bin/python3
"""
queries the Reddit API and returns a list
containing the titles of all hot articles for a given subreddit
"""

import requests


def recurse(subreddit, hot_list=[]):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        children = data["data"]["children"]

        for child in children:
            title = child["data"]["title"]
            hot_list.append(title)

        after = data["data"]["after"]

        if after is not None:
            return recurse(subreddit, hot_list=hot_list)
        else:
            return hot_list
    else:
        return None
