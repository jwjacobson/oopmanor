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
        print(self.location.description)
        self.location.describe_doors()
        for item in self.location.items:
            if item.hidden:
                continue
            else:
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
            if item.takeable:
                print(f'You take the {item.name}.')
                self.inventory.append(item)
                item.position = self.inventory
                item.location = self.inventory
                self.location.remove_item(item)
            else:
                print(item.failure_message)
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
        for door in self.location.doors:        # I know it's inelegant to iterate through all the doors but there's only a few
                                                # and the alternative is adding another door attribute or doing weird stuff with  directions
            if door.leads_to == self.prev_location and door.passed == False:
                self.pass_door(door)
        if self.location.visited == False:
            print(self.location.description)
            self.location.visited = True
        self.location.describe_doors()
        for item in self.location.items:
            if item.hidden:
                continue
            else:
                print(f'You see a {item.name} {item.position}.')

    def move(self, destination):
        for door in self.location.doors:
            if door.leads_to == destination and door.locked:
                print(f'The door to the {door.direction} is locked.')
                return
        print('Moving...')
        self.prev_location = self.location
        self.location = destination
        self.arrive()
    
    def unlock_door(self):
        if key not in self.inventory:
            print('You need a key to do that.')
            return
        locked_doors = []
        for door in self.location.doors:
            if door.hidden:
                continue
            elif door.locked:
                locked_doors.append(door)
        if len(locked_doors) == 1:
            door_to_unlock = locked_doors[0]
            door_to_unlock.unlock()
            print(f'You unlock the door to the {door_to_unlock.direction}.')
            self.inventory.remove(key)
            key.vanish()
        elif len(locked_doors) > 1:
            print('Which door do you want to unlock?')
            # todo: function for selecting which door to unlock in case of multiple lokced doors 
        else:
            print('You see no doors to unlock.')
    
    def candle_switch(self):
        if self.location != candle.location and candle not in self.inventory:
            print('You don\'t see a candle anywhere.')
        else:
            if candle.lit:
                print('You blow out the candle.')
                candle.lit = False
                ghost.hidden = True
                if self.location == library:
                    print('The Hint Ghost vanishes!')
            elif lighter not in self.inventory:
                print('You have nothing to light the candle with.')
            else:
                print('You light the candle.')
                candle.lit = True
                ghost.hidden = False
                if self.location == library:
                    print('A ghost appears!')