import codecs
from rooms import *

class Player:
    """The Player is the protagonist of the game, controlled by the user via a series of menu prompts.
        Most actions in the game are carried out or initiated by the Player."""
    def __init__(self, name, location: Room, alive=True, inventory=None, secrets=0, prev_location=outside):
        if inventory is None:               # This conditional avoids the issue of having a mutable data structure as a default value
            inventory = []
        self.name = name                    # Chosen by the user at the start of the game
        self.location = location            # The Room where the player is
        self.alive = alive                  # Being dead ends the game (Unless...)
        self.inventory = inventory          # A list of the items the Player is carrying 
        self.secrets = 0                    # The number of secrets found, for entry in the High Score table
        self.prev_location = prev_location  # The Player's location before their current location, used in some door/room interactions
    
    def __repr__(self):
        return f'Player | {self.name}'

    def look_around(self):
        """This function allows the player to reread the full description of their location
            and also lists significant features (Items and Doors)"""
        print(f'\nYou look around the {self.location.name}.')
        print(self.location.description)
        self.location.describe_doors()
        for item in self.location.items:
            if item.hidden:                 # Hidden Items are invisible to the Player
                continue
            else:
                print(f'You see a {item.name} {item.position}.')

    def check_inventory(self):
        """This function allows the Player to view the contents of their inventory."""
        if self.inventory:
            print('You have:')
            for item in self.inventory:
                print(item.name)
        else:
            print('You have nothing in your inventory.')

    def take(self, item):
        """This item allows the Player to take an Item from their location into their inventory."""
        if self.location == item.location:
            if item.takeable:
                print(f'You take the {item.name}.')
                self.inventory.append(item)
                item.position = self.inventory
                item.location = self.inventory
                self.location.remove_item(item)
            else:
                print(item.failure_message)
            if isinstance(item, Concealer):
                item.unconceal()
        else:
            print("You don't see one of those!")

    def drop(self, item):
        """This function allows the Player to drop an Item from their inventory into their location."""
        if item in self.inventory:
            item.location = self.location
            item.position = 'on the floor'
            self.inventory.remove(item)
            self.location.items.append(item)
            print(f'You drop the {item.name}.')
        else:
            print(f"You don't have one of those!")

    def pass_door(self, door):
        """This function marks a door as passed; passed doors print their destination when described"""
        door.passed = True
    
    def arrive(self):
        """This function handles what happens when a player arrives in a Room:
        passing the door they came in by, printing the description of the Room of not yet visited,
        and describing the Room's significant features (Items and Doors)"""
        print(f'\nYou arrive in the {self.location.name}.')
        for door in self.location.doors:        # I know it's inelegant to iterate through all the doors but there's only a few
                                                # and the alternative is adding another door attribute or doing weird stuff with  directions
            if door.leads_to == self.prev_location and door.passed == False:
                self.pass_door(door)
        if self.location.visited == False:
            print(self.location.description)
            self.location.visited = True
        self.location.describe_doors()
        if isinstance(self.location, Stairwell):
            self.location.describe_stairs()
        for item in self.location.items:
            if item.hidden:
                continue
            else:
                print(f'You see a {item.name} {item.position}.')
        if isinstance(self.location, DangerRoom):
            print('You have an uneasy feeling.')

    def move(self, destination):
        """This function first checks if a player can move to the desired location,
        then moves them there and calls the arrive function above."""
        for door in self.location.doors:
            if door.leads_to == destination and door.locked:
                print(f'The door to the {door.direction} is locked.')
                return
        print('Moving...')
        self.prev_location = self.location
        self.location = destination
        self.arrive()
    
    def unlock_door(self):
        """This function first checks if a player has the means to unlock a door (a key and a locked door),
        then unlocks the door. The key vanishes after use."""
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
        """This function first checks if the Player has the means to light or extinguish the ghostly candle,
        then does so."""
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

    def talk(self):
        """This function 'talks' to the Hint Ghost, who at present only dispenses hints."""
        if self.location != library or candle.lit == False:
            print('You don\'t see anyone to talk to.')
        else:
            if not ghost.hints:
                ghost.populate_hints()
            print('\nThe Hint Ghost says:')
            print(ghost.hints.pop())          # Popping from a set is sufficiently random for this context

    def examine(self, item):
        """This function prints the detailed description of an item in the Player's location or inventory."""
        if item.location != self.location and item not in self.inventory:
            print(f'You do not see a {item.name}.')
        else:
            print(item.description)

    def open_safe(self):
        """This function allows the Player to attempt to open the safe in the hallway."""
        if self.location != hallway or safe.hidden:
            print('You don\'t see a safe.')
            return
        target = 'abc'                          # placeholder target
        attempt = input('Enter password: ')
        if codecs.encode(attempt, 'rot13') == target:
            print('The safe pops open!')
            safe.unconceal()
        else:
            print('Incorrect password')

    def die(self):
        print('You die...')
        self.alive = False