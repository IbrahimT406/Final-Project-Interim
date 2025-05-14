import os
import sys
import json
from argparse import ArgumentParser


def evaluate_outfit_score(weather, outfit, bonus=0):
    """ 
    Evaluates how appropriate a player's outfit is for the day based on the 
    weather, and if a player uses an accessory that is suitable for the weather, 
    they get a bonus. 
    
    Parameters:
    - outfit (dict): Contains 'warmth', 'waterproof', and optional 'accessories' (list).
    - weather (dict): Contains 'temperature' (int) and 'condition' (str).
    - bonus (int, optional): Additional score to be added based on other criteria. Default is 0.
    
    Returns:
    - int: A score ranging from 0 to 100.
    """
    score = 100
    temp = weather['temperature']
    condition = weather['condition']

    # Conditional Expression for warmth determination
    ideal_cloth_warmth = 9 if temp < 40 else 7 if temp < 60 else 5 if temp < 75 else 3
    actual_warmth = outfit.get('warmth', 5)
    warmth_gap = abs(ideal_cloth_warmth - actual_warmth)
    score -= warmth_gap * 5

    # Debugging statement using f-string with expressions
    print(f"Warmth gap: {warmth_gap}, Initial Score: {score}")

    if condition in ['rainy', 'snowy'] and not outfit.get('waterproof', False):
        score -= 20
    if condition == 'sunny' and actual_warmth > 6:
        score -= 10

    accessories = outfit.get('accessories', [])
    
    # Accessory Bonus Calculation using Comprehension
    expected = {
        'rainy': 'umbrella',
        'sunny': 'sunglasses',
        'cold': 'hat'
    }
    
    accessory_bonus = sum(
        5 if (a == expected.get(condition, '')) else -2 for a in accessories
    )
    score += accessory_bonus

    # Apply bonus parameter
    score = max(0, min(score + bonus, 100))

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

    # Set operation to handle essential items
    essential_items = set()

    # Weather-based essential items
    if weather == "rainy":
        essential_items.add("umbrella")
    if weather == "rainstorm":
        essential_items.add("umbrella")

    # Event-based essential items
    event_essentials = {
        "pop quiz": {"calculator"},
        "field trip": {"water_bottle", "lunch"},
        "lost lunch": {"lunch", "water_bottle"},
        "gym class": {"water_bottle"}
    }

    # Use a set operation to collect all essential items
    for event in event_types:
        essential_items.update(event_essentials.get(event, set()))

    # Calculate missing essential items
    missing_items = essential_items - set(backpack_items)
    for item in missing_items:
        score -= 10

    # Evaluate each item in the backpack using comprehension
    score += sum(
        available_items[item].get("base_value", 0) + 
        (3 if weather in available_items[item].get("useful_weather", []) else -1) + 
        sum(2 for event in event_types if event in available_items[item].get("useful_events", []))
        for item in backpack_items if item in available_items
    )

    # Ensure the score is within the range
    score = max(0, min(score, 100))

    return score


def evaluate_day(weather, events, outfit, backpack, available_items):
    """
    Evaluates both the outfit and the backpack scores for the day, as well as 
    the overall score for the day. 
    
    Parameters: 
    - weather: dict - temperature(int) and condition(str)
    - events: list - anticipated events for the day
    - outfit: dict - includes data from the outfit function
    - backpack: list - items packed in the backpack
    - available_items: dict - available items and their attributes
    
    Returns:
    - dict: Provides the individual scores and overall score.
    """
    outfit_score = evaluate_outfit_score(weather, outfit, bonus=5)
    backpack_score = evaluate_backpack_score(weather['condition'], events, backpack, available_items)
    overall_score = (outfit_score + backpack_score) // 2
    
    # F-string with expression for debugging
    print(f"Outfit Score: {outfit_score}, Backpack Score: {backpack_score}, Overall Score: {overall_score}")

    return {
        "outfit_score": outfit_score,
        "backpack_score": backpack_score,
        "overall_score": overall_score
    }


# Example available items dictionary
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
