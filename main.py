"""
School 101

A text-based simulation game where players pack for randomized
school days by considering the weather and events. The goal is to
keep mood and health as high as possible over five days.

Authors: Koen (I am responsible for most of main.py, we lost 
Yasmin so one of us had to step up to make it), Don, Ibrahim
"""

import random
import json
from event_logic import simulate_event_outcome
from recommendation import recommend_items
from score import evaluate_day

class Player:
    """
    Represents the player with mood, health, and backpack items.
    """

    def __init__(self):
        """Initializes the player's mood, health, and backpack."""
        self.mood = 100
        self.health = 100
        self.backpack = []

    def update_stat(self, stat_name, amount):
        """
        Updates the mood or health by the given amount.

        Parameters:
        stat_name (str): either "mood" or "health"
        amount (int): how much to adjust the stat
        """
        if stat_name == "mood":
            self.mood = max(0, min(100, self.mood + amount))
        elif stat_name == "health":
            self.health = max(0, min(100, self.health + amount))

    def set_backpack(self, items):
        """
        Sets the backpack contents to the given list.

        Parameters:
        items (list): items packed by the player
        """
        self.backpack = items

    def get_stats(self):
        """
        Returns the current mood and health in a formatted string.
        """
        return f"Mood: {self.mood}, Health: {self.health}"


player = Player()

with open("items.json", "r") as file:
    available_items = json.load(file)

weather_options = ["sunny", "rainy", "cloudy", "snowy"]
event_map = {
    "sunny": ["pop quiz", "lost lunch", "gym class"],
    "rainy": ["rainstorm", "pop quiz", "lost lunch"],
    "cloudy": ["pop quiz", "lost lunch"],
    "snowy": ["rainstorm", "lost lunch"]
}

print("Welcome to School 101!")
print("Your goal is to complete five school days while "
      "keeping your mood and health up. You got this :)\n")

# LOOP FUNCTION
for day in range(1, 6):
    print(f"\n*~* Day {day} *~*")

    weather = random.choice(weather_options)
    event = random.choice(event_map[weather])

    print(f"Today's weather: {weather}")
    print(f"Today's event: {event}")

    recommendations = recommend_items(weather, [event], available_items, 5)
    print(f"Available items to choose from: {', '.join(available_items.keys())}")
    print("Hint: Think about today’s weather and event.")
    print("Here are a few items to consider: " + 
          ", ".join(recommendations[:random.randint(2, 3)]))

    backpack_input = input("Pack your backpack (comma-separated items): ")
    backpack_items = [item.strip() for item in backpack_input.split(",")]
    player.set_backpack(backpack_items)

    result = simulate_event_outcome(event, player.backpack)
    print(result["outcome"])

    for stat in ["mood", "health"]:
        if stat in result:
            player.update_stat(stat, result[stat])
            
    outfit = {
        "warmth": 5,
        "waterproof": "umbrella" in backpack_items or 
                  "raincoat" in backpack_items,
        "accessories": [
            item for item in backpack_items 
            if item in ["umbrella", "sunglasses", "hat"]
        ]
    }

    weather_data = {
        "temperature": random.randint(30, 85),
        "condition": weather
    }

    score_result = evaluate_day(
        weather_data,
        [event],
        outfit,
        backpack_items,
        available_items
    )

    print(f"Outfit Score: {score_result['outfit_score']}, "
          f"Backpack Score: {score_result['backpack_score']}, "
          f"Overall Score: {score_result['overall_score']}")

    print(f"End of Day {day}: {player.get_stats()}")

# RESULTS AFTER 5 DAYS
print("\nUwU End of the Week UwU")
print(f"Final Stats: {player.get_stats()}")

if player.mood > 70 and player.health > 70:
    print("Way to go, kiddo! You finished the week like a champ!")
elif player.mood < 30 or player.health < 30:
    print("Rough week... rest up and try again next tomorrow.")
else:
    print("Not bad, keep your head up!")
