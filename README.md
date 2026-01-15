# FastAPI Issue Tracker API 🚀

A modern, high-performance RESTful API for tracking software issues and bugs. This project is built using **FastAPI**, leveraging Python's asynchronous capabilities and Pydantic's data validation for a robust developer experience.



## ✨ Features

* **Full CRUD Operations**: Create, Read, Update, and Delete issues seamlessly.
* **Asynchronous Database Support**: Optimized for high-concurrency environments.
* **Automatic Documentation**: Instant access to Swagger UI and ReDoc.
* **Strict Type Safety**: Powered by Pydantic models to ensure data integrity.
* **Environment Configuration**: Easy setup using environment variables for different deployment stages.

## 🛠 Tech Stack

| Technology | Purpose |
| :--- | :--- |
| **FastAPI** | Web framework for building APIs |
| **Pydantic** | Data validation and settings management |
| **SQLAlchemy** | SQL Toolkit and Object Relational Mapper (ORM) |
| **Uvicorn** | ASGI server for production and development |
| **SQLite/PostgreSQL** | Database storage (configurable) |

---

## 🚀 Getting Started

### Prerequisites

* Python 3.9+
* Virtual environment (recommended)

### Installation

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/ramithperera/fastapi-issue-tracker-api.git](https://github.com/ramithperera/fastapi-issue-tracker-api.git)
    cd fastapi-issue-tracker-api
    ```

2.  **Set up a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

### Running the API

Start the server using Uvicorn:

```bash
uvicorn app.main:app --reload
```
Start the server using FastAPI:

```bash
fastapi dev main.py
```

The API will be live at http://127.0.0.1:8000.

---

## 📖 API Documentation

### Once the application is running, you can explore the endpoints via:

- Interactive Swagger UI: http://127.0.0.1:8000/docs

- ReDoc: http://127.0.0.1:8000/redoc

### Common Endpoints
- `GET /issues` - Retrieve a list of all issues.

- `POST /issues` - Create a new issue.

- `GET /issues/{id}` - Get details for a specific issue.

- `PUT /issues/{id}` - Update an existing issue.

- `DELETE /issues/{id}` - Remove an issue from the tracker.


## 📁 Project Structure
```.
├── app/
│   ├── api/          # Route handlers and API endpoints
│   ├── core/         # Config, security, and global constants
│   ├── db/           # Database sessions and migrations
│   ├── models/       # Database schemas (SQLAlchemy)
│   ├── schemas/      # Pydantic models for request/response
│   └── main.py       # Application entry point
├── tests/            # Automated test suite
├── requirements.txt  # Project dependencies
└── README.md         # Project documentation
```

