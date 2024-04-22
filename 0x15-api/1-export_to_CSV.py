#!/usr/bin/python3
"""
    Records all tasks that are owned by this employee
    and export it to a CSV file
"""

if __name__ == "__main__":
    import csv
    import requests
    from sys import argv

    user_id = argv[1]
    username = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(
                        user_id)).json().get('username')
    tasks = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}/todos'.format(user_id)
    ).json()

    fieldnames = ["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS", "TASK_TITLE"]
    events = []
    for task in tasks:
        my_dict = {}
        my_dict[fieldnames[0]] = user_id
        my_dict[fieldnames[1]] = username
        my_dict[fieldnames[2]] = task.get('completed')
        my_dict[fieldnames[3]] = task.get('title')
        events.append(my_dict)

    with open('{}.csv'.format(user_id), mode='w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames,
                                quoting=csv.QUOTE_ALL)

        for event in events:
            row = {field: event.get(field, '') for field in fieldnames}
            writer.writerow(row)
