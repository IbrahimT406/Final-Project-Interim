from event_logic import simulate_event_outcome
# from outfit_logic import score_outfit  IBRAHIM
# from recommendation import recommend_items  DON

player_stats = {
    "mood": 100,
    "health": 100
}

print("Welcome to School 101!")
print("Your goal is to complete five school days while"
      "keeping your mood and health up.\n")

# THIS IS THE 5 DAY LOOP (WEEK DAYS)
for day in range(1, 6):
    print(f"\n--- Day {day} ---")

    # PLACEHOLDER Ask for event type
    event_type = input("Enter today's event (rainstorm, pop quiz, "
                       "lost lunch, gym class): ").strip()

    # PLACEHOLDER Ask for backpack items
    backpack_input = input("Enter backpack items (comma-separated): ")
    backpack_items = [item.strip() for item in backpack_input.split(",")]

    # PLACE HOLDER FOR DON'S FUNCTION (later) → recommend_items()
    # recommendations = recommend_items(weather, event_types, inventory, limit)
    # print(f"Recommended items: {recommendations}")

    # PLACEHOLDER FOR IBRAHIM'S FUNCTION (later) → score_outfit()
    # outfit_input = input("Enter outfit items (comma-separated): ")
    # outfit_items = [item.strip() for item in outfit_input.split(",")]
    # outfit_score = score_outfit(weather, temperature, outfit_items)
    # Apply outfit_score to health here

    # MY FUNCTION OF EVENT OUTCOME
    result = simulate_event_outcome(event_type, backpack_items)
    print(result["outcome"])

    # MOOD/ HEALTH/ STAT CHANGES !!STAY BETWEEN 0-100 !!
    for stat in ["mood", "health"]:
        if stat in result:
            player_stats[stat] += result[stat]
            player_stats[stat] = max(0, min(100, player_stats[stat]))
    # THIS SHOWS CURRENT PLAYER STATS
    print(
    f"Current Mood: {player_stats['mood']}, "
    f"Current Health: {player_stats['health']}"
)

# GAME END
print("\n--- End of the Week ---")
print(f"Final Mood: {player_stats['mood']}")
print(f"Final Health: {player_stats['health']}")

if player_stats['mood'] > 70 and player_stats['health'] > 70:
    print("Way to go, kiddo! You finished the week like a champ!")
else:
    print("Nice job, buddy. Let's sharpen your skills for next time, though!")
