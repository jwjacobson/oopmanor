class Item:
    def __init__(self, name, description, position):
        self.name = name
        self.description = description
        self.position = position

    def __repr__(self):
        return f'Item | {self.name}'

    