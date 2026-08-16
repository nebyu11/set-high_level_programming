# Python - Network #1

This project covers network requests in Python using the `urllib` standard library and the third-party `requests` package. It covers HTTP GET and POST requests, inspecting response status codes and headers, interacting with JSON REST APIs, authentication with Basic Auth / GitHub API, and parsing GitHub repository commit histories.

## Tasks
- **0-hbtn_status.py**: Fetches `https://alx-intranet.hbtn.io/status` using `urllib` and displays body response details.
- **1-hbtn_header.py**: Sends a request to a URL using `urllib` and displays the `X-Request-Id` response header.
- **2-post_email.py**: Sends a POST request with an email parameter using `urllib`.
- **3-error_code.py**: Sends a request to a URL and displays the response body or prints `Error code: <HTTP status code>` on `HTTPError`.
- **4-hbtn_status.py**: Fetches `https://alx-intranet.hbtn.io/status` using the `requests` package.
- **5-hbtn_header.py**: Sends a request to a URL using `requests` and displays the `X-Request-Id` response header.
- **6-post_email.py**: Sends a POST request with an email parameter using `requests`.
- **7-error_code.py**: Sends a request using `requests` and displays error code if HTTP status code >= 400.
- **8-json_api.py**: Sends a POST request to `http://0.0.0.0:5000/search_user` with a search letter parameter and parses JSON output.
- **10-my_github.py**: Uses the GitHub API to authenticate with personal access tokens and display user ID.
- **100-github_commits.py**: Uses the GitHub API to list the 10 most recent commits of a specified repository.
