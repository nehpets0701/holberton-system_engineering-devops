#!/usr/bin/python3
"""api"""
import requests
from sys import argv

if __name__ == "__main__":
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(argv[1])).json()
    tasks = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    name = user['name']
    tasklist = []
    totaltasks = 0
    tasksdone = 0
    for i in tasks:
        if i['userId'] == int(argv[1]):
            totaltasks += 1
            if i['completed']:
                tasksdone += 1
                tasklist.append(i['title'])
    print("Employee {} is done with tasks({}/{}):"
          .format(name, tasksdone, totaltasks))
    for i in tasklist:
        print("\t {}".format(i))
