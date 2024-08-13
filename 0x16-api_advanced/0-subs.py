#!/usr/bin/python3

"""
Queries the Reddit API and returns the
number of subscribers for a given subreddit
"""
import json
import requests

def number_of_subscribers(subreddit):
    """Query the number of subscribers to a subreddit."""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "MyUserAgent"}

    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0

    data = response.json().get("data", {})
    subscribers = data.get("subscribers", 0)
    return subscribers
