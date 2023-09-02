# from player import *
from items import *
from doors import *
from rooms import *
from room_data import *

# First, create the Rooms of the Manor
def create_rooms():
    """Create the Rooms of the Manor using the  data stored in the all_rooms dictionary,
    storing each instance in the room_instances dictionary. Print statements for debugging."""
    # print('Creating rooms...')
    for room_key in all_rooms:
        room_data, room_type = all_rooms[room_key][0]
        # print(f'\nCreating {room_data[0]}...')
        if room_type == 'vanilla':
            room_instances[room_key] = Room(*room_data)
            # print(f'{room_instances[room_key]} created.')
        elif room_type == 'transformer':
            extra_data = all_rooms[room_key][1]
            room_instances[room_key] = Transformer(*room_data, **extra_data)
            # print(f'{room_instances[room_key]} created.')
        elif room_type == 'dangerstairwell':
            extra_data = all_rooms[room_key][1]
            room_instances[room_key] = DangerStairwell(*room_data, **extra_data)
            # print(f'{room_instances[room_key]} created.')
    # print('\nRoom creation complete.')

create_rooms()

# Create easy references to each room created for use in creating doors and items
foyer = room_instances['foyer']
main_hall = room_instances['main_hall']
laboratory = room_instances['laboratory']
hall_of_easts = room_instances['hall_of_easts']
hallway = room_instances['hallway']
library = room_instances['library']
tower = room_instances['tower']
outside = room_instances['outside']
death = room_instances['death']
placeholder = room_instances['placeholder']

# Next create the doors
# Storing all_doors in separate file and importing always raises an error, still trying to figure that out
all_doors = {
'Foyer':
{
    '1': [[('north', main_hall), 'vanilla'], {'locked': True}],
    '2': [[('south', outside), 'vanilla'], {'passed': True}]
},
'Main Hall':
{
    '1': [[('south', foyer), 'vanilla'], {'passed': True}],
    '2': [[('west', laboratory), 'vanilla'], {'hidden': True}],
    '3': [[('east', hall_of_easts), 'vanilla'], {'locked': True}],
    '4': [[('north', hallway), 'vanilla'], {'locked': False}]
},
'Laboratory':
{
    '1': [[('east', main_hall), 'vanilla'], {'passed': True}]
},
'Hall of Infinite Easts':
{
    '1': [[('west', main_hall), 'vanilla'], {'passed': True}],
    '2': [[('east', hall_of_easts), 'vanilla'], {'locked': False}]
},
'Hallway':
{
    '1': [[('south', main_hall), 'vanilla'], {'passed': True}],
    '2': [[('west', library), 'vanilla'], {'locked': False}],
    '3': [[('east', tower), 'vanilla'], {'hidden': True}]
},
'Library':
{
    '1': [[('east', hallway), 'vanilla'], {'passed': True}]
},
'Tower':
{
    '1': [[('west', hallway), 'vanilla'], {'passed': True}],
    '2': [[('up', death), 'stairs'], {'warning': 'The stairs don\'t look  very dependable.'}]
}
}

def create_doors(room):
    """This function reads the dictionary all_doors to add the doors to a room.
    The print statements can be selectively commented/uncommented for debugging purposes."""
    # print(f'\nCreating doors for {room}...')
    for door in all_doors[room.name]:
        door_data, door_kwargs = all_doors[room.name][door]
        direction, leads_to = door_data[0]
        door_type = door_data[1]

        if door_type == 'vanilla':
            door = Door(direction, leads_to, **door_kwargs)
            room.doors.append(door)
            # print(f'Door {room.doors[-1].id} created.')
        elif door_type == 'stairs':
            door = Stairs(direction, leads_to, **door_kwargs)
            room.stairs.append(door)
            # print(f'Stairs {room.stairs[-1].id} created.')
            
    # print(f'Door creation complete. {room.name} contains the following doors:')
    # for door in room.doors:
    #     print(door)
    # if isinstance(room, Stairwell):
    #     for stair in room.stairs:
    #         print(stair)

for room in room_instances:
    if room_instances[room].name in all_doors:
        create_doors(room_instances[room])


# Next, create items
all_items = {
'Foyer':
{
    '1': [
         [
         ('key',
         'A metal key.',
         'An antique metal key, dark with age. It has a solid heft and fits comfortably in your hand.',
         foyer,
         'on the floor'),
         'vanilla'
         ],
         {}
         ]
},
'Main Hall':
{
    '1': [
         [
         ('rope',
         'A thick rope.',
         'A thick length of rope hanging from the ceiling, frayed at the bottom. It looks sturdy enough to support your weight.',
         main_hall,
         'hanging from the ceiling by the curtain'),
         'catalyst'
         ],
         {
         'transforms': main_hall,
         'verb': 'pull',
         'takeable': 'False',
         'failure_message': 'The rope is too firmly attached to the ceiling.'
         }
         ]
},
'Laboratory':
{
'1': [
         [
         ('lighter',
         'A purple Bic lighter.',
         'A purple Bic lighter with the safety removed so the wheel spins freely. The tines have not been perfectly bent back into place, so you have to watch your thumb as you flick.',
         laboratory,
         'under a chair'),
         'vanilla'
         ],
         {}
         ],
'2': [
         [
         ('piece of scrap paper',
         'A piece of scrap paper with writing on it.',
         'A somewhat rumpled piece of scrap paper. Coffee stains and other damage have rendered most of the writing illegible. Near the center someone has scrawled \'rot13???\' in heavy pencil, underlined several times for emphasis.',
         laboratory,
         'on the table'),
         'vanilla'
         ],
         {}
         ]
},
'Hall of Infinite Easts':
{
},
'Hallway':
{
    '1': [
         [
         ('switch',
         'A metal toggle switch.',
         'A small metal toggle switch.',
         hallway,
         'in the safe'),
         'catalyst'
         ],
         {
         'transforms': hallway,
         'verb': 'flip',
         'hidden': True,
         'takeable': 'False',
         'failure_message': 'The switch is attached to the safe.',
         'reveal_message': 'There was a switch under the note!'
         }
         ],
    '2': [
         [
         ('note',
         'A post-it note.',
         'A yellow post-it note with a message neatly written in pen. It reads: \'You didn\'t think the Object would be in here, did you?\'',
         hallway,
         'in the safe'),
         'concealer'
         ],
         {
         'hides': 'switch',
         'hidden': True,
         'reveal_message': 'There is a note inside the safe!'
         }
         ],
    '3': [
         [
         ('safe',
         'A large safe with a keyboard on the door.',
         'A modern safe with a small screen and full keyboard for password input. It accepts lower-case letters, digits, and spaces.',
         hallway,
         'built into the wall'),
         'concealer'
         ],
         {
         'hides': 'note',
         'hidden': True,
         'takeable': False,
         'failure_message': 'You would need special equipment to remove the safe from the wall.', 
         'reveal_message': 'There was a safe hidden behind the painting!'
         }
         ],
    '4': [
         [
         ('painting',
         'An impressionistic painting',
         'An impressionistic painting depicting a figure in blue atop a white horse racing through a green field; the landscape seem to blur with the speed of the rider. You feel like you\'ve seen it before. A small plaque on the bottom of the frame is engraved with the words \'DER BLAUE REITER\'.',
         hallway,
         'hanging on the wall'),
         'concealer'
         ],
         {
         'hides': 'safe',
         }
         ]
},
'Library':
{
'1': [
         [
         ('candle',
         'A fat candle on a tall brass stand.',
         'A fat gray candle. The wick is blackened from being lit but it appears that no wax has been consumed. Holding it or even looking at it for too long makes you uneasy.',
         library,
         'in an alcove'),
         'vanilla'
         ],
         {}
         ],
'2': [
         [
         ('ghost',
         'A spectral presence.',
         'The Hint Ghost of OOP Manor resembles the cartoon ghosts of your childhood: white, diaphanous, billowing in the air despite the lack of breeze. You cannot distinguish a face.',
         laboratory,
         'before you'),
         'vanilla'
         ],
         {
            'failure_message': 'Your hands pass through the Hint Ghost!',
            'reveal_message': 'A ghost appears!'
         }
         ]
},
'Tower':
{
}
}

item_instances = {}  # Making an item_instances dictionary to allow references to as-yet uninstantiated items in all_items

def create_items(room):
    for item in all_items[room.name]:
        item_info, item_type = all_items[room.name][item][0][0], all_items[room.name][item][0][1]
        extra_info = all_items[room.name][item][1]

        if item_type == 'vanilla':
            item = Item(*item_info, **extra_info)
            room.items.append(item)
            item_instances[item.name] = item
        elif item_type == 'catalyst':
            item = Catalyst(*item_info, **extra_info)
            room.items.append(item)
            item_instances[item.name] = item
        elif item_type == 'concealer':
            item = Concealer(*item_info, **extra_info)
            room.items.append(item)
            item_instances[item.name] = item
            """I get errors if I list the hidden item directly in all_items; this is a workaround"""
            item_instances[item.name].hides = item_instances[item_instances[item.name].hides] 

for room in room_instances:
    if room_instances[room].name in all_items:
        create_items(room_instances[room])




# #foyer

# #mainhall
# rope = Catalyst('rope', 'A thick rope.', 'A thick length of rope hanging from the ceiling, frayed at the bottom. It looks sturdy enough to support your weight.', location=main_hall, position='hanging from the ceiling by the curtain', transforms=main_hall, verb='pull', takeable=False, failure_message='The rope is too firmly attached to the ceiling to take.')
# main_hall.items.append(rope)

# #laboratory
# lighter = Item('lighter', 'A purple Bic lighter', 'A purple Bic lighter with the safety removed so the wheel spins freely. The tines have not been perfectly bent back into place, so you have to watch your thumb as you flick.', location=laboratory, position='under a chair')
# laboratory.items.append(lighter)
# paper = Item('piece of scrap paper', 'A scrap of paper with writing on it', 'A somewhat rumpled piece of scrap paper. Coffee stains and other damage have rendered most of the writing illegible. Near the center someone has scrawled \'rot13???\' in heavy pencil, underlined several times for emphasis.', location=laboratory, position='on the table')
# laboratory.items.append(paper)

# #hallway
# switch = Catalyst('switch', 'A metal toggle switch', 'A small metal toggle switch', location=hallway, position='in the safe', transforms=hallway, verb='flip', hidden=True, takeable=False, failure_message='The switch is attached to the safe.', reveal_message='There was a switch under the note!')
# hallway.items.append(switch)
# note = Concealer('note', 'A post-it note', 'A yellow post-it note with a message neatly written in pen. It reads: \'You didn\'t think the Object would be in here, did you?\'', location=hallway, position='in the safe', hides=switch, hidden=True, reveal_message='There is a note inside the safe!')
# hallway.items.append(note)
# safe = Concealer('safe', 'A large safe with a keyboard', 'A modern safe with a small screen and full keyboard for password input. It accepts lower-case letters, digits, and spaces.', location=hallway, position='built into the wall', hides=note, hidden=True, takeable=False, failure_message='You would need special equipment to remove the safe from the wall.', reveal_message='A safe was hidden behind the painting!')
# hallway.items.append(safe)
# painting = Concealer('painting', 'An impressionistic painting', 'An impressionistic painting depicting a figure in blue atop a white horse racing through a green field; the landscape seem to blur with the speed of the rider. You feel like you\'ve seen it before. A small plaque on the bottom of the frame is engraved with the words \'DER BLAUE REITER\'.', location=hallway, position='on the wall', hides=safe)
# hallway.items.append(painting)

# #library
# candle = Item('candle', 'A fat candle on a tall brass stand', 'A fat gray candle. The wick is blackened from being lit but it appears that no wax has been consumed. Looking at it for too long makes you uneasy. ', location=library, position='in an alcove')
# candle.lit = False
# library.items.append(candle)
# ghost = Item('ghost', 'A spectral presence', 'The Hint Ghost of OOP Manor resembles the cartoon ghosts of your childhood: white, diaphanous, billowing in the air despite the lack of breeze. You cannot distinguish a face.', location=library, position='before you', hidden=True, takeable=False, failure_message='Your hands pass through the Hint Ghost!')
# library.items.append(ghost)

# ghost.populate_hints()



# print('Welcome, adventurer!')
# name = input('What is your name? ')
# player = Player(name, entrance)
# print(f'Player {player.name} created.')
# player.get_location()

# player = Player('ababu', location=foyer)
# player.arrive()
# player.unlock_door()
# player.take(key)
# player.move(main_hall)
# player.unlock_door()
# player.move(main_hall)
# player.manipulate(rope)
# player.take(lighter)
# player.move(hallway)
# player.move(library)
# player.candle_switch()
# # player.candle_switch()
# player.take(candle)
# player.move(hallway)
# player.take(painting)
# player.look_around()
# player.open_safe()
# player.take(note)
# player.examine(note)
# switch.transform(hallway)
# player.look_around()
# player.move(tower)
# player.climb_stairs(death)
# player.status()
# tower.kill(player)
# player.check_inventory()
# player.move(entrance)
# player.move(foyer)
# player.look_around()
# player.move(entrance)
# player.take_item(key)
# player.move(foyer)
# player.drop_item(key)
# player.look_around()
# player.move(entrance)
# player.check_location()
# player.check_inventory()
# player.check_location()
# player.drop_item(key)
# player.check_location()
# player.take_item(wallet)
# player.drop_item(wallet)