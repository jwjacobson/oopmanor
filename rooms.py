# from items import *
# from doors import *

class Room:
    """Rooms are the basic spatial units of the Manor. They contain Items and connect to one another via Doors.
    Via their descriptions, they also play an essential role in constituting the world of the game for the user."""
    id_counter = 1

    def __init__(self, name, blurb, description, doors=None, items=None, visited=False):
        if doors is None:               # These conditionals avoid the issue of having a mutable data structure as a default value
            doors = []
        if items is None:
            items = []
        self.id = Room.id_counter       # IDs are used in the repr and for debugging purposes
        Room.id_counter += 1
        self.name = name
        self.blurb = blurb              # A short description, possibly superfluous
        self.description = description  # The full description read upon first entering a room or when examining it
        self.doors = doors              # The doors in the room
        self.items = items              # The items in the room
        self.visited = visited          # Whether or not the player has been to the room

    def __repr__(self):
        return f'Room {self.id} | {self.name}'

    def remove_item(self, item):
        """This function removes an item from the Room.
        At present it is only called when the player takes an item."""
        self.items.remove(item)

    # def populate_doors(self):
    #     """This function reads the dictionary all_doors to add the doors to a room.
    #     The print statements can be selectively commented/uncommented for debugging purposes."""
    #     from doordata import all_doors
    #     # print(f'Populating doors for {self}...')
    #     for door in all_doors[self.name]:
    #         self.doors.append(Door(*all_doors[self.name][door][0], **all_doors[self.name][door][1]))
    #         # print(f'Door {self.doors[-1].id} created.')
    #     # print(f'Population complete. {self} contains the following doors:')
    #     # for door in self.doors:
    #     #     print(door)

    def describe_doors(self):
        """This function describes the doors in a Room."""
        for door in self.doors:
            if door.hidden:
                continue
            elif door.passed:
                print(f'There is a door to the {door.direction}, leading to the {door.leads_to.name}.')
            else:
                print(f'There is a door to the {door.direction}.')
        if isinstance(self, Stairwell):
            self.describe_stairs()

class Transformer(Room):
    """A Transformer is a Room that changes shape when its Catalyst is manipulated by the Player.""" 
    def __init__(self, name, blurb, description, new_blurb, new_description, doors=None, items=None, visited=False, transformation_message=''):
        super().__init__(name, blurb, description, doors, items, visited)
        self.new_blurb = new_blurb              # A new short description post-transformation
        self.new_description = new_description  # A new full description post-transformation
        self.transformation_message = transformation_message # A message describing the transformation when it occurs

    def __repr__(self):
        return f'Room {self.id} | {self.name}'

class Stairwell(Room):
    """A Stairwell is a Room that contains Stairs for going up or down.""" 
    def __init__(self, name, blurb, description, doors=None, stairs=None, items=None, visited=False):
        super().__init__(name, blurb, description, doors, items, visited)
        if stairs is None:
            stairs = []
        self.stairs = stairs                             

    def __repr__(self):
        return f'Stairwell {self.id} | {self.name}'

    def describe_stairs(self):
        for stair in self.stairs:
            if stair.hidden:
                continue
            elif stair.passed:
                print(f'There is a stairway leading {stair.direction} into the gloom, towards the {stair.leads_to.name}.')
            else:
                print(f'There is a stairway leading {stair.direction} into the gloom.')

class DangerRoom(Room):
    """A Danger Room is a Room that can kill the Player."""

    def __init__(self, name, blurb, description, doors=None, items=None, visited=False, death_message=''):
        super().__init__(name, blurb, description, doors, items, visited)
        self.death_message = death_message      # The description of the player's death

    def __repr__(self):
        return f'Room {self.id} | {self.name}'

    def kill(self, player):
        print(self.death_message)
        player.die()

class DangerStairwell(Stairwell, DangerRoom):
    """I'm in the Stairwell. I'm in the Danger Room. I'm in the combination Stairwell and Danger Room!"""
    def __init__(self, name, blurb, description, doors=None, stairs=None, items=None, visited=False, death_message=''):
        Stairwell.__init__(self, name, blurb, description, doors, stairs, items, visited)
        DangerRoom.__init__(self, name, blurb, description, doors, items, death_message)
        self.death_message = death_message

    def __repr__(self):
        return f'Room {self.id} | {self.name}'