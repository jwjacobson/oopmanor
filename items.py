class Item:
    def __init__(self, name, description, location, position, hidden=False):
        self.name = name
        self.description = description
        self.location = location
        self.position = position
        self.hidden = hidden

    def __repr__(self):
        return f'Item | {self.name}'

class Key(Item):
    def __init__(self, name, description, location, position, hidden=False):
        self.name = name
        self.description = description
        self.location = location
        self.position = position
        self.hidden = hidden