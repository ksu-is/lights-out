'''
Constants, common functions, and other shared material
'''

class EntityTypes:
    '''
    Class being used as a list of constants for every unique EntityType.
    EntityTypes are the values used to search for entities of a specific
    type or class, for the purpose of creating, destroying, or modifying
    particular types.

    NOTE: Every unique EntityType must be added to this class.
    '''
    def __init__(self):

        self.Player = 0
        self.Wall = 1
        self.Enemy = 2
        self.Example = 3


EntityTypeList = EntityTypes()
'''
The list of all EntityTypes. See 'common.py' for more information.

NOTE: Any new entity types must be added in 'common.py' to the
EntityTypes class.
'''

class StateList:
    BEGIN = -1
    NORMAL = 0
    PAUSED = 1
    MENU = 2

states = StateList()