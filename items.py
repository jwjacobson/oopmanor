class Item:
    def __init__(self, name, description, location, position):
        self.name = name
        self.description = description
        self.location = location
        self.position = position

    def __repr__(self):
        return f'Item | {self.name}'
