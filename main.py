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
        for item in self.location.items:
            print(f'You see a {item.name} {item.position}.')

    def check_inventory(self):
        if self.inventory:
            print('You have:')
            for item in self.inventory:
                print(item.name)
        else:
            print('You have nothing in your inventory.')

    def take_item(self, item):
        # self.item = item
        if self.location == item.location:
            self.inventory.append(item)
            item.position = self.inventory
            item.location = self.inventory
            self.location.remove_item(item)
        else:
            print(f"You don't see a {item}.")

    def move(self, destination):
        print('Moving...')
        self.location = destination
        self.check_location()

# print('Welcome, adventurer!')
# name = input('What is your name? ')
# player = Player(name, entrance)
# print(f'Player {player.name} created.')
# player.get_location()

player = Player('ababu', location=entrance)
player.check_location()
player.take_item(key)
player.check_inventory()
player.check_location()