class Item:
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
        """Keys are destroyed after use."""
        print(f'The {self.name} crumbles to bits!')
        del self

    def populate_hints(self):
    # populate ghost hints
        self.hints = set()
        with open("./hints.txt") as hints:
            Hints = hints.readlines()
            for hint in Hints:
                self.hints.add(hint.strip())


class Concealer(Item):
    """A concealer hides another item behind or under it. Taking or otherwise manipulating the concealer reveals the hidden item"""
    def __init__(self, name, blurb, description, location, position, hides: Item, hidden=False, takeable=True, failure_message='', reveal_message=''):
        self.id = Item.id_counter
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

    def unconceal(self):
        self.hides.hidden = False
        print(self.hides.reveal_message)

class Transformer(Item):
    """A transformer alters the structure of a room when manipulated."""
    def __init__(self, name, blurb, description, location, position, transforms: Item, hidden=False, takeable=True, failure_message='', reveal_message=''):
        self.id = Item.id_counter
        self.name = name
        self.blurb = blurb
        self.description = description
        self.location = location
        self.position = position
        self.transforms = transforms              # unique to Transformers: the room altered by the Transformer
        self.hidden = hidden
        self.takeable = takeable
        self.failure_message = failure_message
        self.reveal_message = reveal_message