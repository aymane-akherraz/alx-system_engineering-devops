#!/usr/bin/python3
""" Api module """
import requests


def top_ten(subreddit):
    """ Prints the titles of the first 10 hot posts listed
        for a given subreddit
    """

    r = requests.get('https://www.reddit.com/r/{}/hot.json?limit=10'
                     .format(subreddit), allow_redirects=False)
    if r.status_code == 404:
        print(None)

    else:
        posts = r.json().get('data')
        for post in posts.get('children')
            print(post.get('data').get('title'))
        


