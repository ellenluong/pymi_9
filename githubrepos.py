import requests
import json
import sys


def get_repos(usename):
    url = 'https://api.github.com/users/{}/repos'
    r = requests.get(url.format(usename))
    try:
        result = [i['name'] for i in r.json()]
        return result
    except TypeError:
        print('No existing usename')


def main():
    if len(sys.argv) > 1:
        usename = sys.argv[1]
        repos = get_repos(usename)
        print(repos)
    else:
        print('No usename provided')


if __name__ == "__main__":
    main()
