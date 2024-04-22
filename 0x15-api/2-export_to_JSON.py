#!/usr/bin/python3
"""
    Records all tasks that are owned by this employee
    and export it to a json file
"""
if __name__ == "__main__":
    import json
    import requests
    from sys import argv

    user_id = argv[1]
    username = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(
                        user_id)).json().get('username')
    tasks = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'.format(user_id)
    ).json()

    employee = {}
    task_info = []
    for task in tasks:
        my_dict = {}
        my_dict["task"] = task.get('title')
        my_dict["completed"] = task.get('completed')
        my_dict["username"] = username
        task_info.append(my_dict)

    employee["{}".format(user_id)] = task_info

    with open('{}.json'.format(user_id), mode='w') as jsonf:
        json.dump(employee, jsonf)
