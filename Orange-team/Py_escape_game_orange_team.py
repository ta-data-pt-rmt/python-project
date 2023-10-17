#!/usr/bin/env python
# coding: utf-8

# In[4]:


get_ipython().system('pip install pygame')


# In[5]:


#FINAL VERSION - Spaceship theme + PyGame

#add PyGame to have background music
import pygame
import random #To select a random item in the treasure box

# Initialize PyGame and set up music
pygame.init()

pygame.mixer.init()
pygame.mixer.music.load("space-chillout-14194.mp3")  # path added to the music file
pygame.mixer.music.set_volume(0.5)  # Adjust the volume as needed


music_stopped = False


# Define rooms and items
couch = {
    "name": "couch",
    "type": "furniture",
}

desk = {
    "name": "desk",
    "type": "furniture"
} # Irina: new furniture

chair = {
    "name": "chair",
    "type": "furniture"
} # Irina: new furniture

armchair = {
    "name": "armchair",
    "type": "furniture"
} # Irina: new furniture

shelf = {
    "name": "shelf",
    "type": "furniture"
} # Irina: new furniture

sofa = {
    "name": "sofa",
    "type": "furniture"
} # Irina: new furniture

chest_of_drawers = {
    "name": "chest of drawers",
    "type": "furniture"
} # Irina: new furniture

door_a = {
    "name": "door a",
    "type": "door",
}

key_a = {
    "name": "key for door a",
    "type": "key",
    "target": door_a,
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

key_c = {
    "name": "key for door c",
    "type": "key",
    "target": door_c,
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

control_panel = {
    "name": "control panel",
    "type": "furniture",
}

bunk_bed = {
    "name": "bunk bed",
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

emergency_kit = {
    "name": "emergency kit",
    "type": "furniture",
}

# Spaceship

navigation_room = {
    "name": "navigation room",
    "type": "room",
}

cabin_1 = {
    "name": "cabin 1",
    "type": "room",
}

cabin_2 = {
    "name": "cabin 2",
    "type": "room",
}

control_room = {
    "name": "control room",
    "type": "room",
}

airlock_chamber = {
    "name": "Airlock chamber",
    "type": "room",
}

outside = {
    "name": "outside"
}

treasure_box = {
    "name": "treasure box",
    "type": "furniture",
    "content": random.choice(["one year free unlimited traveling pass in business class", "a rocket sticker", "a trip for an island of your choice"])
} #Amandine new furniture added

random_item = None #intialize random item

all_rooms = [navigation_room, cabin_1, cabin_2, control_room, airlock_chamber, outside]

all_doors = [door_a, door_b, door_c, door_d]

object_relations = {
    "navigation room": [couch, control_panel, desk, chair, door_a], #Irina: new furniture added
    "cabin 1": [bunk_bed, armchair, shelf, door_c, door_b], #Irina: new furniture added
    "cabin 2": [double_bed, chest_of_drawers, dresser, door_b], #Irina: new furniture added
    "control room": [emergency_kit, sofa, door_d, door_c, treasure_box], #Irina: new furniture added + Amandine : added treasure box
    "airlock chamber" : [outside, navigation_room],#Amandine : added hallway
    "control panel": [key_a],
    "bunk bed": [key_b],
    "dresser": [key_d],
    "double bed": [key_c],
    "door a": [navigation_room, cabin_1],
    "door b": [cabin_1, cabin_2],
    "door c": [cabin_1, control_room],
    "door d": [control_room, airlock_chamber] #Nhan : change destination to "hallway" instead of "outside"
}


INIT_GAME_STATE = {
    "current_room": navigation_room,
    "keys_collected": [],
    "target_room": outside
}

def linebreak():
    print("\n\n")

#Amandine : add exit function if the user does not want to play anytime
def exit_game():
    exit_choice = input("Do you want to exit the game? (Enter 'yes' to exit or 'no' to continue): ").strip()
    if exit_choice.lower() == 'yes':
        print("Thank you for playing. Goodbye!")
        exit()

def start_game():
    print("You wake up near from the control panel and find yourself in a strange spaceship with no windows which you have never been to before. You don't remember why you are here and what had happened before. You feel some unknown danger is approaching and you must get back to Earth, NOW!")

    # Start playing the music
    pygame.mixer.music.play(-1)  # Loop the music
    play_room(game_state["current_room"])

def play_room(room):
    game_state["current_room"] = room
    
    global music_stopped

    if(game_state["current_room"] == game_state["target_room"]):
        print(f"Yeah! You are now on the way to Earth! And you won {random_item}") #add this to see the item
    else:
        if game_state["current_room"]==airlock_chamber:
            if left_or_right()==True:
                print("Congrats! You made the right choice")
                pygame.mixer.music.stop()
                play_room(game_state["target_room"])
            else:
                print("Oops it is a wrong direction. You are now back in the spaceship")
                game_state["current_room"] = navigation_room  # Set the current room back to game room
                play_room(navigation_room)  # Play in the game room
        else:
            print("You are now in " + room["name"])
            intended_action = input("What would you like to do? Type 'explore', 'examine', 'exit' or 'stop the music'? ").strip()
            if intended_action == "explore":
                explore_room(room)
                play_room(room)
            elif intended_action == "examine":
                examine_item(input("What would you like to examine? ").strip())
            #give the possibility to exit game any time
            elif intended_action == "stop the music" and not music_stopped:
                pygame.mixer.music.stop()
                music_stopped = True  # Set the flag to True
                print("Music stopped.")
                play_room(room)
                return
            elif intended_action == "exit":
                exit_game()
            else:
                print("Not sure what you mean. Type 'explore', 'examine', or 'exit'.")
                play_room(room)
            linebreak()

def explore_room(room):
    items = [i["name"] for i in object_relations[room["name"]]
    ]
    print("You explore the room. This is " + room["name"] + ". You find " + ", ".join(items))

def get_next_room_of_door(door, current_room):
    connected_rooms = object_relations[door["name"]]
    for room in connected_rooms:
        if not current_room == room:
            return room

def examine_item(item_name):
    global random_item  # Use the global random_item variable to print the item
    current_room = game_state["current_room"]
    next_room = ""
    output = None

    for item in object_relations[current_room["name"]]:
        if item["name"] == item_name:
            output = "You examine " + item_name + ". "
            if item["type"] == "door":
                have_key = False
                for key in game_state["keys_collected"]:
                    if key["target"] == item:
                        have_key = True
                if have_key:
                    output += "You unlock it with a key you have."
                    next_room = get_next_room_of_door(item, current_room)
                else:
                    output += "It is locked but you don't have the key."

            elif item["name"] == "treasure box":
                # Randomly select an item to put in the box
                random_item = random.choice(["one year's free, unlimited rocket travel in business class", "a rocket sticker", "a trip for an island of your choice"])
                output += f"You find {random_item} in the box."

                # Remove the box from the room as it's been examined.
                object_relations[current_room["name"]] = [i for i in object_relations[current_room["name"]] if i["name"] != "box"]

            else:
                if item["name"] in object_relations and len(object_relations[item["name"]]) > 0:
                    item_found = object_relations[item["name"]].pop()
                    game_state["keys_collected"].append(item_found)
                    output += "You find " + item_found["name"] + ". "
                    if item_found["name"] == "key for door a":
                        if ask_questions():
                            output += "You answered the questions correctly and earned the key for door D, and you are now in the control room, one step away to the last room!."
                            game_state["keys_collected"].append(key_d)
                            next_room = control_room
                        else:
                            output += "You answered the questions incorrectly, let's keep exploring."

                else:
                    output += "There isn't anything interesting about it."
            print(output)
            break

    if output is None:
        print("The item you requested is not found in the current room.")

    if next_room and input("Do you want to go to the next room? Enter 'yes' or 'no'").strip() == 'yes':
        play_room(next_room)
    else:
        play_room(current_room)

def ask_questions():
    print("Yay! You have found the key for door A. If you get the next two questions right, you get key D and select if you advance to the control room! You'll be one door away from the last room. Oh and one more thing... Make sure you make the RIGHT choice in the airlock chamber ;).")
    question1 = input("How many rooms do you think are in the game? (Enter a number): ").strip()
    question2 = input("What's the speed of light (in 10^8 m/s)? (Enter the approximate integer): ").strip()

    if question1 == "5" and question2 == "3":
        return True
    else:
        return False

def left_or_right():
    print("You're now out of the control room and in the airlock chamber connected to outside, you have to choose to turn left or right. Choosing wrong side will lead you back to the navigation room")
    the_choice = input("Do you want to turn left or turn right? Enter the word left or right ") #Add that the user can just enter right or left, otherwise it does not work
    if the_choice =="left":
        return False
    #print("Oops it is a wrong direction. You are now back in game room")
        #start_game()
    else:
        return True

game_state = INIT_GAME_STATE.copy()
start_game()


# In[ ]:




