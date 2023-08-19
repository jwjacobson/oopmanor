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
player.unlock_door()
player.take_item(key)
player.move(foyer)
player.unlock_door()
player.move(foyer)
# player.check_inventory()
# player.move(entrance)
# player.move(foyer)
# player.look_around()
# player.move(entrance)
# player.take_item(key)
# player.move(foyer)
# player.drop_item(key)
# player.look_around()
# player.move(entrance)
# player.check_location()
# player.check_inventory()
# player.check_location()
# player.drop_item(key)
# player.check_location()
# player.take_item(wallet)
# player.drop_item(wallet)