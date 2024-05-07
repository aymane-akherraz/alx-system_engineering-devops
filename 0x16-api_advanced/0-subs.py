#!/usr/bin/python3
""" Api module """
import requests


def number_of_subscribers(subreddit):
    """ Returns the number of subscribers for a given subreddit """

    r = requests.get('https://www.reddit.com/r/{}/about.json'
                     .format(subreddit), allow_redirects=False)
    if r.status_code == 404:
        return 0
    subscribers_count = r.json()
    return subscribers_count['data']['subscribers']
