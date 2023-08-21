class Door:
    id_counter = 1

    def __init__(self, direction, leads_to, **kwargs):
        self.id = Door.id_counter
        Door.id_counter += 1
        self.direction = direction
        self.leads_to = leads_to
        self.locked = kwargs.get('locked', False)
        self.hidden = kwargs.get('hidden', False)
        self.passed = kwargs.get('passed', False)

    def __repr__(self):
        return f'Door {self.id} | {self.direction} to {self.leads_to.name}'

    def unlock(self):
        self.locked = False

