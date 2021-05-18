#!/usr/bin/python3
import requests
import time


def recurse(subreddit, hot_list=[], after="NULL"):
    """lists hot posts"""
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    r = requests.get(url, headers={'User-Agent': ''}, params={'after': after})

    if r.status_code != 200:
        return (None)

    for post in r.json()['data']['children']:
            hot_list.append(post['data']['title'])

    after = r.json()['data']['after']
    if after not in [None, 'None', 'NULL']:
        return recurse(subreddit, hot_list, after)
    return hot_list
