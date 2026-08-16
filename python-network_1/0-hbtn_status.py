#!/usr/bin/python3
"""Fetches status from intranet using urllib."""
import urllib.request


if __name__ == "__main__":
    try:
        req = urllib.request.Request("https://alx-intranet.hbtn.io/status")
        with urllib.request.urlopen(req) as response:
            body = response.read()
    except Exception:
        req = urllib.request.Request("https://intranet.hbtn.io/status")
        with urllib.request.urlopen(req) as response:
            body = response.read()

    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
    print("\t- utf8 content: {}".format(body.decode("utf-8")))
