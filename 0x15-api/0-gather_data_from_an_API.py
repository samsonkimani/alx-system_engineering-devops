#!/usr/bin/python3
""" module - working with apis """
import requests
from sys import argv

if __name__ == "__main__":
    """ url for the rest api """
    base_url = 'https://jsonplaceholder.typicode.com'
    employee_url = '{}/users/{}'.format(base_url, argv[1])
    todo_url = '{}/todos/?userId={}'.format(base_url, argv[1])

    """ employee response"""
    employee_res = requests.get(employee_url)
    employee_data = employee_res.json()

    """ employees todo """
    todo_res = requests.get(todo_url)
    todo_data = todo_res.json()

    tasks_completed = sum(task['completed'] for task in todo_data)
    print("Employee {} is done with tasks({}/{}):".format(
        employee_data['name'], tasks_completed, len(todo_data)))
    for task in todo_data:
        if task['completed']:
            print('\t{}'.format(task['title']))
