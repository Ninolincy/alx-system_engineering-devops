#!/usr/bin/python3

"""
function that queries the Reddit API and
prints the titles of the first 10 hot posts listed for a given subreddit.
"""
import requests

def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot.json"
    headers = {"UserAgent": "MyUserAgent"}

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code != 200:
        print(None)
        return

    data = response.json().get("data", {})
    children = data.get("children", [])
    top_posts = [(child["data"]["name"], child["data"]["title"],
                  child["data"]["ups"]) for child in children][:10]

    for post in top_posts:
        print(post[1])
