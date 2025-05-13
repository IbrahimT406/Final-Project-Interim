""" 
Ibrahim
"""
def evaluate_outfit_score(weather, outfit):
    """ 
    Evaluates how appropriate a player's outfit is for the day based on the 
    weather, and if a player uses an accessory that is suitable for the weather, 
    they get a bonus. 
    
    Parameters:
    outfit (dict): Contains 'warmth', 'waterproof', and optional
    'accessories' (list).
    weather (dict): Contains 'temperature' (int) and 'condition' (str).
    
    Returns:
    An int that ranges from 0 to 100
    """
    score = 100
    temp = weather['temperature']
    condition = weather['condition']
    
    if temp < 40: 
        ideal_cloth_warmth = 9
    elif 40 <= temp < 60:
        ideal_cloth_warmth = 7
    elif 60 <= temp < 75:
        ideal_cloth_warmth = 5
    else:
        ideal_cloth_warmth = 3 
    
    actual_warmth = outfit.get('warmth', 5)
    warmth_gap = abs(ideal_cloth_warmth - actual_warmth)
    score -= warmth_gap * 5

    if condition == 'rainy' and not outfit.get('waterproof', False):
        score -= 20
    if condition == 'snowy' and not outfit.get('waterproof', False):
        score -= 20
    if condition == 'sunny' and actual_warmth > 6:
        score -= 10

    accessories = outfit.get('accessories', [])
    
    expected = {
        'rainy': 'umbrella',
        'sunny': 'sunglasses',
        'cold': 'hat'
    }

    """ 
    If a player uses an accessory that is appropriate for the weather, they are 
    given a bonus score and if not appropriate, they are slightly penalized.
    """
    if condition == 'rainy' and 'umbrella' in accessories:
        score += 5
    elif 'umbrella' in accessories:
        score -= 2  
    
    if condition == 'sunny' and 'sunglasses' in accessories:
        score += 5
    elif 'sunglasses' in accessories:
        score -= 2

    if temp < 40 and 'hat' in accessories:
        score += 5
    elif temp >= 70 and 'hat' in accessories:
        score -= 2  

    score = max(0, min(score, 100))
    
    return score

weather1 = {'temperature': 28, 'condition': 'snowy'}
outfit1 = {'warmth': 9, 'waterproof': True, 'accessories': ['hat']}
print("Test 1:", evaluate_outfit_score(weather1, outfit1)) 

weather1 = {'temperature': 75, 'condition': 'sunny'}
outfit1 = {'warmth': 5, 'waterproof': True, 'accessories': ['hat']}
print("Test 1:", evaluate_outfit_score(weather1, outfit1)) 



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
    

""" 
Don
"""
def recommend_backpack_items(forecast, possible_events, 
                             available_items, backpack_limit=5):
    """
    Recommends the best items to pack in a backpack based on weather 
        and possible events.
    
    Parameters:
    - forecast (str): The weather forecast for the day 
            (e.g., "rainy", "sunny")
    - possible_events (list): List of possible events that might occur 
            during the day
    - available_items (dict): Dictionary of items the player 
            can pack 
    - backpack_limit (int): Maximum number of items that can be packed in the
            backpack
    
    Returns:
    - list: Recommended items to pack for that particular day
    """
    # Calculate usefulness score for each item based on weather and events
    item_scores = {}
    
    for item_name, item_props in available_items.items():
        score = 0
        
        if forecast in item_props.get("useful_weather", []):
            score += 3

        for event in possible_events:
            if event in item_props.get("useful_events", []):
                score += 2

        score += item_props.get("base_value", 0)

        item_scores[item_name] = score

    sorted_items = sorted(item_scores.items(), key=lambda x: x[1], reverse=True)

    recommended_items = []
    for item_name, score in sorted_items:
        if len(recommended_items) < backpack_limit:
            recommended_items.append(item_name)
        else:
            break
            
    return recommended_items