from rooms import *

class Player:
    def __init__(self, name, location: Room, inventory=[]):
        self.name = name
        self.location = location
        self.inventory = inventory
    
    def __repr__(self):
        return f'Player | {self.name}'

    def check_location(self):
        print(f'You are in the {self.location.name}.')

    def check_inventory(self):
        if self.inventory:
            print('You have:')
            for item in self.inventory:
                print(item.name)
        else:
            print('You have nothing in your inventory.')


    def move(self, destination):
        print('Moving...')
        self.location = destination
        self.check_location()

# print('Welcome, adventurer!')
# name = input('What is your name? ')
# player = Player(name, entrance)
# print(f'Player {player.name} created.')
# player.get_location()

key = Item('key', 'A metal key', 'in your inventory')
player = Player('ababu', location=entrance, inventory=[key])
player.check_inventory()