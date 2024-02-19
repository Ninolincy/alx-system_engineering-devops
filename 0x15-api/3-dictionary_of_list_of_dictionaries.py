#!/usr/bin/python3
"""Accessing a REST API for todos lists of employees"""

import requests
import sys
import json


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users"
    response = requests.get(url)
    users = response.json()

    dict = {}
    for user in users:
        userId = user.get("id")
        username = user.get("username")
        url = "https://jsonplaceholder.typicode.com/users/{}".format(userId)
        url = url + "/todos"

        response = requests.get(url)
        tasks = response.json()
        dict[userId] = []
        for task in tasks:
            dict[userId].append({"task": task.get("title"),
                                 "completed": task.get("completed"),
                                 "username": username})
        with open("todo_all_employees.json", 'w') as filename:
            json.dump(dict, filename)
