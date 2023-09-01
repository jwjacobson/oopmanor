class Room:
    """Rooms are the basic spatial units of the Manor. They contain Items and connect to one another via Doors.
    Via their descriptions, they also play an essential role in constituting the world of the game for the user."""
    id_counter = 1

    def __init__(self, name, blurb, description, doors=None, items=None, visited=False):
        if doors is None:               # These conditionals avoid the issue of having a mutable data structure as a default value
            doors = []
        if items is None:
            items = []
        self.id = Room.id_counter       # IDs are used in the repr and for debugging purposes
        Room.id_counter += 1
        self.name = name
        self.blurb = blurb              # A short description, possibly superfluous
        self.description = description  # The full description read upon first entering a room or when examining it
        self.doors = doors              # The doors in the room
        self.items = items              # The items in the room
        self.visited = visited          # Whether or not the player has been to the room

    def __repr__(self):
        return f'Room {self.id} | {self.name}'

class Transformer(Room):
    """A Transformer is a Room that changes shape when its Catalyst is manipulated by the Player.""" 
    def __init__(self, name, blurb, description, new_blurb, new_description, doors=None, items=None, visited=False, transformation_message=''):
        super().__init__(name, blurb, description, doors, items, visited)
        self.new_blurb = new_blurb              # A new short description post-transformation
        self.new_description = new_description  # A new full description post-transformation
        self.transformation_message = transformation_message # A message describing the transformation when it occurs

    def __repr__(self):
        return f'Room {self.id} | {self.name}'

all_rooms = {
    'foyer': [[
        (
        'Foyer',
        'The foyer of OOP Manor.',
        'The foyer of OOP Manor is not large to begin with, dominated by two massive carved-stone planters which fill its east and west sides, leaving only a narrow path to walk through the room. In spite of the lack of windows and general gloom, the tropical vegetation growing from the planters is lush and varied, with vines spilling over the edges and climbing the white-tiled walls. From the center of each planter a stately palm rises nearly to the ceiling where its leaves fan out to form a canopy obscuring the ceiling. You expect to see brightly-plumaged birds or even a monkey startle at your entrance, but the room is completely quiet. Not even the indifferent buzz of insects breaks the silence.'
        ),
        'vanilla'
        ],
        {}
    ],
    'main_hall': [[
        (
        'Main Hall',
        'The Main Hall of OOP Manor.',
        'The cavernous main hall of OOP Manor stretches approximately 50 meters from east to west, anchored in its center by a five-meter, fully-lit chandelier hanging over a long, fully set dining table. Along the far wall hang painted portraits of Manor nobility, their faces glowering down at you. Above the portraits is a mezzanine running along the north and west walls, with several doors spaced regularly along its length, but you don\'t see a way to access it from here. A curtain covers the west wall.'
        ),
        'transformer'
        ],
        {
            'new_blurb': 'The main hall of OOP Manor.',
            'new_description': 'The cavernous main hall of OOP Manor stretches approximately 100 meters from east to west, anchored in its center by a five-meter, fully-lit chandelier hanging over a long, fully set dining table. Along the far wall hang painted portraits of Manor nobility, their faces glowering down at you. Above the portraits is a mezzanine running along the north and west walls, with several doors spaced regularly along its length, but you don\'t see a way to access it from here. The curtain on the west wall has been parted, revealing an incongruous metal door, more suited to a school or factory than what you\'ve seen of the Manor.',
            'transformation_message': 'The curtain parts, revealing a door!'
        }
    ]
    # laboratory: [],
    # hall_of_easts: [],
    # hallway: [],
    # library: [],
    # tower: [],
    # outside: [],
    # death: [],
    # placeholder: []
}

room_instances = {}

def populate_rooms():
    for room_key in all_rooms:
        room_data, room_type = all_rooms[room_key][0]
        if room_type == 'vanilla':
            room_instances[room_key] = Room(*room_data)
        elif room_type == 'transformer':
            extra_data = all_rooms[room_key][1]
            room_instances[room_key] = Transformer(*room_data, **extra_data)

populate_rooms()

foyer = room_instances['foyer']
main_hall = room_instances['main_hall']
print(main_hall.transformation_message)