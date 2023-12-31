import os
import timings

class Item:
    """Items are general-purpose objects; they are the things in Rooms the Player can interact with.
    They can be taken, dropped, moved to other rooms, and examined for information.
    Certain items must be present for the Player to perform certain actions."""
    id_counter = 1

    def __init__(self, name, blurb, description, location, position, hidden=False, takeable=True, failure_message='', reveal_message=''):
        self.id = Item.id_counter               # IDs are used in the repr and for debugging purposes
        Item.id_counter += 1
        self.name = name
        self.blurb = blurb                      # short description - might be superfluous
        self.description = description          # detailed description
        self.location = location                # the room where the item is, unless in inventory
        self.position = position                # a phrase describing position in the room, for variety
        self.hidden = hidden                    # hidden items do not appear
        self.takeable = takeable                # whether or not an item can be taken into inventory
        self.failure_message = failure_message  # displays if the player tries to take an untakeable item
        self.reveal_message = reveal_message    # displays when a hidden item becomes unhidden

    def __repr__(self):
        return f'Item {self.id} | {self.name}'

    def vanish(self):
        """Keys are destroyed after use, but this function can destroy any item."""
        print(f'The {self.name} crumbles to bits!')
        del self

    


class Concealer(Item):
    """A concealer hides another item behind or under it. Taking the concealer reveals the hidden item."""
    def __init__(self, name, blurb, description, location, position, hides: Item, hidden=False, takeable=True, failure_message='', reveal_message=''):
        super().__init__(name, blurb, description, location, position, hidden, takeable, failure_message, reveal_message)
        self.hides = hides              # unique to Concealers: the item hidden by the Concealer

    def __repr__(self):
        return f'Item {self.id} (Concealer) | {self.name}'

    def unconceal(self):
        self.hides.hidden = False
        print(self.hides.reveal_message)

class Catalyst(Item):
    """A catalyst alters the structure of a room when manipulated.
    As a rule catalysts are untakeable, more like features of a room than true items."""
    def __init__(self, name, blurb, description, location, position, transforms, verb, hidden=False, takeable=False, failure_message='', reveal_message=''):
        super().__init__(name, blurb, description, location, position, takeable, failure_message, reveal_message)
        self.transforms = transforms              # unique to Catalyst: the Room altered by the Catalyst
        self.verb = verb                          # the verb the Player uses when manipulating the Catalyst

    def __repr__(self):
        return f'Item {self.id} (Catalyst) | {self.name}'

    def transform(self):
        """This function transforms the room and is called when the catalyst is manipulated by the player."""
        print(self.transforms.transformation_message)
        self.transforms.blurb = self.transforms.new_blurb
        self.transforms.description = self.transforms.new_description
        for door in self.transforms.doors:                 # this assumes that the transformation will reveal a hidden door or doors
            if door.hidden:
                door.hidden = False

class Thou(Item):
    """A Thou is an item with which the player can enter into dialogue.
    (see https://plato.stanford.edu/entries/buber/#DiaITho)."""
    def __init__(self, name, blurb, description, location, position, menu, hidden=False, takeable=False, failure_message='', reveal_message='', titles=None, poems=None):
        super().__init__(name, blurb, description, location, position, takeable, failure_message, reveal_message)
        self.menu = menu        # The menu holds the Thou's dialogue options
        import poem_data
        self.poems = poem_data.poems
        self.titles = poem_data.titles

    def populate_hints(self):
        """This function takes hints from a separate file and stores them in a set for use by the Hint Ghost."""
        self.hints = set()
        with open("./testhints.txt") as hints:
            Hints = hints.readlines()
            for hint in Hints:
                self.hints.add(hint.strip())

    def give_hint(self, player):
        """This method gives a hint"""
        print('\n')
        print(self.hints.pop())

    def recite(self, poem):
        print('\nThe Hint Ghost begins to recite...')
        timings.rest(3)
        if os.name == 'posix':
            os.system('clear')
        # this should clear the screen on windows systems
        elif os.name == 'nt':
            os.system('cls')
        print('')
        for line in poem:
            timings.sprint(line)
        print('')
        timings.rest(4)

    def respond(self, player):
        """This function allows a Thou to respond to the initiation of dialogue by the Player.
        Currently it's tailored to the Hint Ghost, the only Thou. If I add another I'll generalize."""
        print(f"You address the {self.name}.")
        total_hints = len(self.hints)
        while True:
            hints_left = len(self.hints)
            hints_heard = total_hints - hints_left
            print('\nAvailable options:')
            for num, qa in self.menu.items():
                print(f'({num}). {qa[0]}')
            print(f'\n(You\'ve heard {hints_heard} of {total_hints} hints)')
            prompt = input('\nWhat would you like to say? ')
            while prompt not in self.menu.keys():
                prompt = input('Choose one of the options above. ' )
            print(f'\n{self.menu[prompt][0]}')
            print(self.menu[prompt][1])
            if prompt == '2':
                self.give_hint(player)
                if hints_left == 1:
                    print('\nYou\'ve heard all my hints!')
                    print('\nYou now have the option to hear me recite poetry!')
                    self.menu['4'] = ('I want to hear a poem.', 'Very well.')
            elif prompt == '3':
                break
            elif prompt == '4':
                self.recite(self.poems[self.titles.pop()])
                
