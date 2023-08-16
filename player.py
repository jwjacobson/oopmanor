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
        self.location.describe_doors()
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
        if self.location == item.location:
            print(f'You take the {item.name}.')
            self.inventory.append(item)
            item.position = self.inventory
            item.location = self.inventory
            self.location.remove_item(item)
        else:
            print("You don't see one of those!")

    def drop_item(self, item):
        if item in self.inventory:
            item.location = self.location
            item.position = 'on the floor'
            self.inventory.remove(item)
            self.location.items.append(item)
            print(f'You drop the {item.name}.')
        else:
            print(f"You don't have one of those!")

    def arrive(self):
        print(f'\nYou arrive in the {self.location.name}.')
        if self.location.visited:
            print(self.location.brief_description)
        else:
            print(self.location.full_description)
        self.location.describe_doors()
        for item in self.location.items:
            print(f'You see a {item.name} {item.position}.')

    def move(self, destination):
        print('Moving...')
        self.location = destination
        self.arrive()
    
   
