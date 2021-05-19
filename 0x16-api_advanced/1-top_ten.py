#!/usr/bin/python3
"""gets top ten posts from subreddit"""
import requests


def top_ten(subreddit):
    """top ten posts"""
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    r = requests.get(url, headers={'User-Agent': ''}, params={'limit': 10})

    try:
        for post in r.json()['data']['children']:
            print(post['data']['title'])
    except Exception as e:
        print(None)
