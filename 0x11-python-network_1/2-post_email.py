#!/usr/bin/python3
"""Python script that takes in a URL and an email,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response (decoded in utf-8)"""


if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys

    url_ = sys.argv[1]
    email_ = {'email': sys.argv[2]}
    email = urllib.parse.urlencode(email_)
    email = email.encode('ascii')
    url_req = urllib.request.Request(url_, email)

    with urllib.request.urlopen(url_req) as response:
        url_res = response.read()
    output = url_res.decode('utf-8')
    print(output)
