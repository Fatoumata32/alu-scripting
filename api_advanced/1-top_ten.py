#!/usr/bin/python3
"""Function to print hot posts on a given Reddit subreddit."""
import requests


def top_ten(subreddit):
    """Print the titles of the 10 hottest posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "limit": 10
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    
    # Check for a 404 error
    if response.status_code == 404:
        print("None")
        return
    
    # Ensure response is JSON
    if response.headers.get("Content-Type") != "application/json":
        print("Error: Non-JSON response")
        return
    
    try:
        results = response.json().get("data")
        if results:
            [print(c.get("data").get("title")) for c in results.get("children")]
        else:
            print("None")
    except ValueError:
        print("Error: Could not parse JSON response")

