#!/usr/bin/python3
"""Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress.
Accept an integer as a parameter, which is the employee ID
"""
import requests
import sys

if __name__ == "__main__":
    """Making GET requests"""
    req_name = requests.get('https://jsonplaceholder.typicode.com/users/'
                            + sys.argv[1])
    req_tasks = requests.get('https://jsonplaceholder.typicode.com/todos?userId='
                            + sys.argv[1])

    res_name = req_name.json()['name']
    tasks = req_tasks.json()

    completed_tasks = 0
    total_tasks = 0
    completed_tasks_list = []

    for task_done in tasks:
        if task_done["completed"] is True:
            completed_tasks += 1
            total_tasks += 1
            completed_tasks_list.append(task_done)
        else:
            total_tasks += 1


    print("Employee {} is done with tasks"
        " ({}/{}):".format(res_name, completed_tasks, total_tasks))

    for task_done in completed_tasks_list:
        print("\t {}".format(task_done["title"]))
