#!/usr/bin/python3
""" Export to CSV """
import requests
import sys
import csv

def fetch_employee_todo_list(employee_id):
    """
    Fetch and export an employee's TODO list to a CSV file.

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

        employee_name = user_data["username"]
        user_id = user_data["id"]

        csv_file_name = f"{user_id}.csv"

        fieldnames = [
            "USER_ID", "USERNAME",
            "TASK_COMPLETED_STATUS", "TASK_TITLE"
        ]

        with open(csv_file_name, mode='w', newline='') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()

            for task in todos_data:
                writer.writerow({
                    "USER_ID": user_id,
                    "USERNAME": employee_name,
                    "TASK_COMPLETED_STATUS": str(task["completed"]),
                    "TASK_TITLE": task["title"]
                })

        print(f"Data exported to {csv_file_name}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    fetch_employee_todo_list(employee_id)
