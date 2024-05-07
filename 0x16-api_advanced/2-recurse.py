#!/usr/bin/python3
""" Api module """
import requests


def recurse(subreddit, hot_list=[], after="null"):
    """ Returns a list containing the titles of all
        hot articles for a given subreddit
    """

    r = requests.get('https://www.reddit.com/r/{}/hot.json?limit=100&after={}'
                     .format(subreddit, after), allow_redirects=False)
    if r.status_code != 200:
        return None
    if after is not None:
        after = r.json()['data']['after']
        for post in r.json()['data']['children']:
            hot_list.append(post['data']['title'])
        recurse(subreddit, hot_list, after)
    return hot_list
