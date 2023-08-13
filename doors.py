class Door:
    def __init__(self, direction, leads_to, locked=False, hidden=False, passed=False):
        self.direction = direction
        self.leads_to = leads_to
    
    def __repr__(self):
        return f'Door | to {self.leads_to.name}'

# entrance = Room('Entrance', 'The entrance to OOP Manor.')
# test_door = Door('n', leads_to=entrance)
# print(test_door)
