#!/usr/bin/python3
"""
Script to query the Reddit API and return the number of subscribers.
"""

import requests


def number_of_subscribers(subreddit):
    """
    Query the Reddit API and return the number of subscribers for a subreddit.

    Args:
        subreddit (str): The subreddit to query.

    Returns:
        int: The number of subscribers, or 0 if the request fails.
    """
    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {"User-Agent": "My User Agent 1.0"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data.get('data', {}).get('subscribers', 0)
    else:
        return 0