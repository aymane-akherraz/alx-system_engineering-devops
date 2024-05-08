#!/usr/bin/python3
""" Api module """
import requests


def number_of_subscribers(subreddit):
    """ Returns the number of subscribers for a given subreddit """

    r = requests.get('https://www.reddit.com/r/{}/about.json'
                     .format(subreddit),
                     headers={"User-Agent": "My-Agent"},
                     allow_redirects=False)

    if r.status_code == 404:
        return 0

    res = r.json().get("data")
    return res.get("subscribers")
