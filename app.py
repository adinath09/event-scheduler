from flask import Flask, request, jsonify
from datetime import datetime, timedelta
import uuid
import json
import threading
import time
import os

app = Flask(__name__)

EVENTS_FILE = 'events.json'
events = []

# Load events from file if exists
def load_events():
    global events
    if os.path.exists(EVENTS_FILE):
        with open(EVENTS_FILE, 'r') as f:
            try:
                events = json.load(f)
                print(f"[INFO] Loaded {len(events)} events.")
            except json.JSONDecodeError:
                print("[WARNING] events.json is empty or invalid. Starting fresh.")
                events = []

# Save events to file
def save_events():
    print(f"[INFO] Saving {len(events)} events to {EVENTS_FILE}")
    with open(EVENTS_FILE, 'w') as f:
        json.dump(events, f, indent=4)

# Background thread for reminders
def reminder_thread():
    while True:
        now = datetime.now()
        for event in events:
            start = datetime.fromisoformat(event['start_time'])
            if 0 <= (start - now).total_seconds() <= 3600:
                print(f"Reminder: Event '{event['title']}' starts at {event['start_time']}")
        time.sleep(60)

@app.route('/events', methods=['POST'])
def create_event():
    data = request.json
    event = {
        'id': str(uuid.uuid4()),
        'title': data['title'],
        'description': data.get('description', ''),
        'start_time': data['start_time'],
        'end_time': data['end_time']
    }
    events.append(event)
    print("[INFO] Event created:", event)
    save_events()
    return jsonify(event), 201

@app.route('/events', methods=['GET'])
def get_events():
    sorted_events = sorted(events, key=lambda x: x['start_time'])
    return jsonify(sorted_events), 200

@app.route('/events/<event_id>', methods=['PUT'])
def update_event(event_id):
    data = request.json
    for event in events:
        if event['id'] == event_id:
            event['title'] = data.get('title', event['title'])
            event['description'] = data.get('description', event['description'])
            event['start_time'] = data.get('start_time', event['start_time'])
            event['end_time'] = data.get('end_time', event['end_time'])
            print(f"[INFO] Event updated: {event}")
            save_events()
            return jsonify(event), 200
    print(f"[ERROR] Event with ID {event_id} not found.")
    return jsonify({'error': 'Event not found'}), 404

@app.route('/events/<event_id>', methods=['DELETE'])
def delete_event(event_id):
    global events
    initial_len = len(events)
    events = [e for e in events if e['id'] != event_id]
    if len(events) < initial_len:
        print(f"[INFO] Event {event_id} deleted.")
    else:
        print(f"[WARNING] Tried to delete non-existent event {event_id}.")
    save_events()
    return jsonify({'message': 'Event deleted'}), 200

if __name__ == '__main__':
    load_events()
    threading.Thread(target=reminder_thread, daemon=True).start()
    app.run(debug=True)
