#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# import libraries
from pathlib import Path
import random

import playsound as ps
from playsound import playsound

from PIL import Image


# In[ ]:


#Questions & answers

question_a = {
    "name": "Question a",
    "type": "question",
    "correct answer": "a"
}

answers_a = {
    "a": "Spanish",
    "b": "Italian",
    "c": "French"
}

question_b = {
    "name": "Question b",
    "type": "question",
    "correct answer": "b"
}

answers_b = {
    "a": "Potato",
    "b": "Rice",
    "c": "Bread"
}

question_c = {
    "name": "Question c",
    "type": "question",
    "correct answer": "a"
}

answers_c = {
    "a": "Whale",
    "b": "Elephant",
    "c": "Rhinoceros"
}

question_d = {
    "name": "Question d",
    "type": "question",
    "correct answer": "c"
}

answers_d = {
    "a": "Water",
    "b": "Iron",
    "c": ""
}

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
    "question": question_a
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


door_blue = {
    "name": "door blue",
    "type": "door",
}

door_pink = {
    "name": "door pink",
    "type": "door",
}

door_red = {
    "name": "door red",
    "type": "door",
}

door_black = {
    "name": "door black",
    "type": "door",
}

door_white = {
    "name": "door white",
    "type": "door",
}

key_b = {
    "name": "key for door b",
    "type": "key",
    "target": door_b,
    "question": question_b
}

key_c = {
    "name": "key for door c",
    "type": "key",
    "target": door_c,
    "question": question_c
}

key_d = {
    "name": "key for door d",
    "type": "key",
    "target": door_d,
    "question": question_d
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

ghost_room = {
    "name": "Ghost Room",
    "type": "room"
}

#all_rooms = [game_room, bedroom_1, bedroom_2, living_room, outside]

#all_doors = [door_a, door_b, door_c, door_d]

# define which items/rooms are related

object_relations = {
    "game room": [couch, piano, door_a],
    "piano": [key_a],
    "Bed Room 1": [queen_bed, door_a, door_b, door_c],
    "Queen Bed": [key_b],
    "Bed Room 2": [double_bed, dresser, door_b],
    "Double Bed": [key_c],
    "Dresser": [key_d],
    "Living Room": [dining_table, door_c, door_d],
    "Ghost Room": [door_blue, door_pink, door_red, door_black, door_white],
    "outside": [door_d],
    "door a": [game_room, bedroom_1],
    "door b": [bedroom_1, bedroom_2],
    "door c": [bedroom_1, living_room],
    "door d": [living_room, outside],        
    "key a": [question_a],
    "Question a": [answers_a],
    "key b": [question_b],
    "Question b": [answers_b],
    "key c": [question_c],
    "Question c": [answers_c],
    "key d": [question_d],
    "Question d": [answers_d]    
}

# define game state. Do not directly change this dict. 
# Instead, when a new game starts, make a copy of this
# dict and use the copy to store gameplay state. This 
# way you can replay the game multiple times.

# Added language, hard_scape and escape door

INIT_GAME_STATE = {
    "language": 'en',
    "current_room": game_room,
    "keys_collected": [],
    "hard_scape": 0,
    "target_room": outside,
    "escape door": door_blue
}

    


# In[ ]:


#Creating the Multi Language dictionaries

#English dictionary

lang_texts_en = {}
lang_texts_en['yes'] = 'yes'
lang_texts_en['no'] = 'no'
lang_texts_en['explore'] = 'explore'
lang_texts_en['examine'] = 'examine'
lang_texts_en['integer'] = 'Please type only the number of the options'
lang_texts_en['intro'] = '''You wake up on a couch and find yourself in a strange house with no windows which you have never been to before. You don't remember why you are here and what had happened before. You feel some unknown danger is approaching and you must get out of the house, NOW!'''
lang_texts_en['escape'] = 'RUN! And do not come back again!\n\nCongrats! You escaped the room!'
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
lang_texts_en['Question a'] = 'What nationality was Columbus believed to be?'
lang_texts_en['Question b'] = 'What is the most consumed food in the world?'
lang_texts_en['Question c'] = 'What is the largest mammal in the world?'
lang_texts_en['Question d'] = 'What weighs more than 1 kg of water or 1kg of iron?'
lang_texts_en['door blue'] = 'Door Blue'
lang_texts_en['door pink'] = 'Door Pink'
lang_texts_en['door red'] = 'Door Red'
lang_texts_en['door black'] = 'Door Black'
lang_texts_en['door white'] = 'Door White'
lang_texts_en['ghost quiz'] = 'Ghost Quiz'
lang_texts_en['Question a correct'] = 'Right... Keep looking for the exit...'
lang_texts_en['Question a failed'] = 'You wont scape... ever'
lang_texts_en['Question b correct'] = 'You can go... for now...'
lang_texts_en['Question b failed'] = 'Nice try...'
lang_texts_en['Question c correct'] = 'True...Who would think a mammal can live underwater?...'
lang_texts_en['Question c failed'] = 'You will not be allowed to go anywhere...'
lang_texts_en['Question d correct'] = 'Clever...'
lang_texts_en['Question d failed'] = 'Hehehehe...'
lang_texts_en['choose_door'] = 'As you failed in your answers... it is time to choose a door.'
lang_texts_en['correct_door'] = 'Congratulations! You can live for one day more'
lang_texts_en['wrong_door'] = 'Time to stay here... FOREVER!'
lang_texts_en['Spanish'] = 'Spanish'
lang_texts_en['Italian'] = 'Italian'
lang_texts_en['French'] = 'French'
lang_texts_en['Potato'] = 'Potato'
lang_texts_en['Rice'] = 'Rice'
lang_texts_en['Bread'] = 'Bread'
lang_texts_en['Whale'] = 'Whale'
lang_texts_en['Elephant'] = 'Elephant'
lang_texts_en['Rhinoceros'] = 'Rhinoceros'
lang_texts_en['Water'] = 'Water'
lang_texts_en['Iron'] = 'Iron'
lang_texts_en[''] = ''


#Spanish dictionary

lang_texts_es = {}
lang_texts_es['yes'] = 'sí'
lang_texts_es['no'] = 'no'
lang_texts_es['explore'] = 'explorar'
lang_texts_es['examine'] = 'examinar'
lang_texts_es['integer'] = 'Por favor teclea solamente números de las opciones'
lang_texts_es['intro'] = 'Te despiertas en un sofá y te encuentras en una casa extraña sin ventanas en la que nunca has estado antes. No recuerdas por qué estás aquí y qué había sucedido antes. Sientes que se acerca un peligro desconocido y debes salir de la casa, ¡YA!'
lang_texts_es['escape'] = '¡CORRE! ¡y no vuelvas más!\n\n¡Felicidades! ¡Has escapado!'
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
lang_texts_es['Question a'] = '¿De qué nacionalidad se creía que era Colón?'
lang_texts_es['Question b'] = '¿Cuál es el alimento más consumido en el mundo?'
lang_texts_es['Question c'] = '¿Cuál es el mamífero más grande del mundo?'
lang_texts_es['Question d'] = '¿Qué pesa más, 1 kg de agua o 1 kg de hierro?'
lang_texts_es['door blue'] = 'Puerta Azul'
lang_texts_es['door pink'] = 'Puerta Rosa'
lang_texts_es['door red'] = 'Puerta Roja'
lang_texts_es['door black'] = 'Puerta Negra'
lang_texts_es['door white'] = 'Puerta Blanca'
lang_texts_es['ghost quiz'] = 'Acertijo Fantasma'
lang_texts_es['Question a correct'] = 'Bien... Sigue buscando la salida...'
lang_texts_es['Question a failed'] = 'Tú no escaparás... nunca'
lang_texts_es['Question b correct'] = 'Puedes irte... por ahora...'
lang_texts_es['Question b failed'] = 'Buen intento...'
lang_texts_es['Question c correct'] = 'Cierto... ¿Quién pensaría que un mamífero puede vivir bajo el agua?...'
lang_texts_es['Question c failed'] = 'No se te permitirá ir a ningún lado...'
lang_texts_es['Question d correct'] = 'Inteligente...'
lang_texts_es['Question d failed'] = 'Jejejeje...'
lang_texts_es['choose_door'] = 'Como fallaste en tus respuestas... es hora de elegir una puerta.'
lang_texts_es['correct_door'] = '¡Felicidades! Puedes vivir un día más'
lang_texts_es['wrong_door'] = 'Es hora de quedarse aquí... ¡PARA SIEMPRE!'
lang_texts_es['Spanish'] = 'Española'
lang_texts_es['Italian'] = 'Italiana'
lang_texts_es['French'] = 'Francesa'
lang_texts_es['Potato'] = 'Patata'
lang_texts_es['Rice'] = 'Arroz'
lang_texts_es['Bread'] = 'Pan'
lang_texts_es['Whale'] = 'Ballena'
lang_texts_es['Elephant'] = 'Elefante'
lang_texts_es['Rhinoceros'] = 'Rinoceronte'
lang_texts_es['Water'] = 'Agua'
lang_texts_es['Iron'] = 'Hierro'
lang_texts_es[''] = ''

#Italian dictionary

lang_texts_it = {}
lang_texts_it['yes'] = 'si'
lang_texts_it['no'] = 'no'
lang_texts_it['explore'] = 'esplorare'
lang_texts_it['examine'] = 'esaminare'
lang_texts_it['integer'] = 'Per favore, digita solo il numero delle opzioni disponibili'
lang_texts_it['intro'] = 'Ci si sveglia su un divano e ci si ritrova in una strana casa senza finestre in cui non si è mai stati prima. Non ricordate perché siete qui e cosa è successo prima. Sentite che un pericolo sconosciuto si sta avvicinando e dovete uscire dalla casa, ORA!'
lang_texts_it['escape'] = 'CORRERE! E non tornare più!\n\nCongratulazioni! Sei riuscito a fuggire dalla stanza!'
lang_texts_it['in'] = 'Ora siete nella '
lang_texts_it['next_room'] = 'Vuoi andare nella prossima stanza?'
lang_texts_it['examine_do'] = 'Cosa desideri esaminare?'
lang_texts_it['repeat'] = "Non sono sicuro di cosa intendi. Scegli un'opzione valida."
lang_texts_it['explore_do'] = 'Esplorate la stanza. Questo è '
lang_texts_it['find'] = 'Tu trovi '
lang_texts_it['you_examine'] = 'Tu esamini '
lang_texts_it['unlock'] = 'La apri con una chiave che possiedi.'
lang_texts_it['locked'] = "È chiusa a chiave ma non avete la chiave."
lang_texts_it['nothing'] = "Non c'è nulla di interessante"
lang_texts_it['none'] = "L'oggetto richiesto non si trova nella stanza attuale."
lang_texts_it['option'] = 'Opzione:'
lang_texts_it['select'] = 'Seleziona una opzione:'
lang_texts_it['selected'] = 'Opzione selezionata: '
lang_texts_it['no_valid'] = ' Selezionare un numero valido'
lang_texts_it['couch'] = 'Divano'
lang_texts_it['piano'] = 'Pianoforte'
lang_texts_it['door a'] = 'porta a'
lang_texts_it['Queen Bed'] = 'Letto matrimoniale'
lang_texts_it['door b'] = 'porta b'
lang_texts_it['door c'] = 'porta c'
lang_texts_it['Double Bed'] = 'Letto doppio'
lang_texts_it['Dresser'] = 'Comò'
lang_texts_it['Dining Table'] = 'Tavolo da pranzo'
lang_texts_it['door d'] = 'porta d'
lang_texts_it['game room'] = 'Sala giochi'
lang_texts_it['Bed Room 1'] = 'Camera da letto 1'
lang_texts_it['Bed Room 2'] = 'Camera da letto 2'
lang_texts_it['Living Room'] = 'Soggiorno'
lang_texts_it['outside'] = 'Fuori'
lang_texts_it['key for door a'] = 'chiave per porta a'
lang_texts_it['key for door b'] = 'chiave per porta b'
lang_texts_it['key for door c'] = 'chiave per porta c'
lang_texts_it['key for door d'] = 'chiave per porta d'
lang_texts_it['Question a'] = 'Di quale nazionalità si credeva fosse Colombo?'
lang_texts_it['Question b'] = 'Qual è il cibo più consumato al mondo?'
lang_texts_it['Question c'] = 'Qual è il mammifero più grande del mondo?'
lang_texts_it['Question d'] = 'Che pesa di più, 1 kg di acqua o 1 kg di ferro?'
lang_texts_it['door blue'] = 'Porta Blu'
lang_texts_it['door pink'] = 'Porta Rosa'
lang_texts_it['door red'] = 'Porta Rossa'
lang_texts_it['door black'] = 'Porta Nera'
lang_texts_it['door white'] = 'Porta Bianca'
lang_texts_it['ghost quiz'] = "L'enigma dei fantasmi"
lang_texts_it['Question a correct'] = "Bene... Continua a cercare l'uscita..."
lang_texts_it['Question a failed'] = 'Non fuggirai... mai'
lang_texts_it['Question b correct'] = 'Puoi andare... per ora...'
lang_texts_it['Question b failed'] = 'Bel tentativo...'
lang_texts_it['Question c correct'] = "Vero...Chi penserebbe che un mammifero possa vivere sott'acqua?..."
lang_texts_it['Question c failed'] = 'Non ti sarà permesso andare da nessuna parte...'
lang_texts_it['Question d correct'] = 'Intelligente...'
lang_texts_it['Question d failed'] = 'ehehehehe...'
lang_texts_it['choose_door'] = 'Dal momento che hai fallito le tue risposte... è ora di scegliere una porta.'
lang_texts_it['correct_door'] = 'Congratulazioni! puoi vivere un altro giorno'
lang_texts_it['wrong_door'] = 'È ora di restare qui... PER SEMPRE!'
lang_texts_it['Spanish'] = 'Spagnolo'
lang_texts_it['Italian'] = 'Italiano'
lang_texts_it['French'] = 'Francese'
lang_texts_it['Potato'] = 'Patata'
lang_texts_it['Rice'] = 'Riso'
lang_texts_it['Bread'] = 'Pane'
lang_texts_it['Whale'] = 'Balena'
lang_texts_it['Elephant'] = 'Elefante'
lang_texts_it['Rhinoceros'] = 'Rinoceronte'
lang_texts_it['Water'] = 'Acqua'
lang_texts_it['Iron'] = 'Ferro'
lang_texts_it[''] = ''

#Portuguese dictionary

lang_texts_pt = {}
lang_texts_pt['yes'] = 'sim'
lang_texts_pt['no'] = 'não'
lang_texts_pt['explore'] = 'explorar'
lang_texts_pt['examine'] = 'examinar'
lang_texts_pt['integer'] = 'Por favor, digite apenas o número das opções'
lang_texts_pt['intro'] = 'Você acorda em um sofá e se encontra em uma casa estranha, sem janelas, na qual nunca esteve antes. Você não se lembra por que está aqui e o que aconteceu antes. Você sente que algum perigo desconhecido está se aproximando e você deve sair de casa, AGORA!'
lang_texts_pt['escape'] = 'CORRE! E não volte mais!\n\nParabéns! Você escapou do quarto!'
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
lang_texts_pt['Question a'] = 'Qual era a nacionalidade de Colombo?'
lang_texts_pt['Question b'] = 'Qual é o alimento mais consumido no mundo?'
lang_texts_pt['Question c'] = 'Qual é o maior mamífero do mundo?'
lang_texts_pt['Question d'] = 'O que pesa mais, 1 kg de água ou 1 kg de ferro?'
lang_texts_pt['door blue'] = 'Porta Azul'
lang_texts_pt['door pink'] = 'Porta Rosa'
lang_texts_pt['door red'] = 'Porta Vermelha'
lang_texts_pt['door black'] = 'Porta Preta'
lang_texts_pt['door white'] = 'Porta Branca'
lang_texts_pt['ghost quiz'] = 'Teste Fantasma'
lang_texts_pt['Question a correct'] = 'Ok... Continue procurando a saída...'
lang_texts_pt['Question a failed'] = 'Você não vai escapar... nunca'
lang_texts_pt['Question b correct'] = 'Você pode ir... por enquanto...'
lang_texts_pt['Question b failed'] = 'Boa tentativa...'
lang_texts_pt['Question c correct'] = "Certo... Quem pensaria que um mamífero poderia viver debaixo d'água?..."
lang_texts_pt['Question c failed'] = 'Você não poderá ir a lugar nenhum...'
lang_texts_pt['Question d correct'] = 'Inteligente...'
lang_texts_pt['Question d failed'] = 'Hehehehe...'
lang_texts_pt['choose_door'] = 'Já que você falhou em suas respostas... é hora de escolher uma porta.'
lang_texts_pt['correct_door'] = 'Parabéns! você pode viver outro dia'
lang_texts_pt['wrong_door'] = 'É hora de ficar aqui... PARA SEMPRE!'
lang_texts_pt['Spanish'] = 'Espanhol'
lang_texts_pt['Italian'] = 'Italiano'
lang_texts_pt['French'] = 'Francesa'
lang_texts_pt['Potato'] = 'Batata'
lang_texts_pt['Rice'] = 'Arroz'
lang_texts_pt['Bread'] = 'Pão'
lang_texts_pt['Whale'] = 'Baleia'
lang_texts_pt['Elephant'] = 'Elefante'
lang_texts_pt['Rhinoceros'] = 'Rinoceronte'
lang_texts_pt['Water'] = 'Água'
lang_texts_pt['Iron'] = 'Ferro'
lang_texts_pt[''] = ''

#Main Dictionary to choose which dictionary we will need


lang_game = {}
lang_game['en'] = ['english',lang_texts_en]
lang_game['es'] = ['spanish',lang_texts_es]
lang_game['it'] = ['italian',lang_texts_it]
lang_game['pt'] = ['portuguese',lang_texts_pt]


# In[ ]:


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


# In[ ]:


def ghost_quiz(key):
    """
    Function to ask a question every time that find a key
    Every fail increases the dificulty to escape     
    """
    answer = selectFromDict({lang_game[game_state["language"]][1][value]:key for key,value in object_relations[key['question']['name']][0].items()},lang_game[game_state["language"]][1][key['question']['name']])
    
    if answer == key['question']['correct answer']:
        print(lang_game[game_state["language"]][1][key['question']['name'] + ' correct'])
    else:
      print(lang_game[game_state["language"]][1][key['question']['name'] + ' failed'])
      game_state['hard_scape'] += 1
        
def ghost_doors():  
    """
    Function to give the chance to choose a door when failed any question

    """
    
    if (game_state["hard_scape"]>0):
        print(lang_game[game_state["language"]][1]['choose_door'])

        game_state['escape door'] = object_relations['Ghost Room'][random.randrange(game_state["hard_scape"]+1)]
        
        #Test for the escape door
        #print(game_state['escape door'])

        dict_escape_room = {}
        for i in range(game_state["hard_scape"]+1):    
            dict_escape_room[lang_game[game_state["language"]][1][object_relations['Ghost Room'][i]['name']]] = i               

        if (game_state['escape door'] == object_relations['Ghost Room'][selectFromDict(dict_escape_room,'')]):
            print(lang_game[game_state["language"]][1]['correct_door'])
            play_sound('victory')
        else:
            print(lang_game[game_state["language"]][1]['wrong_door'])
            play_sound('fail')
    else:        
        print(lang_game[game_state["language"]][1]['escape'])    
        play_sound('victory')


# In[ ]:


def play_sound(sound):
    """
    Play the sound selected
    """
    
    if (sound == 'piano'):
        playsound(Path("sounds/piano_sound_effect.mp3"))
    elif (sound == 'victory'):
        playsound(Path("sounds/Victory_sound.mp3"))
    elif (sound == 'fail'): 
        playsound(Path("sounds/Fail_sound_effect.mp3"))


# In[ ]:


def show_room(room):
    """
    Show an image related to the room
    """
    
    if (room["name"].lower() == game_room['name'].lower()):        
        img = Image.open(Path('images/Game_room.png'))
        img.show()
    elif (room["name"].lower() == bedroom_1['name'].lower()):
        img = Image.open(Path('images/Bedroom_1.png'))
        img.show()
    elif (room["name"].lower() == bedroom_2['name'].lower()):
        img = Image.open(Path('images/Bedroom_2.png'))
        img.show()
    elif (room["name"].lower() == living_room['name'].lower()):
        img = Image.open(Path('images/Living_room.png'))
        img.show()
    
           


# In[ ]:


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
    
    if(game_state["current_room"] == game_state["target_room"]):
        ghost_doors()        
    
def play_room(room):
    """
    Play a room. First check if the room being played is the target room.
    If it is, the game will end with success. Otherwise, let player either 
    explore (list all items in this room) or examine an item found here.
    """
     
    show_room(room)
    
    while game_state['current_room'] != game_state['target_room']:
        linebreak()        
        
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
            key_found = False
            
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
                if(item["name"] == 'piano'):
                    play_sound('piano')
                
                if(item["name"] in object_relations and len(object_relations[item["name"]])>0):
                    item_found = object_relations[item["name"]].pop()
                    game_state["keys_collected"].append(item_found)
                    
                    key_found = True
                    
                    output += lang_game[game_state["language"]][1]['find'] + lang_game[game_state["language"]][1][item_found["name"]] + "."
                else:
                    output += lang_game[game_state["language"]][1]['nothing']
                                
            print(output)
            
            if (key_found):                
                print("\n" + lang_game[game_state["language"]][1]['ghost quiz'] + "\n")
                ghost_quiz(item_found)
                    
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


# In[ ]:


game_state = INIT_GAME_STATE.copy()

start_game()

