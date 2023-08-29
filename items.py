class Item:
    """Items are general-purpose objects; they are the things in Rooms the Player can interact with.
    They can be taken, dropped, moved to other rooms, and examined for information.
    Certain items must be present for the Player to perform certain actions."""
    id_counter = 1

    def __init__(self, name, blurb, description, location, position, hidden=False, takeable=True, failure_message='', reveal_message=''):
        self.id = Item.id_counter
        Item.id_counter += 1
        self.name = name
        self.blurb = blurb                      # short description - might be superfluous
        self.description = description          # detailed description
        self.location = location                # the room where the item is, unless in inventory
        self.position = position                # a phrase describing position in the room, for variety
        self.hidden = hidden                    # hidden items do not appear
        self.takeable = takeable                # whether or not an item can be taken into inventory
        self.failure_message = failure_message  # displays if the player tries to take an untakeable item
        self.reveal_message = reveal_message    # displays when a hidden item becomes unhidden

    def __repr__(self):
        return f'Item {self.id} | {self.name}'

    def vanish(self):
        """Keys are destroyed after use, but this function can destroy any item."""
        print(f'The {self.name} crumbles to bits!')
        del self

    def populate_hints(self):
        """This function takes hints from a separate file and stores them in a set for use by the Hint Ghost."""
        self.hints = set()
        with open("./hints.txt") as hints:
            Hints = hints.readlines()
            for hint in Hints:
                self.hints.add(hint.strip())


class Concealer(Item):
    """A concealer hides another item behind or under it. Taking or otherwise manipulating the concealer reveals the hidden item."""
    def __init__(self, name, blurb, description, location, position, hides: Item, hidden=False, takeable=True, failure_message='', reveal_message=''):
        self.id = Item.id_counter
        Item.id_counter += 1
        self.name = name
        self.blurb = blurb
        self.description = description
        self.location = location
        self.position = position
        self.hides = hides              # unique to Concealers: the item hidden by the Concealer
        self.hidden = hidden
        self.takeable = takeable
        self.failure_message = failure_message
        self.reveal_message = reveal_message

    def __repr__(self):
        return f'Item {self.id} | {self.name} | Conceals {self.hides}'

    def unconceal(self):
        self.hides.hidden = False
        print(self.hides.reveal_message)

class Catalyst(Item):
    """A catalyst alters the structure of a room when manipulated.
    As a rule catalysts will be untakeable, more like features of a room than true items."""
    def __init__(self, name, blurb, description, location, position, transforms, verb, hidden=False, takeable=False, failure_message='', reveal_message=''):
        self.id = Item.id_counter
        Item.id_counter += 1
        self.name = name
        self.blurb = blurb
        self.description = description
        self.location = location
        self.position = position
        self.transforms = transforms              # unique to Catalyst: the Room altered by the Catalyst
        self.verb = verb                          # the verb the Player uses when manipulating the Catalyst
        self.hidden = hidden
        self.takeable = takeable
        self.failure_message = failure_message
        self.reveal_message = reveal_message

    def __repr__(self):
        return f'Item {self.id} | {self.name} | Transforms {self.transforms.name}'

    def transform(self):
        print(self.transforms.transformation_message)
        self.transforms.blurb = self.transforms.new_blurb
        self.transforms.description = self.transforms.new_description
        for door in self.transforms.doors:                 # this assumes that the transformation will reveal a hidden door or doors
            if door.hidden:
                door.hidden = False