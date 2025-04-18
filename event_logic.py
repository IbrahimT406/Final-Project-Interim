"""
Simulate_event_outcome
Koen
"""

def simulate_event_outcome(event_type, backpack_items):
    """
    Checks if the player is prepared for the given event and returns a result.

    Parameters:
    Event_type (str): The type of school event (like "rainstorm" or "pop quiz").
    and
    Backpack_items (list): The list of items the player brought.

    Returns:
    A dict with a message and a mood or health change.
    """

    # From JSON later on
    if event_type == "rainstorm":
        required_items = ["umbrella", "raincoat"]
        stat_affected = "health"
    elif event_type == "pop quiz":
        required_items = ["notebook", "pencil"]
        stat_affected = "mood"
    elif event_type == "lost lunch":
        required_items = ["snack", "water"]
        stat_affected = "mood"
    elif event_type == "gym class":
        required_items = ["sneakers"]
        stat_affected = "health"
    else:
        raise ValueError("Unknown event type")

    # What is missing
    missing_items = []
    for item in required_items:
        if item not in backpack_items:
            missing_items.append(item)

    # Outcome
    if len(missing_items) == 0:
        message = f"You were ready for the {event_type}!"
        stat_change = 10
    else:
        message = f"You were missing: {', '.join(missing_items)} during the " \
          f"{event_type}."
        stat_change = -15

    return {
        "outcome": message,
        stat_affected: stat_change
    }
