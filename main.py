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


entrance = Room('Entrance', 'The entrance to OOP Manor.')
print('Welcome, adventurer!')
name = input('What is your name? ')
player = Player(name, entrance)
print(f'Player {player.name} created.')
print(f'{player.name} is in the {player.location.name}.')
print(player.location.description)