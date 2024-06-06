#!/usr/bin/python3
"""
A script that queries the Reddit API and returns the number of subscribers
"""
import requests


def number_of_subscribers(subreddit):
    """
    A method  that queries the Reddit API
    and returns the number of subscribers.
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    set_headers = {"User-Agent": "My User Agent 1.0"}

    """
    making the request.
    """
    res = requests.get(url, headers=set_headers)
    if res.status_code == 200:
        data = res.json()
        # Uncomment the next line to return the number of subscribers
        return data.get('data').get('subscribers')
    else:
        return 0  # Return 0 if the request was unsuccessful