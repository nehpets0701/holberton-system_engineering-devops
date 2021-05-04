#!/usr/bin/python3
"""json"""
import json
import requests


if __name__ == "__main__":
    users = requests.get('https://jsonplaceholder.typicode.com/users').json()
    tasks = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    dicta = {}
    for user in users:
        tasklist = []
        for task in tasks:
            if task['userId'] == user['id']:
                dictb = {}
                dictb["task"] = task['title']
                dictb["completed"] = task['completed']
                dictb["username"] = user['username']
                tasklist.append(dictb)
        dicta[user['id']] = tasklist
    with open("todo_all_employees.json", 'w') as f:
        json.dump(dicta, f)
