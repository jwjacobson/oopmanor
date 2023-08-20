from items import *
from doors import *

class Room:
    id_counter = 1

    def __init__(self, name, description, blurb, doors=None, items=None, visited=False):
        if doors is None:
            doors = []
        if items is None:
            items = []
        self.id = Room.id_counter
        Room.id_counter += 1
        self.name = name
        self.description = description
        self.blurb = blurb
        self.doors = doors
        self.items = items
        self.visited = visited

    def __repr__(self):
        return f'Room {self.id} | {self.name} | {self.blurb}'

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


#Generating rooms one by one now, later the info will be stored in a data structure
foyer = Room('Foyer',
'At long last, you stand before the front door of OOP Manor.',
'The entrance to OOP Manor.')
main_hall = Room('Main Hall', 'Full description tbd', 'The foyer of OOP Manor.')
outside = Room('Outside', 'Full description tbd', 'Outside of OOP Manor.')
laboratory = Room('Laboratory', 'description tbd', 'A disused laboratory.')
hall_of_easts = Room('Hall of Infinite Easts', 'description tbd', 'An infinite hall in one direction.')
hallway = Room('Hallway', 'description tbd', 'An L-shaped hallway.')
library = Room('Library', 'description tbd', 'The library of OOP manor.')

#Generating items one by one now, later the info will be stored in a data structure and everything populated by a single function
    #foyer
key = Item('key', 'A metal key', 'An antique metal key, dark with age. It has a solid heft and fits comfortably in your hand.', location=foyer, position='on the floor')
foyer.items.append(key)

    #laboratory
lighter = Item('lighter', 'A purple Bic lighter', 'A purple Bic lighter with the safety removed so the wheel spins freely.', location=laboratory, position='under a chair')
laboratory.items.append(lighter)
paper = Item('piece of scrap paper', 'A scrap of paper with writing on it', 'A somewhat rumpled piece of scrap paper. Coffee stains and other damage have rendered most of the writing illegibile. Near the center someone has scrawled \'rot13???\', underlined several times.', location=laboratory, position='on the table')
laboratory.items.append(paper)

    #hallway
safe = Item('safe', 'A large safe with a keyboard', 'A modern safe with a small screen and full keyboard for password input. It accepts lower-case letters, digits, and spaces.', location=hallway, position='built into the wall', hidden=True, takeable=False, failure_message='The safe is too heavy to lift.')
hallway.items.append(safe)
painting = Item('painting', 'An impressionistic painting', 'An impressionistic painting depicting a figure in blue atop a white horse racing through a green field. You feel like you\'ve seen it before. A small plaque on the bottom of the frame is engraved with the words \'DER BLAUE REITER\'.', location=hallway, position='on the wall')
hallway.items.append(painting)

    #library
candle = Item('candle', 'A fat candle on a tall brass stand', 'A fat gray candle. The wick is blackened from being lit but it appears that no wax has been consumed. Looking at it for too long makes you uneasy. ', location=library, position='in an alcove')
candle.lit = False
library.items.append(candle)
ghost = Item('ghost', 'A spectral presence', 'The Hint Ghost of OOP Manor resembles the cartoon ghosts of your childhood: white, diaphanous, billowing in the air despite the lack of breeze. You cannot distinguish a face.', location=library, position='before you', hidden=True, takeable=False, failure_message='Your hands pass through the Hint Ghost!')
library.items.append(ghost)
ghost.populate_hints()

all_doors = {
'Foyer':
{
    '1': [['north', main_hall], {'locked': True}],
    '2': [['south', outside,], {'passed': True}]
},
'Main Hall':
{
    '1': [['south', foyer], {'locked': False}],
    '2': [['west', laboratory], {'locked': False}],
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
    '2': [['west', library], {'locked': False}]
},
'Library':
{
    '1': [['east', hallway], {'passed': True}]
}
}

# Populating doors manually one by one for now
foyer.populate_doors()
main_hall.populate_doors()
laboratory.populate_doors()
hall_of_easts.populate_doors()
hallway.populate_doors()
library.populate_doors()