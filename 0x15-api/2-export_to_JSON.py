#!/usr/bin/python3
"""exports to json"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    id = str(argv[1])
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(id)).json()
    name = user['username']
    tasks = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    dicta = {}
    tasklist = []
    for i in tasks:
        if i['userId'] == int(argv[1]):
            dictb = {}
            dictb["task"] = i['title']
            dictb["completed"] = i['completed']
            dictb["username"] = name
            tasklist.append(dictb)
    dicta[id] = tasklist
    with open("{}.json".format(id), 'w') as f:
        json.dump(dicta, f)
