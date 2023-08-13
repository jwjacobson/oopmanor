from player import *

# print('Welcome, adventurer!')
# name = input('What is your name? ')
# player = Player(name, entrance)
# print(f'Player {player.name} created.')
# player.get_location()

player = Player('ababu', location=entrance)
player.check_location()
player.take_item(key)
player.check_inventory()
player.check_location()