# To-Do API Integration Testing

This project contains a Python script to perform integration testing on a RESTful To-Do API using the `requests` library. The script tests the creation, updating, listing, and deletion of tasks through HTTP requests.

## Features

- **Create Task**: Sends a request to create a new task with unique content and user ID.
- **Update Task**: Updates the content and status of an existing task.
- **List Tasks**: Lists all tasks for a specific user.
- **Delete Task**: Deletes a task and verifies it's no longer retrievable.

## Project Structure

- `main.py`: Contains the test functions and utility functions to interact with the API.
- `requirements.txt`: Lists the Python packages required to run the tests (e.g., `requests`).

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/lokesh2108/todo-api-integration-testing.git
   cd todo-api-integration-testing
