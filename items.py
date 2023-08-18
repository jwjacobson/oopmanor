class Item:
    id_counter = 1

    def __init__(self, name, description, location, position, hidden=False):
        self.id = Item.id_counter
        Item.id_counter += 1
        self.name = name
        self.description = description
        self.location = location
        self.position = position
        self.hidden = hidden

    def __repr__(self):
        return f'Item {self.id} | {self.name}'

# class Key(Item):
#     def __init__(self, name, description, location, position, hidden=False):
#         self.id = Item.id_counter
#         self.name = name
#         self.description = description
#         self.location = location
#         self.position = position
#         self.hidden = hidden

    # def unlock(self, door):
    #     if door.locked:
    #         door.locked = False
    #         print('You unlock the door.')