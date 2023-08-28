from player import *

"""
speculative manor generation sequence:
generate rooms
generate doors
generate items
"""


# print('Welcome, adventurer!')
# name = input('What is your name? ')
# player = Player(name, entrance)
# print(f'Player {player.name} created.')
# player.get_location()

player = Player('ababu', location=foyer)
player.arrive()
player.unlock_door()
player.take(key)
player.move(main_hall)
player.unlock_door()
player.move(main_hall)
player.move(laboratory)
player.take(lighter)
player.move(hallway)
player.move(library)
player.candle_switch()
# player.candle_switch()
player.take(candle)
player.move(hallway)
player.take(painting)
player.look_around()
player.open_safe()
player.take(note)
player.examine(note)
switch.transform(hallway)
player.look_around()
player.move(tower)
player.climb_stairs(death)
# player.status()
# tower.kill(player)
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