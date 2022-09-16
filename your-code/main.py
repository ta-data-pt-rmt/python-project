#!/usr/bin/env python
# coding: utf-8

# In[1]:


# define rooms and items

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

game_room = {
    "name": "game room",
    "type": "room",
}

outside = {
  "name": "outside"
}

#New Rooms

door_b = {
    "name": "door b",
    "type": "door",
}

door_c = {
    "name": "door c",
    "type": "door",
}

door_d = {
    "name": "door d",
    "type": "door",
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

queen_bed = {
    "name": "Queen Bed",
    "type": "furniture",
}

double_bed = {
    "name": "Double Bed",
    "type": "furniture",
}

dresser = {
    "name": "Dresser",
    "type": "furniture",
}

dining_table = {
    "name": "Dining Table",
    "type": "furniture",
}

bedroom_1 = {
    "name": "Bed Room 1",
    "type": "room",
}

bedroom_2 = {
    "name": "Bed Room 2",
    "type": "room",
}

living_room = {
    "name": "Living Room",
    "type": "room",
}


#all_rooms = [game_room, bedroom_1, bedroom_2, living_room, outside]

#all_doors = [door_a, door_b, door_c, door_d]

# define which items/rooms are related

object_relations = {
    "game room": [couch, piano, door_a],
    "piano": [key_a],
    "Bed Room 1": [queen_bed, door_b, door_c],
    "Queen Bed": [key_b],
    "Bed Room 2": [double_bed, dresser, door_b],
    "Double Bed": [key_c],
    "Dresser": [key_d],
    "Living Room": [dining_table, door_d],
    "outside": [door_d],
    "door a": [game_room, bedroom_1],
    "door b": [bedroom_1, bedroom_2],
    "door c": [bedroom_1, living_room],
    "door d": [living_room, outside]
}

# define game state. Do not directly change this dict. 
# Instead, when a new game starts, make a copy of this
# dict and use the copy to store gameplay state. This 
# way you can replay the game multiple times.

# Added language

INIT_GAME_STATE = {
    "language": 'en',
    "current_room": game_room,
    "keys_collected": [],
    "target_room": outside
}


# In[2]:


#Creating the Multi Language dictionaries

#English dictionary

lang_texts_en = {}
lang_texts_en['yes'] = 'yes'
lang_texts_en['no'] = 'no'
lang_texts_en['explore'] = 'explore'
lang_texts_en['examine'] = 'examine'
lang_texts_en['integer'] = 'Please type only the number of the options'
lang_texts_en['intro'] = '''You wake up on a couch and find yourself in a strange house with no windows which you have never been to before. You don't remember why you are here and what had happened before. You feel some unknown danger is approaching and you must get out of the house, NOW!'''
lang_texts_en['escape'] = 'Congrats! You escaped the room!'
lang_texts_en['in'] = 'You are now in '
lang_texts_en['next_room'] = 'Do you want to go to the next room?'
lang_texts_en['examine_do'] = 'What would you like to examine?'
lang_texts_en['repeat'] = "Not sure what you mean. Choose a valid option."
lang_texts_en['explore_do'] = 'You explore the room. This is '
lang_texts_en['find'] = 'You find '
lang_texts_en['you_examine'] = 'You examine '
lang_texts_en['unlock'] = 'You unlock it with a key you have.'
lang_texts_en['locked'] = "It is locked but you don't have the key."
lang_texts_en['nothing'] = "There isn't anything interesting about it."
lang_texts_en['none'] = 'The item you requested is not found in the current room.'
lang_texts_en['option'] = 'Option:'
lang_texts_en['select'] = 'Select one option:'
lang_texts_en['selected'] = 'Selected option: '
lang_texts_en['no_valid'] = 'Please select a valid number'
lang_texts_en['couch'] = 'couch'
lang_texts_en['piano'] = 'piano'
lang_texts_en['door a'] = 'door a'
lang_texts_en['Queen Bed'] = 'Queen Bed'
lang_texts_en['door b'] = 'door b'
lang_texts_en['door c'] = 'door c'
lang_texts_en['Double Bed'] = 'Double Bed'
lang_texts_en['Dresser'] = 'Dresser'
lang_texts_en['Dining Table'] = 'Dining Table'
lang_texts_en['door d'] = 'door d'
lang_texts_en['game room'] = 'Game room'
lang_texts_en['Bed Room 1'] = 'Bed Room 1'
lang_texts_en['Bed Room 2'] = 'Bed Room 2'
lang_texts_en['Living Room'] = 'Living Room'
lang_texts_en['outside'] = 'outside'
lang_texts_en['key for door a'] = 'key for door a'
lang_texts_en['key for door b'] = 'key for door b'
lang_texts_en['key for door c'] = 'key for door c'
lang_texts_en['key for door d'] = 'key for door d'

#Spanish dictionary

lang_texts_es = {}
lang_texts_es['yes'] = 'sí'
lang_texts_es['no'] = 'no'
lang_texts_es['explore'] = 'explorar'
lang_texts_es['examine'] = 'examinar'
lang_texts_es['integer'] = 'Por favor teclea solamente números de las opciones'
lang_texts_es['intro'] = 'Te despiertas en un sofá y te encuentras en una casa extraña sin ventanas en la que nunca has estado antes. No recuerdas por qué estás aquí y qué había sucedido antes. Sientes que se acerca un peligro desconocido y debes salir de la casa, ¡YA!'
lang_texts_es['escape'] = '¡Felicidades! ¡Has escapado!'
lang_texts_es['in'] = 'Estás en '
lang_texts_es['next_room'] = '¿Quieres ir a la siguiente habitación?'
lang_texts_es['examine_do'] = '¿Qué te gustaría examinar?'
lang_texts_es['repeat'] = "No estoy seguro de lo que quieres. Seleccionar una opción válida."
lang_texts_es['explore_do'] = 'Exploras la habitación. Esta es '
lang_texts_es['find'] = 'Encuentras '
lang_texts_es['you_examine'] = 'Tú examinas '
lang_texts_es['unlock'] = 'La abres con la llave que tú tienes.'
lang_texts_es['locked'] = "Está cerrada pero tú no tienes la llave."
lang_texts_es['nothing'] = "No se ve nada interesante"
lang_texts_es['none'] = 'El elemento que solició no se encuentra en la sala actual.'
lang_texts_es['option'] = 'Opción:'
lang_texts_es['select'] = 'Escoge una opción:'
lang_texts_es['selected'] = 'Opción escogida: '
lang_texts_es['no_valid'] = 'Por favor, escoge un número válido'
lang_texts_es['couch'] = 'sofá'
lang_texts_es['piano'] = 'piano'
lang_texts_es['door a'] = 'puerta a'
lang_texts_es['Queen Bed'] = 'Cama de matrimonio'
lang_texts_es['door b'] = 'puerta b'
lang_texts_es['door c'] = 'puerta c'
lang_texts_es['Double Bed'] = 'Cama Doble'
lang_texts_es['Dresser'] = 'Cómoda'
lang_texts_es['Dining Table'] = 'Mesa de comedor'
lang_texts_es['door d'] = 'puerta d'
lang_texts_es['game room'] = 'Habitación de juegos'
lang_texts_es['Bed Room 1'] = 'Habitación 1'
lang_texts_es['Bed Room 2'] = 'Habitación 2'
lang_texts_es['Living Room'] = 'Sala de estar'
lang_texts_es['outside'] = 'Fuera'
lang_texts_es['key for door a'] = 'llave para puerta a'
lang_texts_es['key for door b'] = 'llave para puerta b'
lang_texts_es['key for door c'] = 'llave para puerta c'
lang_texts_es['key for door d'] = 'llave para puerta d'

#Portuguese dictionary

lang_texts_pt = {}
lang_texts_pt['yes'] = 'sim'
lang_texts_pt['no'] = 'não'
lang_texts_pt['explore'] = 'explorar'
lang_texts_pt['examine'] = 'examinar'
lang_texts_pt['integer'] = 'Por favor, digite apenas o número das opções'
lang_texts_pt['intro'] = 'Você acorda em um sofá e se encontra em uma casa estranha, sem janelas, na qual nunca esteve antes. Você não se lembra por que está aqui e o que aconteceu antes. Você sente que algum perigo desconhecido está se aproximando e você deve sair de casa, AGORA!'
lang_texts_pt['escape'] = 'Parabéns! Você escapou do quarto!'
lang_texts_pt['in'] = 'Você está agora em '
lang_texts_pt['next_room'] = 'Você quer ir para a próxima sala?'
lang_texts_pt['examine_do'] = 'O que você gostaria de examinar?'
lang_texts_pt['repeat'] = "Não tenho certeza do que você quer dizer. Escolha uma opção válida."
lang_texts_pt['explore_do'] = 'Você explora a sala. Isto é '
lang_texts_pt['find'] = 'Você encontra '
lang_texts_pt['you_examine'] = 'Você examina '
lang_texts_pt['unlock'] = 'Você desbloqueia com uma chave que você tem.'
lang_texts_pt['locked'] = "Está trancado, mas você não tem a chave."
lang_texts_pt['nothing'] = "Não há nada de interessante nisso."
lang_texts_pt['none'] = 'O item solicitado não foi encontrado na sala atual.'
lang_texts_pt['option'] = 'Opção:'
lang_texts_pt['select'] = 'Selecione uma opção:'
lang_texts_pt['selected'] = 'Opção selecionada: '
lang_texts_pt['no_valid'] = 'Por favor, selecione um número válido'
lang_texts_pt['couch'] = 'sofá'
lang_texts_pt['piano'] = 'piano'
lang_texts_pt['door a'] = 'porta a'
lang_texts_pt['Queen Bed'] = 'Cama de casal'
lang_texts_pt['door b'] = 'porta b'
lang_texts_pt['door c'] = 'porta c'
lang_texts_pt['Double Bed'] = 'Cama Dupla'
lang_texts_pt['Dresser'] = 'Aparador'
lang_texts_pt['Dining Table'] = 'Mesa de jantar'
lang_texts_pt['door d'] = 'porta d'
lang_texts_pt['game room'] = 'Sala de jogos'
lang_texts_pt['Bed Room 1'] = 'Quarto 1'
lang_texts_pt['Bed Room 2'] = 'Quarto 2'
lang_texts_pt['Living Room'] = 'Sala de estar'
lang_texts_pt['outside'] = 'fora'
lang_texts_pt['key for door a'] = 'chave para porta a'
lang_texts_pt['key for door b'] = 'chave para porta b'
lang_texts_pt['key for door c'] = 'chave para porta c'
lang_texts_pt['key for door d'] = 'chave para porta d'


#Main Dictionary to choose which dictionary we will need


lang_game = {}
lang_game['en'] = ['english',lang_texts_en]
lang_game['es'] = ['spanish',lang_texts_es]
lang_game['pt'] = ['portuguese',lang_texts_pt]


# In[3]:


def selectFromDict(options, name=''):
    """
    Function to add options instead of writing
    """

    index = 0
    indexValidList = []
    print(name)
    print(lang_game[game_state["language"]][1]['select'])
    for optionName in options:
        index = index + 1
        indexValidList.extend([options[optionName]])
        print(str(index) + ') ' + optionName)
    inputValid = False
    while not inputValid:
        try:
            inputRaw = int(input(lang_game[game_state["language"]][1]['option']))
        
            inputNo = inputRaw - 1
            if inputNo > -1 and inputNo < len(indexValidList):
                selected = indexValidList[inputNo]              
                print(lang_game[game_state["language"]][1]['selected'] + list(options.keys())[list(options.values()).index(selected)])                                    
                inputValid = True
                break
            else:
                print(lang_game[game_state["language"]][1]['no_valid'])
        except ValueError:
            print(lang_game[game_state["language"]][1]['integer'])
    
    print('\n')
    
    return selected


# In[4]:


def linebreak():
    """
    Print a line break
    """
    print("\n\n")

def start_game():
    """
    Start the game
    """
        
        
    #game language selection
    
    game_state['language'] = (selectFromDict({value[0]:key for key,value in lang_game.items()},'Which language do you want to use?'))    
    
    #intro of the game    
    
    print(lang_game[game_state["language"]][1]['intro'])
    
    #create a loop because inside the play_room function could create problems the execution of the playroom recursively
    
    while game_state['current_room'] != game_state['target_room']:
        play_room(game_state["current_room"])            
    
    #print(game_state["current_room"])
    #print(game_state["target_room"])
    if(game_state["current_room"] == game_state["target_room"]):
        print(lang_game[game_state["language"]][1]['escape'])    
    
def play_room(room):
    """
    Play a room. First check if the room being played is the target room.
    If it is, the game will end with success. Otherwise, let player either 
    explore (list all items in this room) or examine an item found here.
    """
    
    #game_state["current_room"] = room
    #if(game_state["current_room"] == game_state["target_room"]):        
    #    print(lang_game[game_state["language"]][1]['escape'])
    
    #else:   
    while game_state['current_room'] != game_state['target_room']:
        print("\n")
        print(lang_game[game_state["language"]][1]['in'] + lang_game[game_state["language"]][1][room["name"]]) 

        intended_action = selectFromDict({lang_game[game_state["language"]][1]['examine']:'examine',lang_game[game_state["language"]][1]['explore']:'explore'})

        if intended_action == "explore":
            explore_room(room)

            #create loop ouside to prevent the execution of the function recursively 
            #play_room(room)
        elif intended_action == "examine":

            game_state["current_room"] = examine_item(selectFromDict({lang_game[game_state["language"]][1][items['name']]:items['name'] for items in object_relations[game_state['current_room']['name']]},lang_game[game_state["language"]][1]['examine_do']))
            if (game_state["current_room"] != room):
                return                
        else:

            print(lang_game[game_state["language"]][1]['repeat'])

            #create loop ouside to prevent the execution of the function recursively 
            #play_room(room)

        linebreak()

def explore_room(room):
    """
    Explore a room. List all items belonging to this room.
    """
     
    items = [lang_game[game_state["language"]][1][i["name"]] for i in object_relations[room["name"]]]
    
    print(lang_game[game_state["language"]][1]['explore_do'] + lang_game[game_state["language"]][1][room["name"]] + '. ' + lang_game[game_state["language"]][1]['find'] + ", ".join(items))

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
                        
            output = lang_game[game_state["language"]][1]['you_examine'] + lang_game[game_state["language"]][1][item_name] + ". "
            
            if(item["type"] == "door"):
                have_key = False
                                
                for key in game_state["keys_collected"]:
                    if(key["target"] == item):
                        have_key = True
                if(have_key):                    
                    output += lang_game[game_state["language"]][1]['unlock']
                    
                    next_room = get_next_room_of_door(item, current_room)
                else:                                        
                    output += lang_game[game_state["language"]][1]['locked']
            else:
                if(item["name"] in object_relations and len(object_relations[item["name"]])>0):
                    item_found = object_relations[item["name"]].pop()
                    game_state["keys_collected"].append(item_found)
                                        
                    output += lang_game[game_state["language"]][1]['find'] + lang_game[game_state["language"]][1][item_found["name"]] + "."
                else:
                    output += lang_game[game_state["language"]][1]['nothing']
            print(output)
            break

    if(output is None):        
        print(lang_game[game_state["language"]][1]['none'])
        
    if(next_room and selectFromDict({lang_game[game_state["language"]][1]['yes']:'yes',lang_game[game_state["language"]][1]['no']:'no'},lang_game[game_state["language"]][1]['next_room']) == 'yes'):
        #create loop ouside to prevent the execution of the function recursively 
        #play_room(next_room)
        #game_state["current_room"] = next_room
        return next_room
    else:
        #create loop ouside to prevent the execution of the function recursively 
        #play_room(current_room)
        return current_room


# In[5]:


game_state = INIT_GAME_STATE.copy()

start_game()


# In[ ]:




