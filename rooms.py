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

foyer = Room('Foyer',
'At long last, you stand before the front door of OOP Manor.',
'The entrance to OOP Manor.')

main_hall = Room('Main Hall', 'Full description tbd', 'The foyer of OOP Manor.')

outside = Room('Outside', 'Full description tbd', 'Outside of OOP Manor.')

key = Item('key', 'A metal key', location=foyer, position='on the floor')
foyer.items.append(key)

# safe = Item('safe', 'A large safe', location=foyer, position='on the ground', takeable=False, failure_message='The safe is too heavy to lift.')
# foyer.items.append(safe)


all_doors = {
'Foyer':
{
    '1': [['north', main_hall], {'locked': True}],
    '2': [['south', outside,], {'passed': True}]
},
'Main Hall':
{
    '1': [['south', foyer], {'locked': False}],
}
}

# print(all_doors['Entrance']['1'][0])
# door = Door(*all_doors['Entrance']['1'][0], **all_doors['Entrance']['1'][1])
# print(door.locked)

foyer.populate_doors()
main_hall.populate_doors()
# entrance.describe_doors()
# print(rooms)