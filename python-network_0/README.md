# Python - Network #0

This project introduces network programming basics in Bash and Python using `curl` and HTTP methods (GET, POST, DELETE, OPTIONS), status codes, request headers, JSON payloads, and an $O(\log n)$ peak finding algorithm.

## Tasks
- **0-body_size.sh**: Takes in a URL, sends a request, and displays the size of the body of the response in bytes.
- **1-body.sh**: Takes in a URL, sends a GET request, and displays the body of the response for 200 status code.
- **2-delete.sh**: Sends a DELETE request to the URL passed as the first argument and displays the body of the response.
- **3-methods.sh**: Takes in a URL and displays all HTTP methods the server will accept.
- **4-header.sh**: Sends a GET request to the URL with the header `X-School-User-Id: 98` and displays response body.
- **5-post_params.sh**: Sends a POST request with variables `email=test@gmail.com` and `subject=I will always be here for PLD`.
- **6-peak.py**: Python function that finds a peak in a list of unsorted integers with $O(\log n)$ complexity.
- **6-peak.txt**: Time complexity of the peak-finding algorithm.
- **100-status_code.sh**: Sends a request to a URL and displays only the HTTP status code of the response.
- **101-post_json.sh**: Sends a JSON POST request with contents of a file passed as the second argument.
- **102-catch_me.sh**: Makes a request to `0.0.0.0:5000/catch_me` causing the server to respond with `You got me!`.
