

def recommend_items(weather, event_types, available_items, backpack_limit=5):
    """
    Recommends the best items to pack in a backpack based on 
        weather and possible events.
    
    Author: Don
    Advanced technique: Dictionary manipulation and sorting with lambda functions
    
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
        
        if weather in item_props.get("useful_weather", []):
            score += 3

        for event in event_types:
            if event in item_props.get("useful_events", []):
                score += 2

        score += item_props.get("base_value", 0)
        
        # Store the calculated score
        item_scores[item_name] = score
    
    # Sort items by score 
    sorted_items = sorted(item_scores.items(), key=lambda x: x[1], reverse=True)
    
    # Select top items within backpack limit
    recommended_items = []
    for item_name, score in sorted_items:
        if len(recommended_items) < backpack_limit:
            recommended_items.append(item_name)
        else:
            break
            
    return recommended_items