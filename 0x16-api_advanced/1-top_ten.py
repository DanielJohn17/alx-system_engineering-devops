#!/usr/bin/python3
"""
Queries the Reddit API and returns
titles of hot 10 posts for a given subreddit
"""
import requests
import sys


def top_ten(subreddit):
    """Function to retrive titles of hot 10 posts in a subreddit """
    u_agent = 'Mozilla/5'

    headers = {
        'User-Agent': u_agent
    }

    params = {
        'limit': 10
    }

    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)
    response = requests.get(url,
                            headers=headers,
                            params=params,
                            allow_redirects=False)

    if response.status_code != 200:
        print("None")
        return

    res_json = response.json()
    hot_posts = res_json['data']['children']

    if len(hot_posts) == 0:
        print("None")
    else:
        for post in hot_posts:
            print(post['data']['title'])
