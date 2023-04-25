"""
Contains the EntityTypes class, and the EntityTypeList.
"""

from entities.Entity import Entity
from entities.EntityLight import EntityLight
from entities.EntityLightControl import EntityLightControl
from entities.EntityUndo import EntityUndo
from entities.EntityTitle import EntityTitle
from entities.EntityNormal import EntityNormal
from entities.EntityQuit import EntityQuit
from entities.EntityScore import EntityScore
from entities.EntityAward import EntityAward
from entities.EntityBackground import EntityBackground

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

        self.Light = 0

        self.LightControl = 1

        self.Undo = 2

        self.Title = 3

        self.Normal = 4

        self.Quit = 5

        self.Score = 6

        self.Award = 7

        self.Background = 8

    def getNewEntity(self,entity_type):
        match entity_type:

            case self.Light:
                return EntityLight()

            case self.LightControl:
                return EntityLightControl()
            
            case self.Undo:
                return EntityUndo()
            
            case self.Title:
                return EntityTitle()
            
            case self.Normal:
                return EntityNormal()
            
            case self.Quit:
                return EntityQuit()
            
            case self.Score:
                return EntityScore()
            
            case self.Award:
                return EntityAward()
            
            case self.Background:
                return EntityBackground()

            case _:
                return Entity()

EntityTypeList = EntityTypes()
"""
The list of all EntityTypes. See 'EntityList.py' for more information.

NOTE: Any new entity types must be added in 'EntityList.py' to the
EntityTypes class.
"""