#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    employeeId = sys.argv[0]
    baseUrl = "https://jsonplaceholder.typicode.com/users"
    url = baseUrl + "/" + employeeId

    response = requests.get(url)
    employeeName = response.json().get("username")
    todourl = url + "/todos"
    response = requests.get(todourl)
    tasks = response.json()
    completed = 0
    completed_tasks = []
    for task in tasks:
        if task.get("completed"):
            completed += 1
            completed_tasks.append(task.get("title"))

    print("Employee {} is done with tasks({}/{}):"
          .format(employeeName, completed, len(tasks)))

    for task in completed_tasks:
        print("\t {}".format(task))
