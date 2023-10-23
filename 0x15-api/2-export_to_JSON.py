#!/usr/bin/python3
""" Export to JSON """
import requests
import sys
import json


def fetch_employee_todo_list(employee_id):
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

        json_file_name = f"{user_id}.json"

        user_data_json = {
            user_id: [
                {
                    "task": task["title"],
                    "completed": task["completed"],
                    "username": employee_name
                }
                for task in todos_data
            ]
        }

        with open(json_file_name, 'w') as json_file:
            json.dump(user_data_json, json_file, indent=4)

        print(f"Data exported to {json_file_name}")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 script.py <employee_id>")
        sys.exit(1)

    employee_id = sys.argv[1]
    fetch_employee_todo_list(employee_id)
