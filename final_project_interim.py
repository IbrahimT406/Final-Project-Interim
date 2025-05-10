

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