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
    headers = {"User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"}

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Raises an HTTPError for bad responses (4xx or 5xx)
        data = response.json()

        # Check if the 'data' key exists and return the 'subscribers' count or 0
        return data.get('data', {}).get('subscribers', 0)

    except requests.RequestException as e:
        print(f"HTTP request failed: {e}")
        return 0  # Return 0 if the request failed

    except ValueError as e:
        print(f"JSON decoding failed: {e}")
        return 0  # Return 0 if JSON parsing failed
