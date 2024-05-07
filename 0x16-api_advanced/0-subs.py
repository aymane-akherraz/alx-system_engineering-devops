#!/usr/bin/python3
""" Api module """
import requests


def number_of_subscribers(subreddit):
    """ Returns the number of subscribers for a given subreddit """

    if subreddit is None or not isinstance(subreddit, str):
        return 0

    r = requests.get('https://www.reddit.com/r/{}/about.json'
                     .format(subreddit),
                     headers={"User-Agent": "My-Agent"},
                     allow_redirects=False)

    if r.status_code == 200:
        try:
            return subscribers_count.json()["data"]["subscribers"]
        except Exception:
            return 0
    return 0
