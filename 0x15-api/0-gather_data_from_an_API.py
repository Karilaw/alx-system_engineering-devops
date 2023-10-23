#!/usr/bin/python3
""" 0. Gather data from an API """
import requests
import sys


def fetch_employee_todo_list(employee_id):
    """
    Fetch and display an employee's TODO list progress from the API.

    Args:
        employee_id (str): The ID of the employee.

    Returns:
        None
    """
    base_url = "https://jsonplaceholder.typicode.com"
    user_url = f"{base_url}/users/{employee_id}"
    todos_url = f"{base_url}/todos?userId={employee_id}"

    try:
        user_response = requests.get(user_url)
        todos_response = requests.get(todos_url)

        if not (user_response.ok and todos_response.ok):
            print("Error: Unable to fetch data from the API.")
            return

        user_data = user_response.json()
        todos_data = todos_response.json()

        employee_name = user_data["name"]
        completed_tasks = [task for task in todos_data if task["completed"]]
        total_tasks = len(todos_data)

        progress_message = (
            f"Employee {employee_name} is done with tasks "
            f"({len(completed_tasks)}/{total_tasks}):"
        )
        print(progress_message)

        for task in completed_tasks:
            print(f"    {task['title']}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    fetch_employee_todo_list(employee_id)
