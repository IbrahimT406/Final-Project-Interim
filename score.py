def evaluate_outfit_score(weather, outfit):
    """ 
    Evaluates how appropriate a player's outfit is for the day based on the 
    weather, and if a player uses an accessory that is suitable for the weather, 
    they get a bonus. 
    
    Parameters:
    outfit (dict): Contains 'warmth', 'waterproof', and optional 'accessories' (list).
    weather (dict): Contains 'temperature' (int) and 'condition' (str).
    
    Returns:
    An int that ranges from 0 to 100
    """
    score = 100
    temp = weather['temperature']
    condition = weather['condition']
    
    """this deals with the ideal warmth based on the temperature of the day"""
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



def evaluate_backpack_score(weather, event_types, backpack_items, available_items):
    """ 
    Evaluates how well the player's backpack items align with the day's 
    weather and events.

    Parameters:
    - weather (str): The weather condition for the day (e.g., "rainy", "sunny").
    - event_types (list): List of potential events for the day.
    - backpack_items (list): List of items packed by the player.
    - available_items (dict): Dictionary of all possible items with their attributes.

    Returns:
    - int: A score ranging from 0 to 100.
    """
    score = 100

    """this section goes through the items in the backpack and gives 
    a score based on the items attribute
    """
    for item in backpack_items:
        if item not in available_items:
            continue

        item_props = available_items[item]
        item_score = item_props.get("base_value", 0)

        # Weather Check
        if weather in item_props.get("useful_weather", []):
            item_score += 3
        else:
            item_score -= 1  # Slight penalty for irrelevant items

        # Event Check
        for event in event_types:
            if event in item_props.get("useful_events", []):
                item_score += 2

        # Apply score for each item
        score += item_score

    # Penalty for missing key items
    essential_items = []
    
    # Determine essential items based on weather
    if weather == "rainy":
        essential_items.append("umbrella")
    if weather == "rainstorm":
        essential_items.append("umbrella")

    """this determines what items are essential based on the anticipated events"""
    for event in event_types:
        if event == "pop quiz":
            essential_items.append("calculator")
        elif event == "field trip":
            essential_items.append("water_bottle")
            essential_items.append("lunch")
        elif event == "lost lunch":
            essential_items.append("lunch")
            essential_items.append("water_bottle")
        elif event == "gym class":
            essential_items.append("water_bottle")

    """this ensures that the essential items are thoroughly accounted for """
    for essential_item in set(essential_items):
        if essential_item not in backpack_items:
            score -= 10

    """this makes sure that the score doesn't pass the limit of a 100"""
    score = max(0, min(score, 100))

    return score


available_items = {
    "umbrella": {
        "useful_weather": ["rainy", "snowy", "rainstorm"],
        "useful_events": ["field trip", "rainstorm"],
        "base_value": 1
    },
    "textbook": {
        "useful_weather": [],
        "useful_events": ["pop quiz", "study session"],
        "base_value": 2
    },
    "lunch": {
        "useful_weather": [],
        "useful_events": ["field trip", "lost lunch"],
        "base_value": 3
    },
    "calculator": {
        "useful_weather": [],
        "useful_events": ["pop quiz", "math class"],
        "base_value": 1
    },
    "water_bottle": {
        "useful_weather": ["sunny", "hot"],
        "useful_events": ["field trip", "gym class", "lost lunch"],
        "base_value": 2
    }
}

def evaluate_day(weather, events, outfit, backpack, available_items):
    """
    Evaluates both the outfit and the backpack scores for the day, as well as 
    the overall score for the day. 
    
    Parameters: 
    weather: dict - temperature(int) and condition(str)
    events: list - deals with the anticipated events for the day
    outfit: dict - includes data from the outfit function
    backpack: list - takes the list from the items in the backpack
    available_items: dict - takes account of the available items and their attributes 
    
    
    Returns:
    - dict: provides the individual scores and overall score.
    """
    
    outfit_score = evaluate_outfit_score(weather, outfit)
    backpack_score = evaluate_backpack_score(weather['condition'], events, backpack, available_items)
    overall_score = (outfit_score + backpack_score) // 2
    
    return {
        "outfit_score": outfit_score,
        "backpack_score": backpack_score,
        "overall_score": overall_score
    }
    
