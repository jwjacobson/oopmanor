from items import *
from doors import *

class Room:
    """Rooms are the basic spatial units of the Manor. They contain Items and connect to one another via Doors.
    Via their descriptions, they also play an essential role in constituting the world of the game for the user."""
    id_counter = 1

    def __init__(self, name, blurb, description, doors=None, items=None, visited=False):
        if doors is None:               # These conditionals avoid the issue of having a mutable data structure as a default value
            doors = []
        if items is None:
            items = []
        self.id = Room.id_counter       # IDs are used in the repr and for debugging purposes
        Room.id_counter += 1
        self.name = name
        self.blurb = blurb              # A short description, possibly superfluous
        self.description = description  # The full description read upon first entering a room or when examining it
        self.doors = doors              # The doors in the room
        self.items = items              # The items in the room
        self.visited = visited          # Whether or not the player has been to the room

    def __repr__(self):
        return f'Room {self.id} | {self.name}'

    def remove_item(self, item):
        """Only called when the player takes an item"""
        self.items.remove(item)

    def populate_doors(self):
        """Print statements can be selectively commented/uncommented for debugging purposes"""
        # print(f'Populating doors for {self}...')
        for door in all_doors[self.name]:
            self.doors.append(Door(*all_doors[self.name][door][0], **all_doors[self.name][door][1]))
            # print(f'Door {self.doors[-1].id} created.')
        # print(f'Population complete. {self} contains the following doors:')
        # for door in self.doors:
        #     print(door)

    def describe_doors(self):
        for door in self.doors:
            if door.hidden:
                continue
            elif door.passed:
                print(f'There is a door to the {door.direction}, leading to the {door.leads_to.name}.')
            else:
                print(f'There is a door to the {door.direction}.')

class Transformer(Room):
    """A Transformer is a Room that changes shape in response to a Catalyst.""" 
    def __init__(self, name, blurb, description, new_blurb, new_description, doors=None, items=None, visited=False, transformation_message=''):
            if doors is None:               
                doors = []
            if items is None:
                items = []
            self.id = Room.id_counter       
            Room.id_counter += 1
            self.name = name
            self.blurb = blurb              
            self.description = description  
            self.new_blurb = new_blurb              # A new short description post-transformation
            self.new_description = new_description  # A new full description post-transformation
            self.doors = doors              
            self.items = items              
            self.visited = visited
            self.transformation_message = transformation_message

    def __repr__(self):
        return f'Room {self.id} | {self.name}'

class Stairwell(Room):
    """A Stairwell is a Room that contains Stairs for going up or down.""" 
    def __init__(self, name, blurb, description, doors=None, stairs=None, items=None, visited=False):
            if doors is None:               
                doors = []
            if stairs is None:
                stairs = []
            if items is None:
                items = []
            self.id = Room.id_counter       
            Room.id_counter += 1
            self.name = name
            self.blurb = blurb              
            self.description = description  
            self.doors = doors
            self.stairs = stairs                # Unique to Stairwells              
            self.items = items              
            self.visited = visited

    def __repr__(self):
        return f'Stairwell {self.id} | {self.name}'

    def describe_stairs(self):
        for stair in self.stairs:
            if stair.hidden:
                continue
            elif stair.passed:
                print(f'There is a stairway leading {stair.direction} into the gloom, towards the {stair.leads_to.name}.')
            else:
                print(f'There is a stairway leading {stair.direction} into the gloom.')

class DangerRoom(Room):
    """A Danger Room is a Room that can kill the Player."""

    def __init__(self, name, blurb, description, doors=None, items=None, visited=False, death_message=''):
        if doors is None:               
            doors = []
        if items is None:
            items = []
        self.id = Room.id_counter       
        Room.id_counter += 1
        self.name = name
        self.blurb = blurb              
        self.description = description  
        self.doors = doors              
        self.items = items              
        self.visited = visited
        self.death_message = death_message      # The description of the player's death

    def __repr__(self):
        return f'Room {self.id} | {self.name}'

    def kill(self, player):
        player.die()

class DangerStairwell(Stairwell, DangerRoom):
    """I'm in the Stairwell. I'm in the Danger Room. I'm in the combination Stairwell and Danger Room!"""

    def __init__(self, name, blurb, description, doors=None, stairs=None, items=None, visited=False, death_message=''):
        if doors is None:               
            doors = []
        if stairs is None:
            stairs = []
        if items is None:
            items = []
        self.id = Room.id_counter       
        Room.id_counter += 1
        self.name = name
        self.blurb = blurb              
        self.description = description  
        self.doors = doors
        self.stairs = stairs              
        self.items = items              
        self.visited = visited
        self.death_message = death_message    

    def __repr__(self):
        return f'Room {self.id} | {self.name}'


#Generating rooms one by one now, later the info will be stored in a data structure and generated with a single function
foyer = Room('Foyer', 'The foyer of OOP Manor.',
'The foyer of OOP Manor is not large to begin with, dominated by two massive carved-stone planters which fill its east and west sides, leaving only a narrow path to walk through the room. In spite of the lack of windows and general gloom, the tropical vegetation growing from the planters is lush and varied, with vines spilling over the edges and climbing the white-tiled walls. From the center of each planter a stately palm rises nearly to the ceiling where its leaves fan out to form a canopy obscuring the ceiling. You expect to see brightly colored birds or even a monkey startle at your entrance, but the room is completely quiet. Not even the indifferent buzz of insects breaks the silence.')

main_hall = Transformer('Main Hall', 'The main hall of OOP Manor.',
'The cavernous main hall of OOP Manor stretches approximately 100 meters from east to west, anchored in its center by a five-meter, fully-lit chandelier hanging over a long, fully set dining table. Along the far wall hang painted portraits of Manor nobility, their faces glowering down at you. Above the portraits is a mezzanine running along the north and west walls, with several doors spaced regularly along its length, but you don\'t see a way to access it from here. A curtain covers the west wall.',
new_blurb='The main hall of OOP Manor.',
new_description='The cavernous main hall of OOP Manor stretches approximately 100 meters from east to west, anchored in its center by a five-meter, fully-lit chandelier hanging over a long, fully set dining table. Along the far wall hang painted portraits of Manor nobility, their faces glowering down at you. Above the portraits is a mezzanine running along the north and west walls, with several doors spaced regularly along its length, but you don\'t see a way to access it from here. The curtain on the west wall has been parted, revealing an incongruous metal door, more suited to a school or factory than what you\'ve seen of the Manor.',
transformation_message='The curtain parts, revealing a door!'
)
outside = Room('Outside', 'Outside of OOP Manor.',
'To leave the Manor is to abandon your quest.'
)
laboratory = Room('Laboratory', 'A disused laboratory.',
'The laboratory gives the impression of having been abandoned hastily and never returned to.  A single fluorescent tube light in a metal housing suspended by two chains from the particle board ceiling. There are papers scattered about everywhere, but most are so damaged as to be illegible. The northwest corner appears to have contained a large, heavy object, since removed. A sink and eyewash station are next to the door.'
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

# Populating doors manually one by one for now, later it will be done by a single function
foyer.populate_doors()
main_hall.populate_doors()
laboratory.populate_doors()
hall_of_easts.populate_doors()
hallway.populate_doors()
library.populate_doors()
tower.populate_doors()

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


print(main_hall.items)