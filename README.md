# Final-Project-Interim

# School101

## Overview of our game
**School101** is our completely made-up final project which is an easy, 
fun, yet simple game for young children to play in hopes to help them prepare
for the school day all on there own.  The player has to complete five school 
days by packing the right items for the day's weather and event. The goal is to 
stay healthy and in a good mood while making smart choices. 
Every day gives the player a few hints to help them decide what to bring. We 
wanted this to be friendly and immersive. 

## Running the program
This goes without explanation. The input required during the game is explained.
cd ~/path/to/Final-Project-Interim
python3 main.py

### Playing the game
The game runs for 5 days.
Each day, you'll be shown:
    The weather
    A random school event
    A list of available items
    A hint with a few items to consider (not full answers)
    Type a comma-separated list of items to pack.
    Based on what you packed, your stats will update.

You’ll see daily feedback about what you missed (if anything), 
your current health/mood, and your overall score.

### Repository files
| File                | Description                                 |
| ------------------- | ------------------------------------------- |
| `main.py`           | Runs the game loop and connects all logic   |
| `event_logic.py`    | Handles the consequences of event decisions |
| `recommendation.py` | Suggests helpful backpack items             |
| `score.py`          | Calculates the day’s performance scores     |
| `items.json`        | Stores data about item usefulness           |
| `README.md`         | Project overview and instructions           |

### Sources
We did not use any sources from the internet. Everything was made up by us.

# Attribution Table
| Function/Method          | Primary Author | Techniques Demonstrated          |
| ------------------------ | -------------- | ---------------------------------|
| `simulate_event_outcome` | Koen Glick     | `json.load`, `f-strings`         |
| `Player.get_stats`       | Koen Glick     | class definition                 |
| `Player.update_stat`     | Koen Glick     | conditional expression           |
| `display_hint_items`     | Don            | sequence unpacking               |
| `recommend_items`        | Don            | set operations,list comprehension|
| `evaluate_day`           | Ibrahim T.     | composition of two custom classes|
| `score_outfit`           | Ibrahim T.     | conditional expression           |
| `score_backpack`         | Ibrahim T.     | use of key= in `max()`           |

## Notes
We only had three students. Koen Glick(me) was responsible for the 
full integration, main game logic, testing, and structure of the program. 
Don and Ibrahim contributed their required functions. All parts were brought 
together and debugged for a working final version.