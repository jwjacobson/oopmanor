from items import *

class Room:
    def __init__(self, name, description, items=[]):
        self.name = name
        self.description = description
        self.items = items
    
    def __repr__(self):
        return f'Room | {self.name}'

    def remove_item(self, item):
        self.items.remove(item)

rooms = []

entrance = Room('Entrance', 'The entrance to OOP Manor.')
rooms.append(entrance)
foyer = Room('Foyer', 'The foyer of OOP Manor.')
rooms.append(foyer)

key = Item('key', 'A metal key', location=entrance, position='on the ground')
entrance.items.append(key)