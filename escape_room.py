import csv
import time

# Initialize global variables for player name, actions, and start time - this didn't work, until I made the variables global. I think this can be deleted

player_name = ""
actions = 0
start_time = 0

# define rooms and items and 

couch = {
    "name": "couch",
    "type": "furniture",
}

door_a = {
    "name": "door a",
    "type": "door",
}

key_a = {
    "name": "key for door a",
    "type": "key",
    "target": door_a,
}

piano = {
    "name": "piano",
    "type": "furniture",
}

queen_bed = {
    "name": "queen bed",
    "type": "furniture",
}

door_b = {
    "name": "door b",
    "type": "door",
}

key_b = {
    "name": "key for door b",
    "type": "key",
    "target": door_b,
}

door_c = {
    "name": "door c",
    "type": "door",
}

double_bed = {
    "name": "double bed",
    "type": "furniture",
}

dresser = {
    "name": "dresser",
    "type": "furniture",
}

key_c = {
    "name": "key for door c",
    "type": "key",
    "target": door_c,
}


dining_table = {
    "name": "dining table",
    "type": "furniture",
}

door_d = {
    "name": "door d",
    "type": "door",
}

key_d = {
    "name": "key for door d",
    "type": "key",
    "target": door_d,
}

game_room = {
    "name": "game room",
    "type": "room",
}

bedroom_1 = {
    "name": "bedroom 1",
    "type": "room",
}

bedroom_2 = {
    "name": "bedroom 2",
    "type": "room",
}

living_room = {
    "name": "living room",
    "type": "room",
}

outside = {
  "name": "outside"
}

all_rooms = [game_room, bedroom_1, bedroom_2, living_room, outside]

all_doors = [door_a, door_b, door_c, door_d]

# define which items/rooms are related

object_relations = {
    "game room": [couch, piano, door_a],
    "piano": [key_a],
    "door a": [game_room, bedroom_1],
    "bedroom 1": [queen_bed, door_a,door_b, door_c],
    "queen bed": [key_b],
    "bedroom 2": [double_bed,dresser,door_b],
    "double bed": [key_c],
    "dresser": [key_d],
    "living room": [door_c, dining_table, door_d],
    "outside": [door_d],
    "door b": [bedroom_1, bedroom_2],
    "door c": [bedroom_1, living_room],
    "door d": [living_room, outside]
}

# define game state. Do not directly change this dict. 
# Instead, when a new game starts, make a copy of this
# dict and use the copy to store gameplay state. This 
# way you can replay the game multiple times.

INIT_GAME_STATE = {
    "current_room": game_room,
    "keys_collected": [],
    "target_room": outside,
    #debugging
    #'target_room': bedroom_1,
}


def linebreak():
    """
    Print a line break
    """
    print("\n\n")


def start_game():
    global player_name
    player_name = input("Enter your name: ").strip()
    global start_time
    start_time = time.time()
    global actions
    actions = 0
    print("You wake up on a couch and find yourself in a strange house with no windows which you have never been to before. You don't remember why you are here and what had happened before. You feel some unknown danger is approaching and you must get out of the house, NOW!")
    play_room(game_state["current_room"])




def play_room(room):
    """
    Play a room. First check if the room being played is the target room.
    If it is, the game will end with success. Otherwise, let player either 
    explore (list all items in this room) or examine an item found here.
    """
    global actions
    game_state["current_room"] = room
    if game_state["current_room"] == game_state["target_room"]:
        duration = time.time() - start_time
        print("Congratulations",player_name,"you have escaped the room in", duration, "seconds. It took you " , actions, " actions!")
        update_leaderboard(player_name, duration, actions)
        break
    else:
        print("You are now in " + room["name"])
        intended_action = input("What would you like to do? Type 'explore' or 'examine' ").strip().lower()
        if intended_action == "explore":
            if "explored" not in room or room["explored"] == False:  # Check if the room has been explored
                explore_room(room)
                room["explored"] = True  # Set the room as explored
                actions += 1  # Increment actions counter
            else:
                print("You have already explored this room.")
                actions += 1  # Increment actions counter
            play_room(room)  # Restart the loop
        elif intended_action == "examine":
            if "explored" not in room or room["explored"] == False:
                print("You haven't explored the room yet to see what items are there to be examined.")
                actions += 1  # Increment actions counter
                play_room(room)
            else:
                examine_item(input("What would you like to examine? ").strip().lower())
        else:
            print("Not sure what you mean. Type 'explore' or 'examine'. ")
            play_room(room)
        linebreak()

def explore_room(room):
    """
    Explore a room. List all items belonging to this room.
    """
    global actions
    items = [i["name"] for i in object_relations[room["name"]]]
    print("You have decided to explore the room. This is " + room["name"] + ". You find " + ", ".join(items))
    actions += 1  # Increment actions counter
    room["explored"] = True  # Mark the room as explored

def get_next_room_of_door(door, current_room):
    """
    From object_relations, find the two rooms connected to the given door.
    Return the room that is not the current_room.
    """
    connected_rooms = object_relations[door["name"]]
    for room in connected_rooms:
        if(not current_room == room):
            return room

def examine_item(item_name):
    """
    Examine an item which can be a door or furniture.
    First make sure the intended item belongs to the current room.
    Then check if the item is a door. Tell player if key hasn't been 
    collected yet. Otherwise ask player if they want to go to the next
    room. If the item is not a door, then check if it contains keys.
    Collect the key if found and update the game state. At the end,
    play either the current or the next room depending on the game state
    to keep playing.
    """
    current_room = game_state["current_room"]
    next_room = ""
    output = None

    global actions
    
    for item in object_relations[current_room["name"]]:
        if(item["name"] == item_name):
            output = "You examine " + item_name + ". "
            if(item["type"] == "door"):
                have_key = False
                for key in game_state["keys_collected"]:
                    if(key["target"] == item):
                        have_key = True
                if(have_key):
                    output += "You unlock it with a key you have."
                    actions += 1  # Increment actions counter
                    next_room = get_next_room_of_door(item, current_room)
                else:
                    output += "It is locked but you don't have the key."
                    actions += 1  # Increment actions counter
            else:
                if(item["name"] in object_relations and len(object_relations[item["name"]])>0):
                    item_found = object_relations[item["name"]].pop()
                    game_state["keys_collected"].append(item_found)
                    output += "You find " + item_found["name"] + "."
                    actions += 1  # Increment actions counter
                else:
                    output += "There isn't anything interesting about it."
                    actions += 1  # Increment actions counter
            print(output)
            break

    if(output is None):
        print("The item you requested is not found in the current room.")
    
    if(next_room and input("Do you want to go to the next room? Enter 'yes' or 'no' ").strip().lower() == 'yes'):
        play_room(next_room)
    else:
        play_room(current_room)

def update_leaderboard(name, duration, actions):
    global leaderboard
    leaderboard.append({"name": name, "duration": duration, "actions": actions})
    leaderboard.sort(key=lambda x: x["duration"])  # Sort by duration

    # Write leaderboard to a CSV file
    with open('leaderboard.csv', mode='a', newline='') as file: #mode a is append, mode w is write (in this case to overwrite)
        fieldnames = ['Name', 'Actions', 'Duration']
        writer = csv.DictWriter(file, fieldnames=fieldnames)

        writer.writeheader()
        for entry in leaderboard:
            writer.writerow({'Name': entry['name'], 'Actions': entry['actions'], 'Duration': entry['duration']})

    print("Leaderboard updated and written to leaderboard.csv.")


game_state = INIT_GAME_STATE.copy()
leaderboard = []

start_game()

#yes and no don't really work
#use a key each time?
#explore is still pretty important
#Define action counter as a function and call on the function to increase count as opposed to doing it globally (like the linebreak function)

