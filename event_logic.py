"""
Simulate_event_outcome
Author: Koen
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

    event_data = {
        "rainstorm": {
            "required": ["umbrella", "raincoat"],
            "stat": "health"
        },
        "pop quiz": {
            "required": ["notebook", "pencil"],
            "stat": "mood"
        },
        "lost lunch": {
            "required": ["snack", "water_bottle"],
            "stat": "mood"
        },
        "gym class": {
            "required": ["sneakers", "water_bottle"],
            "stat": "health"
        }
    }

    if event_type not in event_data:
        raise ValueError("Unknown event type")

    required_items = event_data[event_type]["required"]
    stat_affected = event_data[event_type]["stat"]

    # Determine missing items
    missing_items = [item for item in required_items if item not in backpack_items]

    if not missing_items:
        message = f"You were ready for the {event_type}!"
        stat_change = 10
    else:
        message = f"You were missing: {', '.join(missing_items)} during the {event_type}."
        stat_change = -15

    return {
        "outcome": message,
        stat_affected: stat_change
    }
