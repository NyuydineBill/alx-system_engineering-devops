#!/usr/bin/python3
"""
Script to query a list of all hot posts on a given Reddit subreddit.
"""

import requests


def recurse(subreddit, hot_list=None, after="", count=0):
    """
    Recursively retrieves a list of titles of all hot posts
    on a given subreddit.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list, optional): List to store the post titles.
                                    Default is None, which initializes an empty list.
        after (str, optional): Token used for pagination. Default is an empty string.
        count (int, optional): Current count of retrieved posts. Default is 0.

    Returns:
        list: A list of post titles from the hot section of the subreddit.
              Returns None if the subreddit is not found.
    """
    if hot_list is None:
        hot_list = []

    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }

    try:
        response = requests.get(url, headers=headers, params=params, allow_redirects=False)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"HTTP request failed: {e}")
        return None

    results = response.json().get("data", {})
    after = results.get("after")
    count += results.get("dist", 0)

    for post in results.get("children", []):
        hot_list.append(post.get("data", {}).get("title"))

    if after:
        return recurse(subreddit, hot_list, after, count)

    return hot_list
