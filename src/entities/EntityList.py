"""
Contains the EntityTypes class, and the EntityTypeList.
"""

from entities.Entity import Entity

class EntityTypes:
    """
    Class being used as a list of constants for every unique EntityType.
    EntityTypes are the values used to search for entities of a specific
    type or class, for the purpose of creating, destroying, or modifying
    particular types.

    NOTE: Every unique EntityType must be added to this class in two places:
    \nfirst, in the __init__ function,
    \nsecond, in the getNewEntity function
    """
    def __init__(self):

        self.Player = 0

        self.Wall = 1

        self.Enemy = 2

        self.Example = 3

    def getNewEntity(self,entity_type):
        match entity_type:

            case self.Player:
                return Entity()

            case self.Wall:
                return Entity()

            case _:
                return Entity()

EntityTypeList = EntityTypes()
"""
The list of all EntityTypes. See 'EntityList.py' for more information.

NOTE: Any new entity types must be added in 'EntityList.py' to the
EntityTypes class.
"""