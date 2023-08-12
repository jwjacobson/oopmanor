class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def __repr__(self):
        return f'Room {self.name}'

rooms = []

entrance = Room('Entrance', 'The entrance to OOP Manor.')
rooms.append(entrance)
foyer = Room('Foyer', 'The foyer of OOP Manor.')
rooms.append(foyer)
