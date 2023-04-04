import pygame
import sys
import time 

# define rooms and items - Game Room

game_room = {
    "name": "game room",
    "type": "room",
    "image": "Game Room.png"
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
couch = {
    "name": "couch",
    "type": "furniture",
}
cupboard_a = {
    "name": "cupboard a",
    "type": "cupboard",
}

piano = {
    "name": "piano",
    "type": "furniture",
}
padlock_a = {
  "name": "padlock a",
  "type": "padlock",
  "code": int(385),
}

# define rooms and items - Bedroom 1 

door_a = {
    "name": "door a",
    "type": "door",
}
cupboard_b = {
    "name": "cupboard b",
    "type": "cupboard",
}

padlock_b = {
  "name": "padlock b",
  "type": "padlock",
  "code": int(712),
}


door_b = {
    "name": "door b",
    "type": "door",
}

door_c = {
    "name": "door c",
    "type": "door",
}

key_b = {
    "name": "key for door b",
    "type": "key",
    "target": door_b,
}

queen_bed = {
    "name": "queen bed",
    "type": "furniture",
}

bedroom_1 = {
    "name": "bedroom_1",
    "type": "room",
    "image": "Bedroom 1.png"
}




# define rooms and items - Bedroom 2 

double_bed = {
    "name": "double bed",
    "type": "furniture",
}
cupboard_c = {
    "name": "cupboard c",
    "type": "cupboard",
}

dresser = {
    "name": "dresser",
    "type": "furniture",
}
padlock_c = {
  "name": "padlock c",
  "type": "padlock",
  "code": int(291),
}

door_b = {
    "name": "door b",
    "type": "door",
}


key_c = {
    "name": "key for door c",
    "type": "key",
    "target": door_c,
}


bedroom_2 = {
    "name": "bedroom_2",
    "type": "room",
    "image": "Bedroom_2.png"
}




# define rooms and items - Living Room

dining_table = {
    "name": "dining table",
    "type": "table",
}

door_c = {
    "name": "door c",
    "type": "door",
}
cupboard_d = {
    "name": "cupboard d",
    "type": "cupboard",
}

door_d = {
    "name": "door d",
    "type": "door",
}
padlock_d = {
  "name": "padlock d",
  "type": "padlock",
  "code": int(666),
}

living_room = {
    "name": "living room",
    "type": "room",
    "image":"Livingroom.png"
}

outside = {
  "name": "outside",
  "image":"congrats.png"
}


key_d = {
    "name": "key for door d",
    "type": "key",
    "target": door_d,
}

all_rooms = [game_room, bedroom_1, bedroom_2, living_room, outside]

all_doors = [door_a, door_b, door_c, door_d]


##DRAWER MESSAGGES
draw_1_a="You find a photography with THREE people smiling"
draw_2_a="Inside you find a number EIGHT billiard ball"
draw_3_a="Inside you find a calendary with a mark on the Fifth day of the month"
draw_1_b="You find a photography with the SEVEN dwarves"
draw_2_b="You find just ONE candle"
draw_3_b="You find a COUPLE of earings"
draw_1_c="You find a COUPLE of earings"
draw_2_c="You find a a note with just IX written"
draw_3_c="You find just ONE candle"
draw_1_d="It's empty"
draw_2_d="It's empty"
draw_3_d="you find a photography of the DEVIL"

# define which items are related

object_relations = {
    "game room": [couch, piano, door_a,cupboard_a,padlock_a],
    "piano": [key_a],
   # "outside": [door_a],
    "door a": [game_room, bedroom_1],
    "bedroom_1": [queen_bed, door_b, door_c,padlock_b,door_a,cupboard_b],
    "queen bed": [key_b],
    #"outside": [door_b, door_c],
    "door b": [bedroom_1, bedroom_2],
    "door c": [bedroom_1, living_room],
    "bedroom_2": [dresser, double_bed, door_b,padlock_c,cupboard_c],
    "double bed":[key_c],
    "dresser": [key_d],
    #"outside": [door_b],
    "living room": [door_d, dining_table,padlock_d,door_c,cupboard_d],
    "outside": [door_d],
    "door d": [living_room, outside],
    "cupboard a" : [draw_1_a, draw_2_a, draw_3_a],
    "cupboard b" : [draw_1_b, draw_2_b, draw_3_b],
    "cupboard c" : [draw_1_c, draw_2_c, draw_3_c],
    "cupboard d" : [draw_1_d, draw_2_d, draw_3_d],
    
}


# define game state. Do not directly change this dict. 
# Instead, when a new game starts, make a copy of this
# dict and use the copy to store gameplay state. This 
# way you can replay the game multiple times.

INIT_GAME_STATE = {
    "current_room": game_room,
    "keys_collected": [],
    "target_room": outside,
    "padlock trials" : int(0),
    "padlock open" : bool(False), # True= the padblock is opened and False= the padlock is closed
    "padlock collected":[],#It will store string values. With names of padlocks


}

def show_image(room):
    
    image_path = room["image"]

    screen_width = 748
    screen_height = 373

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Earth Quake Game ")

   # game_room_image = None
   # if room["name"] == "Game Room":
    game_room_image = pygame.image.load(image_path)
    game_room_image = pygame.transform.scale(game_room_image,(screen_width, screen_height))
#     #elif room["name"] == "Bedroom_1":
#         bedroom_1_image = pygame.image.load(image_path)
#         bedroom_1_image = pygame.transform.scale(bedroom_1_image,(screen_width, screen_height))
#    # elif room["name"] == "Bedroom_2":
#         bedroom_2_image = pygame.image.load(image_path)
#         bedroom_2_image = pygame.transform.scale(bedroom_2_image,(screen_width, screen_height))
#    # elif room["name"] == "Dining_Room":
#         dining_room_image = pygame.image.load(image_path)
#         dining_room_image = pygame.transform.scale(dining_room_image,(screen_width, screen_height))
    #else:
     #   print("Invalid room name")
    #  return

    # game_room_image:
    screen.blit(game_room_image, (0, 0))
    # elif bedroom_1_image:
    #     screen.blit(bedroom_1_image, (0, 0))
    # elif bedroom_2_image:
    #     screen.blit(bedroom_2_image, (0, 0))
    # elif dining_room_image:
    #     screen.blit(dining_room_image, (0, 0))
    
    pygame.display.update()
    time.sleep(10)
    pygame.display.quit()
    return None

def linebreak():
    """
    Print a line break
    """
    print("\n\n")
def cupboard_examine(room,item_name):
  
  print("You are exminating this cupboard. It looks quite old." )
  print( "It has 3 drawers, you could open them" )
  print("DRAWER 1  -   DRAWER  2  -  DRAWER 3" )
  answer='yes'
  while answer=='yes':
    answer=input("Do you want to open some drawer?. Type 'yes' or 'no'").strip() 
    if answer=='yes':
      drawer_str = input("Type 1 ,2 or 3").strip()
      drawer_int = int(drawer_str)
      if drawer_int==1:
        print(object_relations[item_name][0])
      elif drawer_int==2:
       print(object_relations[item_name][1])
      elif drawer_int==3:
        print(object_relations[item_name][2])
      else :
        print("Sorry but I don´t understand your input.")

    elif answer=='no':
      play_room(room)
    else :
      print("Sorry,but I don not understand you")

def padlock_open(item_name,correct_code):

  current_room = game_state["current_room"]
  current_room_str= current_room["name"]
  game_state["padlock collected"].append(item_name)
  trials = game_state["padlock trials"]
  if trials==3:
    print("Sorry, the padlock is blocked forever. You will die in terrible suffering.")
    print("Enjoy!")
  elif trials<3:
    print("This padlock have 3 digits to get it unblocked.")
    print("But there is a small mesagge on its back.")
    print("YOU JUST HAVE 3 TRIALS TO OPEN IT. IF YOU CANNOT FIND THE ANSWER YOU WILL DIE IN THIS ROOM")
    print("And you just have ", (3-trials) , "left")
    print("MUAHAHAHHAHAA")
       
    intended_action=input("Do you want to unblock it? Type'yes' or 'no'").strip()
    if intended_action=="no":
      play_room(current_room)
        
    elif intended_action=="yes": 
      code_entered=""  
      while type(code_entered)!= int:
      
        code_entered=input("Please enter a number with 3 digits").strip() 
        try:
          code_entered=int(code_entered)
        except:
          print("That is not an integer")

      if int( code_entered)== correct_code :
        print("Congrats, you have open the padlock")
        game_state["padlock trials"]=int(0)
        if item_name not in game_state["padlock collected"]:
          game_state["padlock collected"].append(item_name["name"])
          
      elif correct_code!=code_entered:
        trials+=1
        game_state["padlock trials"]=trials
        print ("INCORRECT CODE")
        padlock_open(item_name, correct_code)
                
      else :
        print("Sorry, but I do not understand you answer")
        padlock_open(item_name, correct_code)  
                        

def start_game():
    """
    Start the game
    """
    print("""“You are a seismic scientist, and you are in Lisbon on duty, because your team received a sign through a new AI machine that 
    
the next earthquake will happen this month. 

You just woke up feeling what you know is a sism around 4.2(ritcher) but you know that this one will be followed 

by another one…. 9.0(ritcher) or more!!!!! 

You know you have about one hour to escape this building. 

Is your first day, and you rented an Airbnb, so you don't know all the furniture well yet. 

Can you escape before the next sism? 

Good luck!! “""")
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
        show_image(room)
    else:
        print("You are now in " + game_state["current_room"]["name"])
        intended_action = input("What would you like to do? Type 'explore' or 'examine'?").strip()
        if intended_action == "explore":
            explore_room(room)
            show_image(room)
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
    print("You explore the room. This is " + room["name"] + ". You find " + ", ".join(items))

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
    output = ""
    for item in  object_relations[current_room["name"]]:
      if item["type"]== "padlock":
       current_padlock = item

    for item in object_relations [current_room["name"]]:
      if(item["name"] == item_name):
            print( "You examine " + item_name + ". ")
            if(item["type"] == "door"):
                have_key = False
                for key in game_state["keys_collected"]:
                    if(key["target"] == item):
                        have_key = True
                if(have_key) and current_padlock in game_state["padlock collected"]:
                  next_room = get_next_room_of_door(item, current_room)
                elif(have_key):
                    print("You unlock it with a key you have." )
                    print(output)
                    
                    if  current_padlock in game_state["padlock collected"]:
                        output="You have opened both: door and padlock"
                        next_room = get_next_room_of_door(item, current_room)
                    else:  
                        print("Sorry. you have open the door but there is still a padlock blocking it")   
                       
                else:
                    output += "It is locked but you don't have the key."
            elif (item["type"] == "padlock"):
              correct_code= item["code"]
              padlock_open(item,correct_code)
              last_padlock=item["name"]
              
            elif (item["type"] == "cupboard"):
              cupboard_examine(current_room,item_name)
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
        play_room(next_room)
    else:
        play_room(current_room)
game_state = INIT_GAME_STATE.copy()

start_game()