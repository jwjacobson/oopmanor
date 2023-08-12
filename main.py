class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
    
    def __repr__(self):
        return f'Room {self.name}'

class Player:
    def __init__(self, name, location: Room):
        self.name = name
        self.location = location
    
    def __repr__(self):
        return f'Player {self.name}'

    def get_location(self):
        print(f'You are in the {self.location.name}.')

entrance = Room('Entrance', 'The entrance to OOP Manor.')
print('Welcome, adventurer!')
name = input('What is your name? ')
player = Player(name, entrance)
print(f'Player {player.name} created.')
player.get_location()