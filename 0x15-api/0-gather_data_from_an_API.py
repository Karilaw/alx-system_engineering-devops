#!/usr/bin/python3
""" 0. Gather data from an API """
import requests
import sys


def get_employee_todo_progress(employee_id):
    """
    Given an employee ID, fetches the employee's TODO list progress
    from a REST API and prints it in a specific format.

    Args:
        employee_id (int): The ID of the employee.

    Returns:
        None
    """
    base_url = "https://jsonplaceholder.typicode.com/users/"
    user_url = "{}{}".format(base_url, employee_id)
    todos_url = "{}/{}/todos".format(base_url, employee_id)

    user_response = requests.get(user_url)
    todos_response = requests.get(todos_url)

    if user_response.status_code != 200:
        print('Error: Could not retrieve user information')
        sys.exit(1)

    if todos_response.status_code != 200:
        print('Error: Could not retrieve todos')
        sys.exit(1)

    user_data = user_response.json()
    todos_data = todos_response.json()

    total_tasks = len(todos_data)
    done_tasks = [task for task in todos_data if task.get('completed')]

    print("Employee {} is done with tasks({}/{}):".format(
        user_data.get('name'), len(done_tasks), total_tasks))

    for task in done_tasks:
        print("\t {}".format(task.get('title')))


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print('Usage: {} <employee_id>'.format(sys.argv[0]))
        sys.exit(1)

    employee_id = sys.argv[1]
    get_employee_todo_progress(employee_id)
