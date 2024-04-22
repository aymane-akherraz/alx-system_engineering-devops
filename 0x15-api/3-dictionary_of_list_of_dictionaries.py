#!/usr/bin/python3
""" Records all tasks from all employees """

if __name__ == "__main__":
    import json
    import requests

    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    todo = {}
    for user in users:
        tasks = requests.get(
            'https://jsonplaceholder.typicode.com/users/{}/todos'.format(
                user.get('id'))).json()
        task_info = []
        for task in tasks:
            my_dict = {}
            my_dict["username"] = user.get('username')
            my_dict["task"] = task.get('title')
            my_dict["completed"] = task.get('completed')
            task_info.append(my_dict)

        todo["{}".format(user.get('id'))] = task_info

    with open('todo_all_employees.json', mode='w') as jsonf:
        json.dump(todo, jsonf)
