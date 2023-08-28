class Door:
    """Doors connect Rooms and can be locked or hidden."""
    id_counter = 1

    def __init__(self, direction, leads_to, **kwargs):
        self.id = Door.id_counter                    # IDs are used in the repr and for debugging purposes
        Door.id_counter += 1
        self.direction = direction                   # At present direction is only used to orient the user
        self.leads_to = leads_to                     # Where the door goes
        self.locked = kwargs.get('locked', False)    # Locked doors must be unlocked with a key to be passed through
        self.hidden = kwargs.get('hidden', False)    # Hidden doors cannot be seen or interacted with
        self.passed = kwargs.get('passed', False)    # Passed doors report their destination when described (Before passing the 
                                                     # door the Player doesn't know what's on the other side)
        self.warning = kwargs.get('warning', '')     # The warning gives the player one more chance not to go through

    def __repr__(self):
        return f'Door {self.id} | {self.direction} to {self.leads_to.name}'

    def unlock(self):
        self.locked = False

class Stairs(Door):
    """Stairs are Doors that lead up or down."""
    def __init__(self, direction, leads_to, **kwargs):
        self.id = Door.id_counter                   
        Door.id_counter += 1
        self.direction = direction                   
        self.leads_to = leads_to                     
        self.locked = kwargs.get('locked', False)    
        self.hidden = kwargs.get('hidden', False)    
        self.passed = kwargs.get('passed', False)
        self.warning = kwargs.get('warning', '')

    def __repr__(self):
        return f'Stairs {self.id} | {self.direction} to {self.leads_to.name}'