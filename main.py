from player import *

"""
speculative map generation:
generate rooms
generate doors
generate items
"""


# print('Welcome, adventurer!')
# name = input('What is your name? ')
# player = Player(name, entrance)
# print(f'Player {player.name} created.')
# player.get_location()

player = Player('ababu', location=entrance)
player.arrive()
player.move(foyer)
print(player.location)
# player.check_location()
# player.take_item(key)
# player.check_inventory()
# player.check_location()
# player.drop_item(key)
# player.check_location()
# player.take_item(wallet)
# player.drop_item(wallet)