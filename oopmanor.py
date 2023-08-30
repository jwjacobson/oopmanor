# from player import *
from items import *
from doors import *
from rooms import *

#Generating rooms one by one now, later the info will be stored in a data structure and generated with a single function
print('Generating rooms...')
foyer = Room('Foyer', 'The foyer of OOP Manor.',
'The foyer of OOP Manor is not large to begin with, dominated by two massive carved-stone planters which fill its east and west sides, leaving only a narrow path to walk through the room. In spite of the lack of windows and general gloom, the tropical vegetation growing from the planters is lush and varied, with vines spilling over the edges and climbing the white-tiled walls. From the center of each planter a stately palm rises nearly to the ceiling where its leaves fan out to form a canopy obscuring the ceiling. You expect to see brightly colored birds or even a monkey startle at your entrance, but the room is completely quiet. Not even the indifferent buzz of insects breaks the silence.')

main_hall = Transformer('Main Hall', 'The main hall of OOP Manor.',
'The cavernous main hall of OOP Manor stretches approximately 50 meters from east to west, anchored in its center by a five-meter, fully-lit chandelier hanging over a long, fully set dining table. Along the far wall hang painted portraits of Manor nobility, their faces glowering down at you. Above the portraits is a mezzanine running along the north and west walls, with several doors spaced regularly along its length, but you don\'t see a way to access it from here. A curtain covers the west wall.',
new_blurb='The main hall of OOP Manor.',
new_description='The cavernous main hall of OOP Manor stretches approximately 100 meters from east to west, anchored in its center by a five-meter, fully-lit chandelier hanging over a long, fully set dining table. Along the far wall hang painted portraits of Manor nobility, their faces glowering down at you. Above the portraits is a mezzanine running along the north and west walls, with several doors spaced regularly along its length, but you don\'t see a way to access it from here. The curtain on the west wall has been parted, revealing an incongruous metal door, more suited to a school or factory than what you\'ve seen of the Manor.',
transformation_message='The curtain parts, revealing a door!'
)

outside = Room('Outside', 'Outside of OOP Manor.',
'To leave the Manor is to abandon your quest.'
)

laboratory = Room('Laboratory', 'A disused laboratory.',
'Entering the laboratory is like stepping into another time and place entirely.  gives the impression of having been abandoned hastily and never returned to. A single fluorescent tube light in a metal housing suspended by two chains from the particle board ceiling. There are papers scattered about everywhere, but most are so damaged as to be illegible. The northwest corner appears to have contained a large, heavy object, since removed. A sink and eyewash station are next to the door.'
)

hall_of_easts = Room('Hall of Infinite Easts', 'An infinite hall in one direction.',
'The Hall of Infinite Easts is less spectacular than you would have guessed from the name. It is a short and simple hallway with decor matching that of the main hall. There is a small table by the west door and two full-length mirrors facing each other on the north and south walls halfway across the hallway. If you wish, you can stand between them and see yourself reflected infinitely in either direction.'
)
hallway = Transformer('Hallway', 'An L-shaped hallway.',
'An unremarkable hallway that travels a few meters north before making a ninety-degree turn to the west, where it ends in a door.',
'A T-shaped hallway',
'A moderately remarkable T-shaped hallway that travels north before branching east and west. The two branches are identical, save for the rubble from the collapsed wall in the eastern branch.',
transformation_message='The wall to your right collapses, revealing a previously hidden branch of the hallway!'
)
library = Room('Library', 'The library of OOP manor.',
'description tbd'
)
tower = DangerStairwell('Tower', 'A stone tower with a spiral staircase.',
'description', death_message='As you climb, you stray too close to the edge and slip when a loose stone breaks off of a step. You plummet into the pit below.'
)

placeholder = Room('Placeholder', 'Placeholder room', 'The /dev/null of rooms.')

death = Room('Death', 'Where the Player dies', 'The destination for deathtrap doors.'
)
print('Done.')

all_doors = {
'Foyer':
{
    '1': [['north', main_hall], {'locked': True}],
    '2': [['south', outside,], {'passed': True}]
},
'Main Hall':
{
    '1': [['south', foyer], {'locked': False}],
    '2': [['west', laboratory], {'hidden': True}],
    '3': [['east', hall_of_easts], {'locked': True}],
    '4': [['north', hallway], {'locked': False}]
},
'Laboratory':
{
    '1': [['east', main_hall], {'passed': True}]
},
'Hall of Infinite Easts':
{
    '1': [['west', main_hall], {'passed': True}],
    '2': [['east', hall_of_easts], {'locked': False}]
},
'Hallway':
{
    '1': [['south', main_hall], {'passed': True}],
    '2': [['west', library], {'locked': False}],
    '3': [['east', tower], {'hidden': True}]
},
'Library':
{
    '1': [['east', hallway], {'passed': True}]
},
'Tower':
{
    '1': [['west', hallway], {'passed': True}]
}
}


"""
speculative manor generation sequence:
generate rooms
generate doors
generate items
"""

def populate_doors(room):
    """This function reads the dictionary all_doors to add the doors to a room.
    The print statements can be selectively commented/uncommented for debugging purposes."""
    print(f'Populating doors for {room}...')
    for door in all_doors[room.name]:
        room.doors.append(Door(*all_doors[room.name][door][0], **all_doors[room.name][door][1]))
        print(f'Door {room.doors[-1].id} created.')
    print(f'Population complete. {room.name} contains the following doors:')
    for door in room.doors:
        print(door)


# Populating doors manually one by one for now, later it will be done by a single function
populate_doors(foyer)
populate_doors(main_hall)
populate_doors(laboratory)
populate_doors(hall_of_easts)
populate_doors(hallway)
populate_doors(library)
populate_doors(tower)

# Since there is only one stairwell right now I will just manually put the stairs there (later single function etc.)
tower_stairs = Stairs('up', death, warning='The stairs don\'t look very dependable.')
tower.stairs.append(tower_stairs)

#Generating items one by one now, later the info will be stored in a data structure and generated by a single function
#foyer
key = Item('key', 'A metal key', 'An antique metal key, dark with age. It has a solid heft and fits comfortably in your hand.', location=foyer, position='on the floor')
foyer.items.append(key)

#mainhall
rope = Catalyst('rope', 'A thick rope.', 'A thick length of rope hanging from the ceiling, frayed at the bottom. It looks sturdy enough to support your weight.', location=main_hall, position='hanging from the ceiling by the curtain', transforms=main_hall, verb='pull', takeable=False, failure_message='The rope is too firmly attached to the ceiling to take.')
main_hall.items.append(rope)

#laboratory
lighter = Item('lighter', 'A purple Bic lighter', 'A purple Bic lighter with the safety removed so the wheel spins freely. The tines have not been perfectly bent back into place, so you have to watch your thumb as you flick.', location=laboratory, position='under a chair')
laboratory.items.append(lighter)
paper = Item('piece of scrap paper', 'A scrap of paper with writing on it', 'A somewhat rumpled piece of scrap paper. Coffee stains and other damage have rendered most of the writing illegible. Near the center someone has scrawled \'rot13???\' in heavy pencil, underlined several times for emphasis.', location=laboratory, position='on the table')
laboratory.items.append(paper)

#hallway
switch = Catalyst('switch', 'A metal toggle switch', 'A small metal toggle switch', location=hallway, position='in the safe', transforms=hallway, verb='flip', hidden=True, takeable=False, failure_message='The switch is attached to the safe.', reveal_message='There was a switch under the note!')
hallway.items.append(switch)
note = Concealer('note', 'A post-it note', 'A yellow post-it note with a message neatly written in pen. It reads: \'You didn\'t think the Object would be in here, did you?\'', location=hallway, position='in the safe', hides=switch, hidden=True, reveal_message='There is a note inside the safe!')
hallway.items.append(note)
safe = Concealer('safe', 'A large safe with a keyboard', 'A modern safe with a small screen and full keyboard for password input. It accepts lower-case letters, digits, and spaces.', location=hallway, position='built into the wall', hides=note, hidden=True, takeable=False, failure_message='You would need special eqipment to remove the safe from the wall.', reveal_message='A safe was hidden behind the painting!')
hallway.items.append(safe)
painting = Concealer('painting', 'An impressionistic painting', 'An impressionistic painting depicting a figure in blue atop a white horse racing through a green field; the landscape seem to blur with the speed of the rider. You feel like you\'ve seen it before. A small plaque on the bottom of the frame is engraved with the words \'DER BLAUE REITER\'.', location=hallway, position='on the wall', hides=safe)
hallway.items.append(painting)

#library
candle = Item('candle', 'A fat candle on a tall brass stand', 'A fat gray candle. The wick is blackened from being lit but it appears that no wax has been consumed. Looking at it for too long makes you uneasy. ', location=library, position='in an alcove')
candle.lit = False
library.items.append(candle)
ghost = Item('ghost', 'A spectral presence', 'The Hint Ghost of OOP Manor resembles the cartoon ghosts of your childhood: white, diaphanous, billowing in the air despite the lack of breeze. You cannot distinguish a face.', location=library, position='before you', hidden=True, takeable=False, failure_message='Your hands pass through the Hint Ghost!')
library.items.append(ghost)
ghost.populate_hints()




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