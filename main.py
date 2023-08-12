from rooms import *

class Player:
    def __init__(self, name, location: Room, inventory=[]):
        self.name = name
        self.location = location
        self.inventory = inventory
    
    def __repr__(self):
        return f'Player | {self.name}'

    def get_location(self):
        print(f'You are in the {self.location.name}.')

    def move(self, destination):
        print('Moving...')
        self.location = destination
        self.get_location()

# print('Welcome, adventurer!')
# name = input('What is your name? ')
# player = Player(name, entrance)
# print(f'Player {player.name} created.')
# player.get_location()

player = Player('ababu', entrance)
player.move(foyer)
candle = Object('Candle', 'a candle')
print(candle.description)
