#!/usr/bin/python3
"""
    Function that queries the Reddit API and returns
    the number of subscribers for a given subreddit.
"""
import requests


def number_of_subscribers(subreddit):
    """ Returns number of subscribers from a subreddit"""
    u_agent = 'Mozilla/5.0'

    headers = {
        "User-Agent": u_agent
    }

    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)

    response = requests.get(url, headers=headers, allow_redirects=False)
    res_json = response.json()

    if response.status_code != 200:
        return 0

    if 'data' not in res_json:
        return 0

    if 'subscribers' not in res_json.get('data'):
        return 0

    data = res_json.get('data')

    subscribers = data['subscribers']

    return subscribers
