#!/usr/bin/python3
""" 0. How many subs? """
import requests


def number_of_subscribers(subreddit):
    """
    Query the Reddit API for the number

    Parameters:
    subreddit (str): The name of the subreddit to query.

    Returns:
    int: The number of subscribers
    """
    headers = {'User-Agent': 'custom'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        return 0
    return response.json()['data']['subscribers']
