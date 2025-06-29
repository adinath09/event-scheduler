import json
from app import app

def test_create_event():
    client = app.test_client()
    response = client.post('/events', json={
        "title": "Test Event",
        "description": "This is a test event.",
        "start_time": "2025-07-01T09:00:00",
        "end_time": "2025-07-01T10:00:00"
    })
    assert response.status_code == 201
    data = json.loads(response.data)
    assert data['title'] == "Test Event"
