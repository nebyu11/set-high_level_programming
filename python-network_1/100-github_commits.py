#!/usr/bin/python3
"""Lists the 10 most recent commits on a given GitHub repository."""
import sys
import requests


if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])
    r = requests.get(url)
    commits = r.json()
    if isinstance(commits, list):
        for commit in commits[:10]:
            print("{}: {}".format(
                commit.get("sha"),
                commit.get("commit").get("author").get("name")))
