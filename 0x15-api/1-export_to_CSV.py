#!/usr/bin/python3
"""exports data to CSV"""
import csv
import requests
from sys import argv


if __name__ == "__main__":
    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(argv[1])).json()
    name = user['username']
    tasks = requests.get('https://jsonplaceholder.typicode.com/todos').json()
    with open('{}.csv'.format(argv[1]), mode='w') as employees:
        for i in tasks:
            if i['userId'] == int(argv[1]):
                r = csv.writer(employees, delimiter=',', quotechar='"',
                               quoting=csv.QUOTE_ALL)
                r.writerow([str(argv[1]), name, i['completed'], i['title']])
