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
    ],
    'laboratory': [[
        (
        'Laboratory',
        'A disused laboratory.',
        'Entering the laboratory is like stepping into another time and place entirely.  gives the impression of having been abandoned hastily and never returned to. A single fluorescent tube light in a metal housing suspended by two chains from the particle board ceiling. There are papers scattered about everywhere, but most are so damaged as to be illegible. The northwest corner appears to have contained a large, heavy object, since removed. A sink and eyewash station are next to the door.'
        ),
        'vanilla'
        ],
        {}
    ],
    'hall_of_easts': [[
        (
        'Hall of Infinite Easts',
        'An infinite hall in one direction.',
        'The Hall of Infinite Easts is less spectacular than you would have guessed from the name. It is a short and simple hallway with decor matching that of the main hall. There is a small table by the west door and two full-length mirrors facing each other on the north and south walls halfway across the hallway. If you wish, you can stand between them and see yourself reflected infinitely in either direction.'
        ),
        'vanilla'
        ],
        {}
    ],
    'hallway': [[
        (
        'Hallway',
        'An L-shaped hallway.',
        'An unremarkable hallway that travels a few meters north before making a ninety-degree turn to the west, where it ends in a door.'
        ),
        'transformer'
        ],
        {
            'new_blurb': 'A T-shaped hallway.',
            'new_description': 'A moderately remarkable T-shaped hallway that travels north before branching east and west. The two branches are identical, save for the rubble from the collapsed wall in the eastern branch.',
            'transformation_message': 'The wall to your right collapses, revealing a previously hidden branch of the hallway!'
        }
    ],
    'library': [[
        (
        'Library',
        'The library of OOP Manor.',
        'Library description.'
        ),
        'vanilla'
        ],
        {}
    ],
    'tower': [[
        (
        'Tower',
        'A stone tower with a spiral staircase.',
        'Tower description.'
        ),
        'dangerstairwell'
        ],
        {'death_message': 'As you climb, you stray too close to the edge and slip when a loose stone breaks off of a step. You plummet into the pit below.'}
    ],
    'outside':  [[
        (
        'Outside',
        'Outside of OOP Manor.',
        'To leave the Manor is to abandon your quest.'
        ),
        'vanilla'
        ],
        {}
    ],
    'death': [[
        (
        'Death',
        'Where the player dies.',
        'The destiantion for deathtrap doors.'
        ),
        'vanilla'
        ],
        {}
    ],
    'placeholder': [[
        (
        'Placeholder',
        'Placeholder room.',
        'The /dev/null of rooms.'
        ),
        'vanilla'
        ],
        {}
    ] 
}

room_instances = {}