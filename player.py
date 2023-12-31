# import codecs
# from rooms import *

class Player:
    """The Player is the protagonist of the game, controlled by the user via a series of menu prompts.
        Most actions in the game are carried out or initiated by the Player."""
    def __init__(self, name, location, prev_location='', alive=True, inventory=None, secrets=0, rooms_visited=0, items_found=0):
        if inventory is None:               # This conditional avoids the issue of having a mutable data structure as a default value
            inventory = []
        self.name = name                    # Chosen by the user at the start of the game
        self.location = location            # The Room where the player is
        self.prev_location = prev_location  # The Player's location before their current location, used in some door/room interactions
        self.alive = alive                  # Being dead ends the game (Unless...)
        self.inventory = inventory          # A list of the items the Player is carrying 
        self.secrets = secrets              # The number of secrets found, for entry in the High Score table
        self.rooms_visited = rooms_visited
        self.items_found = items_found
    
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
        """This function allows the Player to take an Item from their location into their inventory."""
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
        """This function marks a door as passed; passed doors print their destination when described."""
        door.passed = True
    
    def arrive(self):
        """This function handles what happens when a player arrives in a room:
        passing the door they came in by, printing the description of the room if not yet visited,
        and describing the room's significant features (items and doors)"""
        if self.location == death:
            print(self.prev_location.death_message)
            self.die()
            return
        print(f'\nYou arrive in the {self.location.name}.\n')
        for door in self.location.doors:        # I know it's inelegant to iterate through all the doors but there's only a few
                                                # and the alternative is adding another door attribute or doing weird stuff with  directions
            if door.leads_to == self.prev_location and door.passed == False:
                self.pass_door(door)
        if self.location.visited == False:
            print(self.location.description, '\n')
            self.location.visited = True
            self.rooms_visited += 1
            for item in self.location.items:
                if item.hidden == False:
                    self.items_found += 1
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
            if door.leads_to == destination:
                if door.locked:
                    print(f'The door to the {door.direction} is locked.')
                    return
                elif door.warning:
                    print(door.warning)
                    return
        print('Moving...')
        self.prev_location = self.location
        self.location = destination
        self.arrive()
    
    def climb_stairs(self, destination):
        """Once stairs are more clearly defined this can be integrated into the move function"""
        for stair in self.location.stairs:
            if stair.leads_to == destination:           #in this case the function is only being called with death as destination
                print(stair.warning)
                decision = input('Really proceed? (y/n)')
                while decision.lower() != 'y' and decision.lower() != 'n':
                    decision = input('Answer (Y)es or (N)o.')
                if decision.lower() == 'n':
                    print('You change your mind.')
                else:
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
            # todo: function for selecting which door to unlock in case of multiple locked doors 
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

    # Original open_safe method, leaving it here just in case
    # def open_safe(self):
    #     """This function allows the Player to attempt to open the safe in the hallway."""
    #     if self.location != hallway or safe.hidden:
    #         print('You don\'t see a safe.')
    #         return
    #     target = 'abc'                          # placeholder target
    #     attempt = input('Enter password: ')
    #     if codecs.encode(attempt, 'rot13') == target:
    #         print('The safe pops open!')
    #         self.secrets += 1
    #         safe.unconceal()
    #     else:
    #         print('Incorrect password')

    def open_safe(self):
        import safe_interface
        safe_interface.main()

    def die(self):
        print('You die...')
        self.alive = False

    def status(self):
        """The status report prints basic information about the Player.
        Will perhaps be a function of the house computer."""
        print(f'\nStatus Report: {self.name}')
        print(f'You are in the {self.location.name}; before that you were in the {self.prev_location.name}.')
        if self.alive:
            print('You are alive.')
        else:
            print('You are dead.')
        print(f'You have visited {self.rooms_visited} rooms.')
        print(f'You have found {self.items_found} items.')
        print(f'You have discovered {self.secrets} secrets.')
        print('You have yet to find the Object.')

    def manipulate(self, catalyst):
        """This function allows the Player to interact with Catalysts,
        which change the structure of rooms they are in (mainly by revealing hidden Doors)."""
        if isinstance(catalyst, Catalyst):
            print(f'\nYou {catalyst.verb} the {catalyst.name}.')
            catalyst.transform()
        else:
            print('You can\'t manipulate that.')

    def dialogue(self, thou):
        """This function allows the Player to enter into dialogue with a Thou."""
        thou.respond(self)