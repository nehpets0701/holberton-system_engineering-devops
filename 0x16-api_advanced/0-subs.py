#!/usr/bin/python3
import requests


def number_of_subscribers(subreddit):
    """gets number of subs from subreddit"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    r = requests.get(url,
                     headers={'User-Agent': 'Python:sub.counter:v0.1\
                     (by /u/01100100011011110111)'},
                     allow_redirects='false')

    try:
        return r.json()['data']['subscribers']
    except Exception as e:
        return 0
