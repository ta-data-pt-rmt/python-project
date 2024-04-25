import csv 

import time 

 # Initialize global variables for player name, actions, and start time - this didn't work, until I made the variables global. I think this can be deleted 


player_name = "" 
actions = 0 
start_time = 0 

 

# define rooms and items  

couch = { 

    "name": "couch", 
    "type": "furniture", 

} 


bookshelf = { 

    "name": "bookshelf", 
    "type": "puzzle", 
    "puzzle_solution": "5472", 
    "hint": "Check the back cover of the red book on the second shelf.", 

} 


red_book = { 

    "name": "red book", 
    "type": "item", 
    "contains": "The code 5472 is scribbled on the back cover.", 

} 


door_a = { 

    "name": "door a", 
    "type": "lock", 
    "unlocks": "key",

} 


key_a = { 

    "name": "key for door a", 
    "type": "key", 
    "target": door_a, 

} 


piano = { 

    "name": "piano", 
    "type": "lock", 
    "unlocks": "key",

} 


key_piano = { 

    "name": "key for the piano", 
    "type": "key", 
    "target": piano, 

} 


queen_bed = { 

    "name": "queen bed", 
    "type": "furniture", 

} 


painting = { 

    "name": "painting", 
    "type": "hidden item", 

} 


locker = {  

    "name": "locker", 
    "type": "lock", 
    "unlocks": "key",

} 


key_locker = { 

     "name": "key for a locker", 
     "type": "key", 
     "target": locker, 

} 


door_b = { 

    "name": "door b", 
    "type": "lock",
    "unlocks": "key", 

} 


key_b = { 

    "name": "key for door b", 
    "type": "key", 
    "target": door_b, 

} 


door_c = { 

    "name": "door c", 
    "type": "lock", 
    "unlocks": "key",

} 
 

double_bed = { 

    "name": "double bed", 
    "type": "furniture", 

} 


dresser = { 

    "name": "dresser", 
    "type": "puzzle", 
    "puzzle_solution": "58746", 
    "hint": "The television can give you the code that you need."

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
    "type": "lock", 
    "unlocks": "key",

} 


key_d = { 

    "name": "key for door d", 
    "type": "key", 
    "target": door_d, 

} 


game_room = { 

    "name": "game room", 
    "type": "room", 
    "description": "The room has a cozy, albeit dusty atmosphere filled with board games and an old grand piano.", 

} 


bathroom = {
    "name": "bathroom",
    "type": "room",
    "description": "It is rather modern and tranquil, featuring clean lines with a spacious walk-in shower and a separate bathtub for relaxation.",
}

kitchen = {
    "name": "kitchen",
    "type": "room",
    "description": "It is well-equipped with modern appliances and granite countertops. An inviting island sits at the center, surrounded by white cabinets and subtle lighting.",
}


toilet_seat = {
    "name": "toilet seat",
    "type": "item",
}

fridge = {
    "name": "fridge",
    "type": "item",
}

door_e = {
    "name": "door e",
    "type": "lock",
    "unlocks":"key"
}
door_f = {
    "name": "door f",
    "type": "lock",
    "unlocks":"key"
}

key_e = {
    "name": "key for door e",
    "type": "key",
    "target": door_e,
}

key_f = {
    "name": "key for door f",
    "type": "key",
    "target": door_f,
}

bedroom_1 = { 

    "name": "bedroom 1", 
    "type": "room", 
    "description": "It's a small bedroom with a large queen-sized bed and a wooden wardrobe.", 
    "image": "bedroom_1.jpeg", 

} 

bedroom_2 = { 

    "name": "bedroom 2", 
    "type": "room", 
    "description": "This bedroom features a double bed and a small dresser. It seems less used.", 

} 

television = {
    "name": "television",
    "type": "riddle",

}

dresser_code = {

    "name":"code to open the dresser",
    "description": "58746",
    "type": "key",
    "target": dresser
}

remote = {

    "name": "remote",
    "type": "item",

}

living_room = { 

    "name": "living room", 
    "type": "room", 
    "description": "The living room is spacious with a comfortable couch, a television, and a dining table.", 

} 

wooden_box = {

    "name": "wooden box",
    "type": "lock",
    "unlocks": "key",


}

key_woodenbox = { 

     "name": "key for a wooden box", 
     "type": "key", 
     "target": wooden_box, 

}

closet = {

    "name": "closet",
    "type": "furniture",
}

outside = { 

  "name": "outside", 
  "description": "You see the outside world, a breath of fresh air and freedom.", 

} 

all_rooms = [game_room, bedroom_1, bedroom_2, living_room, bathroom, kitchen, outside] 

all_doors = [door_a, door_b, door_c, door_d, door_e, door_f] 


# define which items/rooms are related 

object_relations = { 

    "game room": [couch, piano, bookshelf, door_a], 
    "bookshelf": [key_piano], 
    "piano": [key_a], 
    "door a": [game_room, bedroom_1], 
    "bedroom 1": [painting, queen_bed, door_a,door_b, door_c], 
    "painting": [key_locker], 
    "locker": [key_b], 
    "queen bed": [locker], 
    "bedroom 2": [double_bed,television, dresser,door_b, door_e], 
    "television": [dresser_code],
    "double bed": [remote], 
    "dresser": [key_e], 
    "living room": [door_c, closet, dining_table, door_d,door_f], 
    "closet": [key_woodenbox],
    "dining table": [wooden_box],
    "wooden box": [key_f],
    "kitchen": [fridge, door_f],
    "bathroom": [toilet_seat,door_e],
    "toilet seat": [key_c],
    "fridge": [key_d],
    "outside": [door_d], 
    "door b": [bedroom_1, bedroom_2], 
    "door c": [bedroom_1, living_room], 
    "door d": [living_room, outside], 
    "door e": [bathroom, bedroom_2],
    "door f": [kitchen, living_room]
} 

 

# define game state. Do not directly change this dict.  
# Instead, when a new game starts, make a copy of this 
# dict and use the copy to store gameplay state. This  
# way you can replay the game multiple times. 

INIT_GAME_STATE = { 

    "current_room": game_room, 

    "keys_collected": [], 

    "target_room": outside, 



} 

 
def start_game(): 

    global player_name 
    player_name = input("Enter your name: ").strip() 
    global start_time 
    start_time = time.time() 
    global actions 
    actions = 0 
    global game_state 
    global difficulty_level
    difficulty_level = choose_difficulty() 

    game_state = initialize_game_state(difficulty_level) 
    print(f"Welcome, {player_name}! You find yourself in a mysterious house with no memory of how you got here. You must escape!\nUse 'explore' to check the room you are in, and use 'examine' to check individual items that you may find.") 



    # print("Game State Before Playing:", game_state)  # Debug print 

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
        duration = round(time.time() - start_time, 2) 
        print(f"Congratulations {player_name}, you made it! You accomplished your task in {duration}, seconds. It took you {actions} actions!") 
        update_leaderboard(player_name, duration, actions, difficulty_level) 

    else: 
        print(f"\nYou are now in the {room['name']}.") 
        intended_action = input("What would you like to do? Type 'explore' or 'examine'\n").strip().lower() 

        if intended_action == "explore": 
            explore_room(room) 
            room["explored"] = True  # Set the room as explored 
            actions += 1  # Increment actions counter 
            play_room(room)  # Restart the loop 

        elif intended_action == "examine": 
            if "explored" not in room or room["explored"] == False: 
                print("You haven't explored the room yet to see what items are there to be examined.\n") 
                actions += 1  # Increment actions counter 
                play_room(room) 

            else: 
                examine_item(input("What would you like to examine?\n").strip().lower()) 

        else: 
            print("Not sure what you mean. Type 'explore' or 'examine'.\n") 
            play_room(room) 

def explore_room(room): 

    """ 
    Explore a room. List all items belonging to this room. 

    """ 

    global actions 

    items = [i["name"] for i in object_relations[room["name"]]] 
    print(f"\nYou have decided to explore the room. This is the {room['name']}. {room['description']} These items can be examined:", ", ".join(items)) 
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

def prompt_yes_no(prompt): 

    """ 
    Prompt the user with a yes/no question and return True for 'yes' and False for 'no'. 
    """ 

    while True: 

        response = input(prompt).strip().lower() 
        if response == 'yes': 
            return True 
        elif response == 'no': 
            return False 
        else: 
            print("Invalid input. Please enter 'yes' or 'no'.\n") 

 

def handle_puzzle(item, current_room): 
    attempts = 0 
    while attempts < 3: 
        puzzle_code = input("\nThis bookshelf contains a numeric lock. Enter the 4-digit code. You get 3 attempts. Type 'hint' to get help. If you rather continue exploring, you may instead type 'pass'. \n") 

        if puzzle_code.lower() == 'hint':
            print(f"Hint: {item['hint']}\n")
            break

        elif puzzle_code == item["puzzle_solution"]: 
            key_found = object_relations[item["name"]].pop(0) 
            game_state["keys_collected"].append(key_found) 
            print("\nCorrect code! You find a " + key_found["name"] + ".") 
            return  # Exit the function after solving the puzzle 
        elif puzzle_code == 'pass':
            play_room(current_room)
            break
        else: 
            attempts += 1 
            print("\nWrong code.") 

            if attempts == 3: 
                print("\nYou've entered the wrong code multiple times.")


def handle_puzzle_1(item, current_room): 
    attempts = 0 
    while attempts < 3: 
        puzzle_code = input("\nThis dresser contains a numeric lock. Enter the 5-digit code. You get 3 attempts. Type 'hint' to get help. If you rather continue exploring, you may type 'pass'.\n") 

        if puzzle_code.lower() == 'hint': 
            print(f"Hint: {item['hint']}\n")
            break

        elif puzzle_code == item["puzzle_solution"]: 
            key_found = object_relations[item["name"]].pop(0) 
            game_state["keys_collected"].append(key_found) 
            print("\nCorrect code! You find a " + key_found["name"] + ".") 
            return  # Exit the function after solving the puzzle 
        elif puzzle_code == 'pass':
            play_room(current_room)
            break
        else: 
            attempts += 1 
            print("\nWrong code.") 

            if attempts == 3: 
                print("\nYou've entered the wrong code multiple times.")


def handle_riddle():
    """
    Handles the riddle interaction.
    """
    # Display the riddle to the player

    print("I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?")

    # Get the player's answer
    player_answer = input("\nEnter your answer: ")

    # Check if the answer is correct
    correct_answer = "sound"

    if player_answer.lower().strip() == correct_answer:
        print("\nCongratulations! You've solved the riddle.\n")
        print("\nThe screen turns white, revealing the hidden message.\n")
        print(f"\nYou read the message: 'The {dresser_code['name']} is {dresser_code['description']}'\n")

        game_state["keys_collected"].append(dresser_code)

    else:
        print("\nSorry, that's not the correct answer. Keep trying!")
 
def examine_item(item_name): 

    """ 
    Examine an item which can be of different types. 
    First make sure the intended item belongs to the current room. 
    Then check if the item is of type 'lock' meaning that it needs either a key or a code to be unlocked. 
    Tell player if key/code hasn't been collected yet. 
    Otherwise open if 'lock' item is not door, if door: ask player if they want to go to the next room. 
    If the item is not a lock type, then check if it contains keys or other items of interest. 
    Collect the key if found and update the game state. Add item of interest to items in related room.
    At the end, play either the current or the next room depending on the game state to keep playing. 

    """ 

    current_room = game_state["current_room"] 
    next_room = "" 
    output = None 

    global actions 


    for item in object_relations[current_room["name"]]: 

        if(item["name"] == item_name): 
            output = "\nYou examine the " + item_name + ". " 

            if(item["type"] == "lock"): 
                have_key = False 
                for key in game_state["keys_collected"]: 

                    if(key["target"] == item): 
                        have_key = True 

                if(have_key): 
                    output += f"You unlock it with a {item['unlocks']} that you have." 
                    actions += 1  # Increment actions counter 

                    if not item["name"].startswith("door"): 
                        item_found = object_relations[item["name"]].pop() 
                        game_state["keys_collected"].append(item_found) 
                        print(f"\nInside the {item['name']} you find the {item_found['name']}")  

                        break 

                    else: 
                        next_room = get_next_room_of_door(item, current_room) 

                else: 
                    output += f"It is locked but you don't have the {item['unlocks']} to open it.\n" 
                    actions += 1  # Increment actions counter 

            elif item["type"] == "puzzle":
                if item_name == "bookshelf":
                    object_relations[current_room["name"]].append(red_book)
                    handle_puzzle(item, current_room) 
                    break 
                elif item_name == "dresser":
                    handle_puzzle_1(item, current_room) 
                    break   

            elif item["name"] == "red book": 
                print(f"\nYou examine the red book. {item['contains']}\n") 

                break 

            elif item["type"] == "riddle" and item_name == "television":

                if remote in object_relations[current_room["name"]]:
                    print(f"\nYou examine the {item['name']}, and turn it on with the remote you have\n")
                    print("The screen reveals a riddle.\n")
                    handle_riddle()

                    break
                
                else:
                    print(f"\nYou examine the {item['name']}, but it is turned off, and you don't have the remote.\n")
                    break

            else: 
                if(item["name"] in object_relations and len(object_relations[item["name"]])>0): 

                    item_found = object_relations[item["name"]].pop() 
                    if item_found["type"] == "key":
                        game_state["keys_collected"].append(item_found) 
                    else:
                        object_relations[current_room["name"]].append(item_found)

                    output += "You find a " + item_found["name"] + "." 
                    actions += 1  # Increment actions counter 

                   
                else: 
                    output += "\nThere isn't anything interesting about it.\n" 
                    actions += 1  # Increment actions counter 

            print(output) 

            break 

 

    if(output is None): 

        print("\nThe item you requested is not found in the current room.\n") 

     

    if(next_room): 

        # Ask the user if they want to go to the next room 
        if prompt_yes_no("\nDo you want to go to the next room? Enter 'yes' or 'no'\n"): 
            play_room(next_room) 

        else: 
            play_room(current_room) 

    else: 
        play_room(current_room) 


def choose_difficulty(): 

    """ 
    Prompt the user to choose the difficulty level. 
    """ 

    while True: 

        print("Choose the difficulty level:") 
        print("1. Easy") 
        print("2. Medium") 
        print("3. Hard") 
        choice = input("Enter the number corresponding to your choice: ").strip() 

        if choice in ['1', '2', '3']: 
            return int(choice) 

        else: 
            print("Invalid choice. Please enter a number between 1 and 3.") 


def initialize_game_state(difficulty_level): 

 

    #Initialize the game state based on the selected difficulty level. 


    if difficulty_level == 1:  # Easy - target set 
        target_room = bedroom_1 
    elif difficulty_level == 2:  # Medium - target set 
        target_room = bedroom_2 
    elif difficulty_level == 3:  # Hard - target set 
        target_room = outside 

    #print("Difficulty Level:", difficulty_level)  # Debug print 
    #print("Target Room:", target_room)  # Debug print 


    return { 

        "current_room": game_room, 
        "keys_collected": [], 
        "target_room": target_room 

    } 

 

 

 

def update_leaderboard(name, duration, actions, difficulty_level): 

    global leaderboard 

    leaderboard.append({"name": name, "duration": duration, "actions": actions,"difficulty": difficulty_level}) 

    leaderboard.sort(key=lambda x: x["duration"])  # Sort by duration 

 

    # Write leaderboard to a CSV file 

    with open('leaderboard.csv', mode='a', newline='') as file: #mode a is append, mode w is write (in this case to overwrite) 

        fieldnames = ['Name', 'Actions', 'Duration', 'Difficulty'] 

        writer = csv.DictWriter(file, fieldnames=fieldnames) 

 

        writer.writeheader() 

        for entry in leaderboard: 

            writer.writerow({'Name': entry['name'], 'Actions': entry['actions'], 'Duration': entry['duration'], 'Difficulty': entry['difficulty']}) 

 

    print("Leaderboard updated and written to leaderboard.csv.") 



game_state = INIT_GAME_STATE.copy() 

leaderboard = [] 

 

start_game() 