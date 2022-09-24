
# Imports

import pygame
import math
import random
import time

from threading import Thread
from os import system, name

from colorama import Fore, Style

# Defining the timer - to check

def countdown():
    time_sec = 180
    while time_sec:
        mins, secs = divmod(time_sec,60)
        timeformat = "{:02d}:{:02d}".format(mins,secs)
        time.sleep(1)
        time_sec -=1
        if game_state['game_won'] == False:
            if time_sec == 119:
                print(Fore.RED + "\n\nYou only have ",timeformat,"left!")
                print(Style.RESET_ALL)
            elif time_sec == 59:
                print(Fore.RED + "\n\nYou're running out of time:",timeformat)
                print(Style.RESET_ALL)
            elif time_sec == 0:
                print(Fore.RED + "\n\nOh no.. GAME OVER")
                print(Style.RESET_ALL)

countdown_thread = Thread(target = countdown)
countdown_thread.start()

# Defining rooms

game_room = {
    "name": "game room",
    "type": "room",
    "image": "gameroom.jpg",
}

bedroom_1 = {
    "name": "bedroom 1",
    "type": "room",
    "image": "bedroom1.jpg",
}

bedroom_2 = {
    "name": "bedroom 2",
    "type": "room",
    "image": "bedroom2.jpg",
}

living_room = {
    "name": "living room",
    "type": "room",
    "image": "livingroom.jpg",
}

backyard = {
    "name": "backyard",
    "type": "room",
    "image": "backyard.jpg",
}

outside = {
  "name": "outside",
  "image": "outside.jpg",
}

# Defining furnishings

couch = {
    "name": "couch",
    "type": "furniture",
    "image": "couch.jpg",
}

piano = {
    "name": "piano",
    "type": "furniture",
    "image": "piano.jpg",
}

suspicious_painting = {
    "name": "suspicious painting",
    "type": "safe",
    "image": "painting.jpg",
}

queen_bed = {
    "name": "queen bed",
    "type": "furniture",
    "image": "queenbed.jpg",
}

double_bed = {
    "name": "double bed",
    "type": "furniture",
    "image": "doublebed.jpg",
}

dresser = {
    "name": "dresser",
    "type": "furniture",
    "image": "dresser.jpg",
}

library = {
    "name": "library",
    "type": "furniture",
    "image": "library.jpg",
}

dining_table = {
    "name": "dining table",
    "type": "furniture",
    "image": "diningtable.jpg",
}

kennel = {
    "name": "kennel",
    "type": "dog",
    "image": "kennel.jpg",
}

tree = {
    "name": "tree",
    "type": "furniture",
    "image": "tree.jpg",
}

# Defining doors

door_a = {
    "name": "door a",
    "type": "door",
    "image": "door.jpg",
}

door_b = {
    "name": "door b",
    "type": "door",
    "image": "door.jpg",
}

door_c = {
    "name": "door c",
    "type": "door",
    "image" : "door.jpg",
}

door_d = {
    "name": "door d",
    "type": "door",
    "image": "door.jpg",
}

door_e = {
    "name": "door e",
    "type": "door",
    "image": "door.jpg",
}

# Defining keys

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

key_e = {
    "name": "key for door e",
    "type": "key",
    "target": door_e,
}

# Defining belongings

dog = "Buddy, your faithful friend"

valuables = ['wallet', 'mobile phone', 'watch']

all_rooms = [game_room, bedroom_1, bedroom_2, living_room, backyard, outside]

all_doors = [door_a, door_b, door_c, door_d, door_e]

# defining object relations

object_relations = {
    # rooms - furnishings
    "game room": [couch, piano, suspicious_painting, door_a],
    "bedroom 1": [queen_bed, door_a, door_b, door_c],
    "bedroom 2": [double_bed, dresser, door_b],
    "living room": [dining_table, library, door_c, door_d],
    "backyard": [tree, kennel, door_d, door_e],
    "outside": [door_d],
    # furnishings - items
    "piano": [key_a],
    "queen bed": [key_b],
    "double bed": [key_c],
    "dresser": [key_d],
    "library": [key_e],
    # doors - rooms
    "door a": [game_room, bedroom_1],
    "door b": [bedroom_1, bedroom_2],
    "door c": [bedroom_1, living_room],
    "door d": [living_room, backyard],
    "door e": [backyard, outside]
}

# Game state

INIT_GAME_STATE = {
    "current_room": game_room,
    "keys_collected": [],
    "items_collected": [],
    "target_room": outside,
    "game_won": False
}

def clear():
    "Clear terminal output"
    if name == 'nt':
        _ = system('cls') # windows
    else:
        _ = system('clear') # mac + linux

def linebreak():
    """
    Print a line break
    """
    print("\n\n")

def start_game():
    play_music()
    """
    Start the game
    """
    print(
    """
    You wake up on a couch and find yourself in a strange house with no windows which you have never been to before.
    You remember walking the dog - but you have no idea what happened.
    You realize that your other valuables are also missing.
    You feel some unknown danger is approaching and you must get out of the house, NOW!
    """)
    print(Fore.RED + 'You only have 3:00 minutes left!')
    print(Style.RESET_ALL)

    pygame.init()
    pygame.display.set_caption('RUN')
    icon = pygame.image.load('evacuacion.png')
    pygame.display.set_icon(icon)
    screen = pygame.display.set_mode((800, 600))
    screen.blit(pygame.image.load(game_room["image"]),(0,0))
    pygame.display.update()
    play_room(game_state["current_room"])

def play_room(room):
    "Play a room."
    curr_room = game_state["current_room"]
    game_state["current_room"] = room
    if(game_state["current_room"] == game_state["target_room"]):
        game_state['game_won'] = True
        clear()
        print("Congrats! You escaped the room!")
        if valuables in game_state['items_collected']:
            print(f"You also managed to get back your wallet, your mobile phone and your watch!")
        if dog in game_state['items_collected']:
            print(f"Best of all: you freed your dog Buddy!!")
        print("🎉 GOOD JOB!! 🎉")
        return
    else:
        print("You are now in " + room["name"])
        if curr_room != room:
            draw_room(room["image"])
        intended_action = input("What would you like to do? Type 'explore' or 'examine'?").strip()
        if intended_action == "explore":
            explore_room(room)
            play_room(room)
        elif intended_action == "examine":
            examine_item(input("What would you like to examine?").strip())
        else:
            print("Not sure what you mean. Type 'explore' or 'examine'.")
            play_room(room)
        linebreak()

def explore_room(room):
    """
    Explore a room. List all items belonging to this room.
    """
    items = [i["name"] for i in object_relations[room["name"]]]
    print("\nYou explore the room. This is " + room["name"] + ". You find " + ", ".join(items))

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
    "Examine an item which can be a door or furniture."
    current_room = game_state["current_room"]
    next_room = ""
    output = None
    clear()
    
    for item in object_relations[current_room["name"]]:
        if(item["name"] == item_name):
            output = "\nYou examine " + item_name + ". "
            draw_item(item["image"]) #needs fixing, the picture only loads for a split second
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
            elif (item["type"] == "safe"):
                open_safe(current_room)
            elif (item["type"] == "dog"):
                free_dog(current_room)
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
    
    if(next_room and input("Do you want to go to the next room? Enter 'yes' or 'no'").strip() == 'yes'):
    # if(next_room):    
        play_room(next_room)
    else:
        play_room(current_room)

# safe guess combination mini game

def open_safe(current_room):
    "Guess combination mini game intro"
    if valuables not in game_state['items_collected']:
        print(
        """
        The picture folds to the side.
        Behind it is a safe with a rusty 3 digit lock!
        You wonder if you could figure out the right combination by intuition.
        """
        )
        try_safe(current_room)
    else:
        print("\nYou have already emptied the safe.")
        play_room(current_room)

def try_safe(current_room):
    "Guess combination mini game yes/no"
    try_input = input("Do you want to give it a try? Enter 'yes' or 'no'")
    if try_input == 'yes':
        combination = math.floor(random.random() * 1000)
        guess_digits(current_room, combination)
    elif try_input == 'no':
        play_room(current_room)
    else:
        try_safe(current_room)

def guess_digits(current_room, combination):
    "Guess combination mini game logic"
    guess = input("Test your lock picking skill (3-digit number):")
    if guess.isnumeric():
        guess = int(guess)
        if 0 <= guess <= 999:
            if guess < combination:
                print(f"The heavier turning wheels tell you that the combination needs to be HIGHER than {str(guess).zfill(3)}!")
                guess_digits(current_room, combination)
            elif guess > combination:
                print(f"The easier turning wheels tell you that the combination needs to be LOWER than {str(guess).zfill(3)}!")
                guess_digits(current_room, combination)
            else:
                print("""
                🎊 BINGO! 🎊
                Your open the safe and get back your ...\n
                => 💰 wallet
                => 📱 mobile phone
                => ⌚ watch
                """)
                game_state['items_collected'].append(valuables)
                play_room(current_room)
        else:
            guess_digits(current_room, combination)
    else:
        guess_digits(current_room, combination)
        
# free dog switch mini game

def free_dog(current_room):
    "Switch combination mini game intro"
    if dog not in game_state['items_collected']:
        print(
        """
        Buddy!!
        You finally found your beloved dog.
        Someone locked Buddy in a kennel.
        """
        )
        try_kennel(current_room)
    else:
        print("\nYou have already opened the kennel and freed Buddy.")
        play_room(current_room)

def try_kennel(current_room):
    "Switch combination mini game yes/no"
    try_input = input("Do you want to try to free him? Enter 'yes' or 'no'")
    if try_input == 'yes':
        combination = [round(random.random()) for switch in range(4)]
        user_start = [round(random.random()) for switch in range(4)]
        while combination == user_start:
          user_start = [round(random.random()) for switch in range(4)]
        guess_switches(current_room, combination, user_start)
    elif try_input == 'no':
        play_room(current_room)
    else:
        try_kennel(current_room)

def guess_switches(current_room, combination, user_start):
    "Switch combination mini game logic"
    switch_icons = ['⭕', '❌']
    while combination != user_start:
        clear()
        print('The kennel is locked by a combination of switches.\n\n')
        print('\t\t' + ' '.join(['1', ' 2', ' 3', ' 4']))
        print('\t\t' + ' '.join([switch_icons[switch] for switch in user_start]))
        switch_key = input('\n\nTry one single digit at a time!')
        if switch_key == '1':
            user_start[0] = 1 if user_start[0] == 0 else 0
        elif switch_key == '2':
            user_start[1] = 1 if user_start[1] == 0 else 0
        elif switch_key == '3':
            user_start[2] = 1 if user_start[2] == 0 else 0
        elif switch_key == '4':
            user_start[3] = 1 if user_start[3] == 0 else 0
        else:
            continue
    clear()
    print('You found the correct combination!!\n\n')
    print('\t\t' + ' '.join(['1', ' 2', ' 3', ' 4']))
    print('\t\t' + ' '.join([switch_icons[switch] for switch in user_start]))
    print("""
    \n\n🎊 BINGO! 🎊
    Your open the kennel and free ...\n
    => 🐶 Buddy
    """)
    game_state['items_collected'].append(dog)
    play_room(current_room)

def draw_room(room):
    #creates images of the rooms in the game, that display when the player enters the room
    screen = pygame.display.set_mode((800, 600))
    screen.blit(pygame.image.load(room),(0,0))
    pygame.display.update()

def draw_item(item):
    #creates images of the different items in the game that display when they are examined by the player
    screen = pygame.display.set_mode((800, 600))
    screen.blit(pygame.image.load(item),(0,0))
    pygame.display.update()

def play_music():
    pygame.init()
    pygame.mixer.music.load('horror.mp3')
    pygame.mixer.music.play(-1)

game_state = INIT_GAME_STATE.copy()

start_game()