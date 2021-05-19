#!/usr/bin/python3
import requests


def number_of_subscribers(subreddit):
    """gets number of subs from subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    r = requests.get(url, headers={'User-Agent': ''}, allow_redirects = 'false')

    if r.status_code != 200:
        return (0)

    return r.json()['data']['subscribers']
