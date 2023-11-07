#!/usr/bin/python3
""" Recurse it! """
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively query the Reddit API

    Parameters:
    subreddit (str): The name of the subreddit to query.
    hot_list (list): A list to store
    after (str): The ID of the last post

    Returns:
    list: A list of the titles of the hot post.
    """
    headers = {'User-Agent': 'custom'}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    params = {'limit': 100, 'after': after}
    response = requests.get(
        url,
        headers=headers,
        params=params,
        allow_redirects=False
    )

    if response.status_code != 200:
        return None
    data = response.json()['data']
    for post in data['children']:
        hot_list.append(post['data']['title'])
    if data['after'] is not None:
        return recurse(subreddit, hot_list, data['after'])
    return hot_list
