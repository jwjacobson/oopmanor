from items import *
from doors import *

class Room:
    id_counter = 1

    def __init__(self, name, full_description, brief_description, doors=[], items=[], visited=False):
        self.id = Room.id_counter
        Room.id_counter += 1
        self.name = name
        self.full_description = full_description
        self.brief_description = brief_description
        self.doors = doors
        self.items = items


    def __repr__(self):
        return f'Room {self.id} | {self.name}'

    def remove_item(self, item):
        """Only called when the player takes an item"""
        self.items.remove(item)

    def populate_doors(self):
        for door in all_doors[self.name]:
            self.doors.append(Door(*all_doors[self.name][door][0], **all_doors[self.name][door][1]))

    def describe_doors(self):
        for door in self.doors:
            if door.passed:
                print(f'There is a door to the {door.direction}, leading to the {door.leads_to.name}.')
            else:
                print(f'There is a door to the {door.direction}.')

rooms = []

entrance = Room('Entrance', 'Full description tbd', 'The entrance to OOP Manor.')
rooms.append(entrance)
foyer = Room('Foyer', 'Full description tbd', 'The foyer of OOP Manor.')
rooms.append(foyer)
outside = Room('Outside', 'Full description tbd', 'Outside of OOP Manor.')
rooms.append(outside)

key = Item('key', 'A metal key', location=entrance, position='on the ground')
entrance.items.append(key)

all_doors = {
'Entrance':
{
    '1': [['north', foyer], {'locked': True}],
    '2': [['south', outside,], {'passed': True}]
}
}

# print(all_doors['Entrance']['1'][0])
# door = Door(*all_doors['Entrance']['1'][0], **all_doors['Entrance']['1'][1])
# print(door.locked)

entrance.populate_doors()
entrance.describe_doors()
print(rooms)