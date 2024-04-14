#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# define rooms and items
import cv2

couch = {
    "name": "couch",
    "type": "furniture",
}

door_a = {
    "name": "door a",
    "type": "door",
}

door_b = {
    "name": "door b",
    "type": "door",
}

door_c = {
    "name": "door c",
    "type": "door",
}

door_d= {
    "name": "door d",
    "type": "door",
}
key_a = {
    "name": "key for door a",
    "type": "key",
    "target": door_a,
}

key_b = {
    "name": "key for door b",
    "type": "key",
    "target": door_b,
}

key_c = {
    "name": "key for door c",
    "type": "key",
    "target": door_c,
}
key_d = {
    "name": "key for door d",
    "type": "key",
    "target": door_d,
}
piano = {
    "name": "piano",
    "type": "furniture",
}

queen_bed = {
    "name": "queen bed",
    "type": "furniture",
}

double_bed = {
    "name": "double bed",
    "type": "furniture",
}

dresser = {
    "name": "dresser",
    "type": "furniture",
}

dinning_table = {
    "name": "dinning table",
    "type": "furniture",
}
game_room = {
    "name": "game room",
    "type": "room",
}

bedroom_1 = {
    "name": "bedroom 1",
    "type": "room"
}

bedroom_2 = {
    "name": "bedroom 2",
    "type": "room"
}
living_room = {
    "name": "living room",
    "type": "room"
}

outside = {
  "name": "outside"
}

all_rooms = [game_room, bedroom_1, bedroom_2,living_room, outside]

all_doors = [door_a, door_b, door_c, door_d]

# define which items/rooms are related

object_relations = {
    "game room": [couch, piano, door_a],
    "bedroom 1": [door_a, door_b, door_c, queen_bed],
    "piano": [key_a],
    "queen bed": [key_b],
    "double bed": [key_c],
    "dresser": [key_d],
    "outside": [door_d],
    "door a": [game_room, bedroom_1],
    "door b": [bedroom_1, bedroom_2],
    "door c": [bedroom_1, living_room],
    "door d": [living_room, outside],
    "bedroom 2": [dresser, double_bed,door_b],
    "living room": [door_d, dinning_table , door_c]
}

# define game state. Do not directly change this dict. 
# Instead, when a new game starts, make a copy of this
# dict and use the copy to store gameplay state. This 
# way you can replay the game multiple times.

INIT_GAME_STATE = {
    "current_room": game_room,
    "keys_collected": [],
    "target_room": outside
}


# In[ ]:


def linebreak():
    """
    Print a line break
    """
    print("\n\n")
    
def video ():
    video_path = "Presentation_Video.mp4"  
    cap = cv2.VideoCapture(video_path)
    print ("Press Q to exit the video.")
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        cv2.imshow('Video Frame', frame)

        if cv2.waitKey(25) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


def start_game():
    """
    Start the game
    """
    print("You wake up on a couch and find yourself in a strange house with no windows which you have never been to before. You don't remember why you are here and what had happened before. You feel some unknown danger is approaching and you must get out of the house, NOW!")
    play_room(game_state["current_room"])

def play_room(room):
    """
    Play a room. First check if the room being played is the target room.
    If it is, the game will end with success. Otherwise, let player either 
    explore (list all items in this room) or examine an item found here.
    """
    game_state["current_room"] = room
    if(game_state["current_room"] == game_state["target_room"]):
        print("Congrats! You escaped the room!")
    else:
        print("You are now in " + room["name"])
        intended_action = input("What would you like to do? Type 'explore' or 'examine' followed by item name?").strip()
        if intended_action == "explore":
            explore_room(room)
            play_room(room)
        # UPDATE: merging the examine from two steps into single input to make it easier
        elif intended_action.find("examine ")== 0:
            examine_item(intended_action[8:].strip())
        else:
            print("Not sure what you mean. Type 'explore' or 'examine' followed by item name.")
            play_room(room)
        linebreak()

def explore_room(room):
    """
    Explore a room. List all items belonging to this room.
    """
    # UPDATE: Checking to ensure object exists
    if room["name"] not in object_relations:
        print("Something wrong with the game settings! Do something!")
    
    items = [i["name"] for i in object_relations[room["name"]]]
    print("You explore the room. This is " + room["name"] + ". You find " + ", ".join(items))

def get_next_room_of_door(door, current_room):
    """
    From object_relations, find the two rooms connected to the given door.
    Return the room that is not the current_room.
    """
    
    # UPDATE: Checking to ensure object exists
    if door["name"] not in object_relations:
        # returning empty string to mark it as not found
        return ""
    
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
    
    #UPDATE: checking if room exists in the object relations
    if current_room["name"] not in object_relations:
        print("Game settings are wrong! Aborting")
        linebreak()
        return
    
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
                    next_room = get_next_room_of_door(item, current_room)
                else:
                    output += "It is locked but you don't have the key."
            else:
                if(item["name"] in object_relations and len(object_relations[item["name"]])>0):
                    item_found = object_relations[item["name"]].pop()
                    game_state["keys_collected"].append(item_found)
                    output += "You find " + item_found["name"] + "."
                else:
                    output += "There isn't anything interesting about it."
            print(output)
            break

    if(output is None):
        print("The item you requested is not found in the current room.")
    
    if(next_room and input("Do you want to go to the next room? Ener 'yes' or 'no'").strip() == 'yes'):
        play_room(next_room)
    else:
        play_room(current_room)


# In[ ]:


game_state = INIT_GAME_STATE.copy()

video()

start_game()

"""
IMPROVEMENTS
============

1. Merged the two steps needed for the 'examine' step, to be in single command,
   so instead of writing 'examine' first, and then in another input to type
   'piano', you can now type 'examine piano' which is easier for the player.

2. Added error checking to ensure object definitions are correct and the game
   will not crash because of bad game settings, like forgetting to add items 
   to object_relations, etc.
"""


# In[ ]:





# In[ ]:





# In[ ]:




