from rooms import *

class Player:
    def __init__(self, name, location: Room, inventory=None, secrets=0, prev_location=outside):
        if inventory is None:
            inventory = []
        self.name = name
        self.location = location
        self.inventory = inventory
        self.secrets = 0
        self.prev_location = prev_location
    
    def __repr__(self):
        return f'Player | {self.name}'

    def look_around(self):
        print(f'\nYou look around the {self.location.name}.')
        print(self.location.full_description)
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

    def pass_door(self, door):
        door.passed = True
    
    def arrive(self):
        print(f'\nYou arrive in the {self.location.name}.')
        for door in self.location.doors:
            if door.leads_to == self.prev_location and door.passed == False:
                self.pass_door(door)
        if self.location.visited == False:
            print(self.location.full_description)
            self.location.visited = True
        self.location.describe_doors()
        for item in self.location.items:
            print(f'You see a {item.name} {item.position}.')

    def move(self, destination):
        print('Moving...')
        self.prev_location = self.location
        self.location = destination
        self.arrive()
    
   
