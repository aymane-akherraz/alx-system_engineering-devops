#!/usr/bin/python3
""" Api module """
import requests


def number_of_subscribers(subreddit):
    """ Returns the number of subscribers for a given subreddit """

    r = requests.get('https://www.reddit.com/r/{}/about.json'
                     .format(subreddit),
                     headers={"User-Agent": "My-User-Agent"},
                     allow_redirects=False)
    if r.status_code != 200:
        return 0

    return r.json().get("data").get("subscribers")
