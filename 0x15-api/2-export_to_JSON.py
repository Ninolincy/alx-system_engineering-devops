#!/usr/bin/python3
"""Accessing a REST API for todos lists of employees"""

import requests
import sys
import json


if __name__ == "__main__":
    employeeId = sys.argv[1]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = baseUrl + "/" + employeeId

    response = requests.get(url)
    username = response.json().get('username')

    todourl = url + "/todos"
    response = requests.get(todourl)
    tasks = response.json()

    dict = {employeeId: []}
    for task in tasks:
        dict[employeeId].append({"task": task.get("title"),
                                 "completed": task.get("completed"),
                                 "username": username})

    with open("{}.json".format(employeeId), 'w') as filename:
        json.dump(dict, filename)
