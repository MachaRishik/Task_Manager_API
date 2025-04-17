# Task Manager API

A simple Task Manager web application using Flask (Python) and a basic frontend with HTML, CSS, and JavaScript. The backend is a RESTful API that allows users to add, update, delete, and view tasks. Tasks are stored in a local `tasks.json` file.

## Features
- Create, read, update, and delete tasks.
- Each task has a title, description, completion status, and timestamps (created_at and updated_at).
- Delete all tasks in one go.

## Technologies Used
- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Data Storage**: `tasks.json` file (JSON format)
- **CORS**: Enabled for cross-origin requests.

## Installation and Setup

### Prerequisites
- Python 3.x
- pip (Python package manager)

### Backend Setup
1. Clone the repository:
    ```bash
    git clone <repository-url>
    cd task-manager-api
    ```
2. Install dependencies:
    ```bash
    pip install flask flask-cors
    ```
3. Run the Flask app:
    ```bash
    python app.py
    ```
    This will start the API server at `http://127.0.0.1:5000`.

### Frontend Setup
1. Create a folder for your frontend and place the `index.html` file inside it.
2. Open the `index.html` file in your browser. The frontend will interact with the Flask API running on `http://127.0.0.1:5000`.

## API Endpoints

### `POST /tasks`
Creates a new task.
- **Body** (JSON):
    ```json
    {
        "title": "Task Title",
        "description": "Task Description"
    }
    ```
- **Response** (JSON):
    ```json
    {
        "id": "unique-task-id",
        "title": "Task Title",
        "description": "Task Description",
        "completed": false,
        "created_at": "2025-04-17T12:34:56",
        "updated_at": "2025-04-17T12:34:56"
    }
    ```

### `GET /tasks`
Fetches all tasks.
- **Response** (JSON):
    ```json
    [
        {
            "id": "unique-task-id",
            "title": "Task Title",
            "description": "Task Description",
            "completed": false,
            "created_at": "2025-04-17T12:34:56",
            "updated_at": "2025-04-17T12:34:56"
        }
    ]
    ```

### `PUT /tasks/{task_id}`
Updates an existing task.
- **Body** (JSON):
    ```json
    {
        "title": "Updated Task Title",
        "description": "Updated Task Description",
        "completed": true
    }
    ```

### `DELETE /tasks/{task_id}`
Deletes a specific task.

### `DELETE /tasks`
Deletes all tasks.

## Usage

- **Frontend**: The frontend allows users to interact with the Task Manager API. Users can add tasks, view tasks, toggle their completion status, and delete individual or all tasks.
- **Backend**: The backend handles the logic for managing tasks and storing them in a JSON file.

## Contributing

Feel free to fork the project and submit pull requests with improvements or fixes!

## License

This project is open-source and available under the MIT License.