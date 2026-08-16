#!/usr/bin/python3
"""Fetches status using the requests package."""
import requests


if __name__ == "__main__":
    try:
        r = requests.get("https://alx-intranet.hbtn.io/status")
    except Exception:
        r = requests.get("https://intranet.hbtn.io/status")

    print("Body response:")
    print("\t- type: {}".format(type(r.text)))
    print("\t- content: {}".format(r.text))
