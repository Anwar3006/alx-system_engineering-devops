#!/usr/bin/python3
"""Exports to-do list information for a given employee ID to CSV format."""
import csv
import requests
import sys

if __name__ == "__main__":
    req_name = requests.get('https://jsonplaceholder.typicode.com/users/'
                            + sys.argv[1])
    req_tasks = requests.get('https://jsonplaceholder.typicode.com/todos?userId='
                            + sys.argv[1])

    res_name = req_name.json()['username']
    tasks = req_tasks.json()

    csv_list = []

    for task in tasks:
        new_list = [task["id"], res_name, task["completed"], task["title"]]
        csv_list.append(new_list)

    with open(f"{sys.argv[1]}.csv", "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerows(csv_list)
