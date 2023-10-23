#!/usr/bin/python3
"""
    A script to export data in the JSON format
"""

import json
import requests
from sys import argv


def get_employee_tasks(employee_id):
    """
        Get the tasks of an employee
    """
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    employee = requests.get(user_url).json()
    tasks = requests.get(todos_url).json()

    return employee, tasks


if __name__ == "__main__":
    employee_id = argv[1] if len(argv) > 1 else "1"

    employee, tasks = get_employee_tasks(employee_id)

    user_id = employee.get("id")
    username = employee.get("username")

    task_list = [
        {
            "username": username,
            "task": task["title"],
            "completed": task["completed"]
        }
        for task in tasks
    ]

    user_tasks = {user_id: task_list}
    filename = "todo_all_employees.json"

    with open(filename, "w") as jsonfile:
        json.dump(user_tasks, jsonfile)
