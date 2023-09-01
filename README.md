# Adventures in OOP Manor:
## *Search for the Lost Object*

### About the project
I'm making a text adventure to deepen and refine my **object-oriented programming** skills. It's been a lot of fun so far and could even be a step toward my goal of eventually creating a roguelike.

### About the game
You play an adventurer just arrived at OOP Manor, looking for the fabled Object. Will you succeed where others failed? Have others failed? Has anyone even tried this?

Gameplay is standard for a text adventure: walk from room to room, read descriptions, take and manipulate items, solve puzzles, laugh at my jokes! I don't know how elaborate it will be, but the OOP approach means once the formal groundwork is laid, adding more rooms/items/puzzles will be relatively easy.

The game is not yet playable.

### Prerequisites
At present AOOPM requires only **Python 3**, with no additional packages or dependencies. Specifically, I'm writing it in **Python 3.11.3**. For this reason it should be extremely portable, able to run on any OS on which Python can be installed, whether it be Linux, macOS, Windows, or something more exotic!

### Installation
TBD once I'm further along

### License
Adventures in OOP Manor is [free software](https://www.fsf.org/about/what-is-free-software), released under version 3.0 of the GPL. Everyone has the right to use, modify, and distribute Adventures in OOP Manor subject to the [stipulations](https://github.com/jwjacobson/oopmanor/blob/main/License) of that license.

### Reflections
Approach-wise, I find my work to be dominated by two possibly related tensions. The first is the tension between generality and specificity. On the one hand I feel like the big advantage of OOP is the generality of the objects created and thus the modularity of the app. It's always possible to ask, "am I being sufficiently general in how I define this object/function/etc.?" On the other hand it's not possible for me at this point in my development to fully map out everything before starting. Often what gets written is what works for the specific case I'm writing it for, even when I know I'll have to come back later if I ever want to extend its use. I am comfortable with this non-ideal approach, especially since the ideal one would seem to require perfect knowledge.

The other major tension, perhaps more specific to this project than the first, is between how much of the game world is explicitly modeled by the objects and their attributes and how much is simply indicated textually for the player. For example, each Item object has a position attribute, which is a string describing where in a room the item is found. My hope is that the existence of the position attribute adds to the depth of the world constructed by the player: instead of simply seeing "a key," they see  "a key on the floor." For now at least, the position function is purely textual in that I do not spatially model the rooms, which seems sufficient in this case but makes me wonder about situations in which both approaches are possible for the same feature: object modeling or mere textual description. It's something I'll be keeping in mind.   
