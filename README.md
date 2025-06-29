

# 🗓️ Event Scheduler System

A RESTful API built using **Python 3.x** and **Flask** to manage events — allowing users to create, view, update, and delete events with persistent storage. Reminders for upcoming events are also supported.

---

## ✅ Features

- 📝 **Event Creation** – Add new events with title, description, start time, and end time.
- 📋 **Event Listing** – Retrieve all events sorted by start time (earliest first).
- ✏️ **Event Updating** – Update any detail of an existing event using its unique ID.
- ❌ **Event Deletion** – Delete an event by ID.
- 💾 **Persistent Storage** – Events are saved in a `events.json` file to retain data across sessions.
- ⏰ **Reminders** – The system displays reminders for events due in the next hour.
- 🧪 **Unit Tests** – Sample test cases included using Pytest.
- 📬 **Tested using Postman** – All endpoints tested and shared as a Postman collection.

---

## 🚀 Setup Instructions

### Prerequisites

- Python 3.6+
- pip (Python package installer)

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/event-scheduler-flask.git
cd event-scheduler-flask
````

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the Application

```bash
python app.py
```

The server will start on:

```
http://127.0.0.1:5000
```

---

## 📬 API Endpoints

| Method | Endpoint       | Description              |
| ------ | -------------- | ------------------------ |
| POST   | `/events`      | Create a new event       |
| GET    | `/events`      | Retrieve all events      |
| PUT    | `/events/<id>` | Update an existing event |
| DELETE | `/events/<id>` | Delete an event          |

---

## 🔄 Request/Response Example

### ➕ Create Event (POST `/events`)

**Request Body:**

```json
{
  "title": "Meeting with Team",
  "description": "Monthly review meeting",
  "start_time": "2025-07-01T10:00:00",
  "end_time": "2025-07-01T11:00:00"
}
```

**Response:**

```json
{
  "id": "3dbb9ad2-e137-410f-8f2d-9075878ebe63",
  "title": "Meeting with Team",
  "description": "Monthly review meeting",
  "start_time": "2025-07-01T10:00:00",
  "end_time": "2025-07-01T11:00:00"
}
```

---

## 🧪 Unit Testing

### Run all tests:

```bash
pytest
```

Tests are located inside the `tests/` folder.

---

## 🧰 Project Structure

```
event-scheduler/
├── app.py                               # Main Flask application
├── events.json                          # JSON file storing all events
├── requirements.txt                     # Project dependencies
├── README.md                            # Setup and usage instructions
├── event-scheduler.postman_collection.json  # Postman test collection
└── tests/
    └── test_app.py                      # Unit tests using pytest
```

---

## 📬 Postman Collection

A Postman collection is provided:
`events.json`

You can import it into Postman to test all the endpoints easily.

---

## 📌 Optional Features (Not Implemented Yet)

These are extra features that can be added:

* 🔁 Recurring events (daily, weekly, monthly)
* 📧 Email notifications for reminders
* 🔍 Search functionality (by title/description)

---

## 🧹 .gitignore

The following files/folders are excluded from version control:

```
__pycache__/
.pytest_cache/
*.pyc
.env
```

---

## 👤 Author

**Your Name**
📧 [adinathnage9739@gmail.com](mailto:adinathnage9739@gmail.com
🔗 [GitHub Profile](https://github.com/adinath09)

---

