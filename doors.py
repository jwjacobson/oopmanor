class Door:
    def __init__(self, direction, leads_to, **kwargs):
        self.direction = direction
        self.leads_to = leads_to
        self.locked = kwargs.get('locked', False)
        self.hidden = kwargs.get('hidden', False)
        self.passed = kwargs.get('passed', False)

    def __repr__(self):
        return f'Door | {self.direction} to {self.leads_to.name}'

# entrance = Room('Entrance', 'The entrance to OOP Manor.')
# test_door = Door('n', leads_to=entrance)
# print(test_door)

# all_doors = {
# 'Entrance':
# {
#     '1': [['north', foyer], {'locked': True}],
#     '2': [['south', 'out',], {'passed': True}]
# }
# }
# print(all_doors['Entrance'][0])