
With the goal of creating a more reliable and interactive code, we made some modifications to the initial code. 'Therapac' is a mental health-promoting game designed to provide users with a therapeutic and engaging experience. We named it 'Therapac' to enhance its marketability.

Next, we list the changes made:


- Defined  multiple rooms (game_room, bedroom_1, bedroom_2, living_room, outside) and various furniture items (couch, piano, queen_bed, etc.).

- Defined multiple doors (door_a, door_b, door_c, door_d) and corresponding keys (key_a, key_b, key_c, key_d).

- Specified relationships between rooms, furniture, doors, and keys in the object_relations dictionary.

- Added error checking to ensure object definitions are correct and the game will not crash because of bad game settings, like forgetting to add items to object_relations, etc.


- Merged the two steps needed for the 'examine' step, to be in single command, so instead of writing 'examine' first, and then in another input to type 'piano', you can now type 'examine piano' which is easier for the player.


- Used of the OpenCV library to display a video in the application and created a function to display a video.
