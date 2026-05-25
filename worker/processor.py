def process_event(event: dict):
    print("EVENT RECEIVED")

    print(event)

    event_type = event.get("event_type")
    user_id = event.get("user_id")

    print(f"event_type={event_type}")
    print(f"user_id={user_id}")
