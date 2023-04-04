#For the potions room
import time
import os


# Clearing the Screen for Mac
def clear():
    #for mac
    os.system('clear')
    #for Windows
    os.system('cls')

#Library
book_1 = {'name': 'revelio page', 'type': 'item',}
book_2 = {'name': 'expelliarmus page', 'type': 'item'}
spell = { 'name': 'alohomora page', 'type': 'furniture', 'spell': 'alohomora'}
painting = { "name": "Temeritus Shanks portrait", "type": "furniture",}
book_shelve = { 'name': 'book shelve', 'type': 'furniture'}
library = { "name": "library", "type": "room",}
library_door = { "name": "library door", "type": "door",}
key_a = { "name": "key to open the library door", "type": "key", "target": library_door,}

#Potions room
potions_room = { "name": "potions room", "type": "room",}
door_b = { "name": "stairs gate", "type": "door",}
key_b = {"name": "ashwinder eggs", "type": "key", "target": door_b,}
door_c = {"name": "golden door", "type": "door",}
potion_station = {"name": "potion station", "type": "furniture",}
green_cabinet = {"name": "cabinet", "type": "furniture",}
cabinet = {"name": "wood cabinet", "type": "furniture",}
bookstand = {"name": "bookstand", "type": "furniture",}

#Requirement room
requirement_room = {"name": "requirement room", "type": "room",}
erised_mirror = { "name": "erised mirror", "type": "door",}
outside = {"name": "outside"}


#Stairs
key_c = { "name": "golden key", "type": "key", "target": door_c,}
key_d = { "name": "paper inscription to use with a mirror", "type": "key", "target": erised_mirror,}
nick = { "name": "portrait of Nick", "type": "furniture",}
notebook = {"name": "notebook", "type": "furniture",}
stairs = {"name": "stairs", "type": "room",}


#Variables
diploma = 'Diploma of Ironhack Data'
hogwarts ={ "points": 0, "name_wizard": None}

all_rooms = [library, potions_room, stairs, requirement_room, outside]

all_doors = [library_door,door_b,door_c,erised_mirror]

all_keys = []

# define which items/rooms are related
object_relations = {
    "library": [book_shelve, painting, book_1, book_2, spell, library_door],
    'alohomora page': [key_a],
    "outside": [erised_mirror],
    "library door": [library, potions_room],
    "potions room": [potion_station, green_cabinet, cabinet, bookstand, library_door, door_b, door_c],
    "bookstand": [key_b],
    "stairs gate": [potions_room,stairs],
    "stairs": [nick,notebook,door_b],
    "portrait of Nick": [key_d],
    "notebook": [key_c],
    "requirement room": [erised_mirror,door_c],
    "erised mirror": [outside],
    "golden door": [potions_room,requirement_room]
}

# define game state. Do not directly change this dict. 
# Instead, when a new game starts, make a copy of this
# dict and use the copy to store gameplay state. This 
# way you can replay the game multiple times.

INIT_GAME_STATE = {
    "current_room": library,
    "keys_collected": [],
    "target_room": outside
}

def sorting_hat():
    #variables
    gryffindor = 0
    ravenclaw = 0
    hufflepuff = 0
    slytherin = 0
    name_wizard = ''

    #Welcome
    clear()
    print('==========================')
    print('\nWelcome to Hogwarts')
    print('The magical world awaits you')
    print('\n==========================')

    
    #Asking name
    name_wizard = input('\nBut, first of all: what is your name? ')

    #Explain the next move
    clear()
    
    print('It is dangerous to go alone, answer this question so we can sort you inside a house.')
    print('\n==========================')

    #Question 1 ---- if the user writes anything besides 1 or 2, the code repeats. 
    question1=None
    while (question1 !=1) and (question1 !=2):
        try:
            print(f'\n{name_wizard}, do you like Dawn or Dusk? ')
            print('    1) Dawn')
            print('    2) Dusk')
            question1 = int(input('\nWrite the corresponding number: '))
        except ValueError:
            clear()
            print('\n-> Please, enter a number between 1 and 2')
            print('\n==========================')
        else:
            if question1 == 1:
                gryffindor = gryffindor +1
                ravenclaw = ravenclaw + 1

            elif question1 == 2:
                hufflepuff = hufflepuff + 1
                slytherin = slytherin + 1
            else:
                clear()
                print('\n-> Please, enter a number between 1 and 2')
                print('\n==========================')

    clear()
    #Question 2 ---- if the user writes anything besides 1, 2, 3 or 4, the code repeats. 
    #print('\n==========================')

    question2 = None
    while (question2 != 1) and (question2 != 2) and (question2 != 3) and (question2 != 4):
        try:
            print(f"{name_wizard}, when you're dead, how do you want people to remember you as?")
            print('    1) The Good')
            print('    2) The Great')
            print('    3) The Wise')
            print('    4) The Bold')
            question2 = int(input('\nWrite the corresponding number: '))
        except ValueError:
            clear()
            print('\n-> Please, enter a number between 1 and 4')
            print('\n==========================')
        else:
            if question2 == 1:
                hufflepuff = hufflepuff +2
            elif question2 == 2:
                slytherin = slytherin + 2
            elif question2 == 3:
                ravenclaw = ravenclaw + 2
            elif question2 == 4:
                gryffindor = gryffindor +2
            else:
                clear()
                print('\n-> Please, enter a number between 1 and 4')
                print('\n==========================')


    clear()
    #print('\n==========================')

    #Question 3 ---- if the user writes anything besides 1, 2, 3 or 4, the code repeats. 
    question3 = None
    while (question3 != 1) and (question3 != 2) and (question3 != 3) and (question3 != 4):
        try:
            print(f'{name_wizard}, which kind of instrument most pleases your ear?')
            print('    1) The violin')
            print('    2) The trumpet')
            print('    3) The piano')
            print('    4) The drum')
            question3 = int(input('\nWrite the corresponding number: '))
        except ValueError:
            clear()
            print('\n-> Please, enter a number between 1 and 4')
            print('\n==========================')
        else:
            if question3 == 1:
                slytherin = slytherin +1
            elif question3 == 2:
                hufflepuff = hufflepuff + 1
            elif question3 == 3:
                ravenclaw = ravenclaw + 1
            elif question3 == 4:
                gryffindor = gryffindor +1
            else:
                clear()
                print('\n-> Please, enter a number between 1 and 4')
                print('\n==========================')
    clear()
    #Sorting 
    winning_house = ''
    winning_motto = ''
    if gryffindor >= slytherin and gryffindor >= ravenclaw and gryffindor >= hufflepuff:
        winning_house = '🦁 Gryffindor'
        winning_motto = 'the House of the brave'
    elif slytherin >= ravenclaw and slytherin >= hufflepuff:
        winning_house = '🐍 Slytherin'
        winning_motto = 'the house of the ambitious'
    elif ravenclaw >= hufflepuff:
        winning_house = '🦅 Ravenclaw'
        winning_motto = 'the house of the witty'
    else:
        winning_house = '🦡 Hufflepuff'
        winning_motto = 'the house of the most loyal people'
    
    #Print the winning house
    #print('\n==========================')
    
    print(f"Congrats, {name_wizard}, you've been sorted into {winning_house}, {winning_motto}. ")
    time.sleep(2)
    hogwarts['points']=0
    hogwarts['name_wizard'] = name_wizard
    hogwarts['house'] = winning_house

#The Ghost of Nick Almost Beheaded in the stairs give you a paper
def paper():
  output = "\nNick Almost Beheaded gives you a piece of paper. It reads the following:"
  output += '\n--------------------------------------------'
  output += '\n          ' + diploma[::-1]
  output += '\n--------------------------------------------'
  output += "\nMaybe if you use something reflective it will show itself."
  print(output)

#The erised mirror shows the message of the paper
def mirror ():
    print('You put the paper that the portrait of Nick gave you in front of the Erised Mirror.')
    print('It shows the thing that you wish the most. You can read the following:')
    print('\n--------------------------------------------')
    print('         ' + diploma)
    print('--------------------------------------------')



def linebreak():
    """
    Print a line break
    """
    print("\n\n")



def start_game():
    """
    Start the game
    """
    sorting_hat()
    print('\n' + hogwarts['name_wizard'] + ", as a "+ hogwarts['house'] + " student you are curious about the castle and its histories.")
    print("However, when you touched a not common object, not to say weird, you were drawn to this completly dark room, where you can't see a thing in front of you.")
    print("You remember that is almost time for your Potions class and Professor Snape doesn't like late students. You need to find a way out NOW or you will make your house loose points.")
    print('\n========================')
    light_the_room()
    play_room(game_state["current_room"])
    
    # using a while loop to keep calling light_the_room() until the player enters play_room()
    '''
    while True:
        if light_the_room():
            play_room(game_state["current_room"])
            break
        else:
            print("You failed to light the room. Try again. The spell is something like 'lum...")
    '''
'''
def light_the_room():
    Lumus = input(str('\nYou remember a spell to light the room and now is the perfect time to try it: '))
    if Lumus == 'lumus':
        clear()
        print("\nLumus spell worked. Professor Snape didn't believe you when you said you were concentrating, not sleeping")
        play_room(game_state["current_room"])
    else:
        clear()
        #print('Try again. Its something like lum...')
    linebreak()
'''

def light_the_room():
    spell = None
    points_spell = 10
    while spell != 'lumus':
        try:
            spell = input(str('\nYou remember a spell to light the room and now is the perfect time to try it: ')) 
        except ValueError:
            clear()
            print("You failed to light the room. Try again. The spell is something like 'lum...'")
            points_spell -= 1
            print('\n========================')
        else:
            if spell == 'lumus':
                hogwarts["points"] += points_spell
                clear()
                print("Lumus spell worked.",points_spell,'points to', hogwarts["house"] ,"Professor Snape didn't believe you when you said you were concentrating, not sleeping")
                print('\nNow', hogwarts['house'], 'has', hogwarts['points'])
                print('\n========================')
                break
            else:
                clear()
                points_spell -= 1
                print("You failed to light the room. Try again. The spell is something like 'lum...'")
                print('\n========================')
                

def room_desc(room): 
    if room == potions_room:
        potion_room()

def play_room(room):
    """
    Play a room. First check if the room being played is the target room.
    If it is, the game will end with success. Otherwise, let player either 
    explore (list all items in this room) or examine an item found here.
    """
    #print(hogwarts["points"])
    game_state["current_room"] = room
    
    if(game_state["current_room"] == game_state["target_room"]):
        print("\nFinally, you enter the Potions class.")
        hogwarts['points'] -= 10
        print(f"""Snape is quite mad at you and he says: "10 less points for {hogwarts["house"]}!". Now your house has {hogwarts["points"]} points.""")
        print("\nMischief managed.")
        time.sleep(30)
        exit()
    else:
        #print("You are now in " + room["name"])
        room_desc(room)
        explore_room(room)
        examine_item(input("\nWhat would you like to examine? ").strip())

        linebreak()

visited_potions_room = False


def potion_room():
    global visited_potions_room
    if not visited_potions_room:
        print("You enter a dark and small room with shelves of various potion ingredients lining the walls.")
        time.sleep(2)
        print('∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞')
        print("In the center of the room is a potion station with a small note on it.")
        time.sleep(2)
        print('∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞')
        print("The note says 'the door shall open to the lucky one who find the right eggs'")
        time.sleep(2)
        print('∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞')
        print("You notice that near the note there is a flask labeled 'incomplete felix felicis'.")
        time.sleep(2)
        visited_potions_room = True  
    

#History in the potions room
def bookstand():
    print("You search the bookstand and find a container of ashwinder eggs!")
    print("You grab the eggs and return to the potion station.")
    time.sleep(2) 
    print('∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞∞')
    print("You add the ashwinder eggs to the potion and it turns a brilliant gold color!")
    time.sleep(2)
    print("Suddenly, you feel lucky enough to try and open the door")
    time.sleep(2)

#Riddle inside the notebook
def riddle():
    print(f'\nYou encounter the Magic Snake notebook, if you answer correctly you could be awarded 10 points for your house.')
    print(f"\nBe carefull, your house will be subtracted 1 point each time your answer is wrong.")
    riddle_nick=None
    
    riddle_points = 10
    while riddle_nick != 'python':
        try:
            print('\n==========================')
            print(f'\nQuestion 1: We know that Harry Potter knows parsel...')
            riddle_nick = input("\nBut what other 'snake language' can you speak: ")
        except ValueError:
            clear()
            print('-> That is not correct.')
            riddle_points -= 1
            print('\nRemember the language we are learning right now...')
        else:
            if riddle_nick == 'python':
                clear()
                print('Correct!')
                hogwarts['points']+=riddle_points
                print(riddle_points,'points to', hogwarts["house"], '!')
                break
            else:
              clear()
              print('-> That is not correct.')
              riddle_points -= 1
              print('\nRemember the language we are learning right now...')
    
    riddle_nick = None
    riddle_points = 10
    while riddle_nick != 'nagini':
        try:
            print('\n==========================')
            riddle_nick = input("\nQuestion 2: What is the name of Voldemort's snake? ")
        except ValueError:
            clear()
            print('-> That is not correct.')
            riddle_points -= 1
            print("\nRemember it rhymes with 'Martini'")
        else:
            if riddle_nick == 'nagini':
                clear()
                print('Correct!')
                hogwarts['points']+=riddle_points
                print(riddle_points,'points to', hogwarts["house"], '!')
                break
            else:
              clear()
              print('-> That is not correct.')
              riddle_points -= 1
              print("\nRemember it rhymes with 'Martini'")
    
    riddle_nick = None
    riddle_points = 10
    print('\nNow the last question')  
    while riddle_nick != 'basilisk':
        try:
            print('\n==========================')
            riddle_nick = input("\nQuestion 3: What kind of snake was inside the pipes in Hogwarts? ")
        except ValueError:
            clear()
            print('-> That is not correct.')
            riddle_points -= 1
            print("\nIt is not 'basil', but it is similar to basil ;)")

        else:
            if riddle_nick == 'basilisk':
                clear()
                print('Correct!')
                hogwarts['points'] += riddle_points
                print(riddle_points,'points to', hogwarts["house"], '!')
                time.sleep(3)
                break
            else:
                clear()
                print('-> That is not correct.')
                riddle_points -= 1
                print("\nIt is not 'basil', but it is similar to basil ;)")
    clear()
    print('You finished reading the notebook and now', hogwarts["house"], 'has', hogwarts["points"],'points!')


def explore_room(room):
    """
    Explore a room. List all items belonging to this room.
    """
    print("\nYou are in the " + room["name"] + " and you find:")
    items = [i["name"] for i in object_relations[room["name"]]]
    a=0
    for i in items:
        a+=1
        print(a,')',i)
    

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
    for item in object_relations[current_room["name"]]:
        if(item["name"] == item_name):
            clear()
            output = "After you examine the " + item_name + ', '
            if(item["type"] == "door"):
                have_key = False
                for key in game_state["keys_collected"]:
                    if(key["target"] == item):
                        have_key = True
                if(have_key):
                    if item["name"] == "erised mirror":
                        mirror()
                        output += "you see that the class is at the other side of the mirror."
                    else:
                        output += 'you unlocked the door with the item you just found' 
                        #output += '\n========================' 
                    next_room = get_next_room_of_door(item, current_room)
                else:
                    output += "It is locked, you don't have the required item."
            else:
                if (item["name"] in object_relations and len(object_relations[item["name"]])>0 and item["name"] == nick["name"]):
                  paper()
                elif (item["name"] in object_relations and len(object_relations[item["name"]])>0 and item["name"] == notebook["name"]):
                  riddle()
                elif item["name"] == "bookstand":
                  bookstand()
                if(item["name"] in object_relations and len(object_relations[item["name"]])>0):
                    item_found = object_relations[item["name"]].pop()
                    game_state["keys_collected"].append(item_found)
                    output += "you found the " + item_found["name"] +"."    

                else:
                    output += "There isn't anything interesting about it."
            print(output)
            print('\n========================')
            break


    if(output is None):
        clear()
        print("The item you requested is not found in the current room.")
        print('\n========================')
    
    if(next_room and input("\nDo you want to go to the next room? Enter 'yes' or 'no': ").strip() == 'yes'):
        clear()
        play_room(next_room)
    else:
        play_room(current_room)

game_state = INIT_GAME_STATE.copy()

start_game()

