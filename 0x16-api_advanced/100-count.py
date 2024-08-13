#!/usr/bin/python3

"""
Recursive function that queries the Reddit API
Parses the title of all hot articles and
prints a sorted count of given keywords
case insensitive, delimited by spaces
"""
import requests
import json

def count_words(subreddit, word_list, hot_list=[], after=None):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers, params={"after": after})

    if response.status_code == 200:
        data = response.json()
        children = data["data"]["children"]

        for child in children:
            title = child["data"]["title"]
            hot_list.extend(title.lower().split())

        after = data["data"]["after"]

        if after is not None:
            return count_words(subreddit, word_list, hot_list, after)
        else:
            word_count = {word: hot_list.count(word) for word in word_list}
            for word, count in sorted(word_count.items(),
                                      key=lambda x: x[1], reverse=True):
                if count > 0:
                    print(f"{word}: {count}")
    else:
        return None
