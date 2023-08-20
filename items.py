class Item:
    id_counter = 1

    def __init__(self, name, blurb, description, location, position, hidden=False, takeable=True, failure_message=''):
        self.id = Item.id_counter
        Item.id_counter += 1
        self.name = name
        self.blurb = blurb
        self.description = description
        self.location = location
        self.position = position
        self.hidden = hidden
        self.takeable = takeable
        self.failure_message = failure_message

    def __repr__(self):
        return f'Item {self.id} | {self.name} | {self.blurb}'

    def vanish(self):
        """Keys are destroyed after use."""
        print(f'The {self.name} crumbles to dust!')
        del self

    def populate_hints(self):
    # populate ghost hints
        self.hints = set()
        with open("./hints.txt") as hints:
            Hints = hints.readlines()
            for hint in Hints:
                self.hints.add(hint.strip())


"""
The idea below was to have subclasses for different Item types that would specify their use via attributes and functions.
It turns out that at least in the case of keys (the only item to exist so far) the use function - unlocking a door - belongs to the Player, and it checks if a key is in inventory before executing. I'm leaving the subclass commented out below in case I decide to use it or something similar in the future.
"""
# class Key(Item):
#     def __init__(self, name, description, location, position, hidden=False):
#         self.id = Item.id_counter
#         self.name = name
#         self.description = description
#         self.location = location
#         self.position = position
#         self.hidden = hidden