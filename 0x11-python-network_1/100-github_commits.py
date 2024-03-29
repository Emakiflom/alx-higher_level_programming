#!/usr/bin/python3
"""Listing 10 commits in a repo"""

if __name__ == '__main__':
    import sys
    import requests

    url = 'https://api.github.com/repos/{}/{}/commits'.format(
        sys.argv[2], sys.argv[1])
    try:
        response = requests.get(url)
        res_dict = response.json()
        for i in range(0, 10):
            print("{}: {}".format(res_dict[i].get('sha'), res_dict[i].get(
                'commit').get('author').get('name')))
    except Exception:
        pass
