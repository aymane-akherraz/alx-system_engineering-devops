#!/usr/bin/python3
""" Api module """
import requests


def top_ten(subreddit):
    """ Prints the titles of the first 10 hot posts listed
        for a given subreddit
    """

    r = requests.get('https://www.reddit.com/r/{}/hot.json?limit=9'
                     .format(subreddit), allow_redirects=False)
    if r.status_code != 200:
        print(None)
        return

    [print(post['data']['title']) for post in r.json()['data']['children']]
