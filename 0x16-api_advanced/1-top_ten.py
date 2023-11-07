#!/usr/bin/python3
""" Top Ten """
import requests


def top_ten(subreddit):
    """
    Query the Reddit API for the titles

    Parameters:
    subreddit (str): The name of the subreddit
    """
    headers = {'User-Agent': 'custom'}
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code != 200:
        print(None)
        return
    data = response.json()['data']['children']
    for post in data:
        print(post['data']['title'])
