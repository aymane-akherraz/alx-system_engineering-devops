#!/usr/bin/python3
"""
    Returns information about TODO list progress
    of a a given employee ID
"""

if __name__ == "__main__":
    import requests
    from sys import argv

    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'.format(
                            argv[1])).json()
    tasks = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}/todos".format(argv[1])
    ).json()
    done_tasks = [i.get("title") for i in tasks
                  if i.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):".format(user.get("name"),
          len(done_tasks), len(tasks)))
    for title in done_tasks:
        print("\t {}".format(title))
