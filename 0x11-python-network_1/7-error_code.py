#!/usr/bin/python3
"""sends a request to the URL and displays the body of the response."""

if __name__ == "__main__":
    import sys
    import requests

    response = requests.get(sys.argv[1])
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)
