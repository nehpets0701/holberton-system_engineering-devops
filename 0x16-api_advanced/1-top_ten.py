#!/usr/bin/python3
import requests


def top_ten(subreddit):
    """top ten posts"""
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    r = requests.get(url, headers={'User-Agent': ''}, params = {'limit': 10})

    if r.status_code != 200:
        return (0)

    for post in r.json()['data']['children']:
            print(post['data']['title'])

