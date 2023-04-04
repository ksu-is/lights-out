"""
The light control entity class.
"""

import pygame
import util
from common import states
import error
import sound
import secrets
from entities.Entity import Entity

class EntityLightControl(Entity):
    """
    The light control entity class. Should be responsible for creating and maintaining the 'grid' of lights
    """
    def __init__(self):
        try:
            super().__init__()
            self.EntityType = 1
            self.EntityName = ""
            self.EntityImageSource = ""

            self.EntityRect = pygame.Rect(0,0,0,0)

            self.EntityVisible = False

            self.EntityDepth = 1000

            self.RestrictUpdate = False
            self.UpdateStates = [states.NORMAL]

            self.RequiresInputs = True 

            self.Inputs = []

            self.SolutionGrid = []

            self.GridWidth = 8
            self.GridHeight = 8

            self.SolutionGrid = [[1 for i in range(self.GridWidth)] for j in range(self.GridHeight)]

            print(self.SolutionGrid)

            self.PowerGrid = [row[:] for row in self.SolutionGrid]

            print(self.PowerGrid)

            self.NumberOfComputerFlips = 10


        except:
            error.causeError("Entity Initializing Error","There was an error in the __init__ function for an entity. This means it happened BEFORE finishing either the createEntity or onCreated functions")

    def onCreated(self,entity_handler,app):
        """
        An entity's creation function.
        This function will only be run once, when the entity is created,
        and it will ONLY run when the entity is created through the
        createEntity method. Useful for initial actions for entities and
        behaviour that should be run immediately for the entity, but
        that don't make sense to include in __init__
        """

        initial_x = 32
        initial_y = 16

        spacing = 12

        tmp_x = initial_x
        tmp_y = initial_y

        for i in range(self.GridWidth):
            for j in range(self.GridHeight):
                tmp_entity = entity_handler.createEntity(app,0,(tmp_x,tmp_y,8,8),"Light","light_on")
                tmp_entity.PowerX = i
                tmp_entity.PowerY = j
                tmp_y += spacing
            tmp_x += spacing
            tmp_y = initial_y

        for l in range(self.NumberOfComputerFlips):
            t_x = secrets.randbelow(self.GridWidth)
            t_y = secrets.randbelow(self.GridHeight)
            for entity in entity_handler.EntityList:
                if entity.EntityType == 0:
                    if (entity.PowerX == t_x and entity.PowerY == t_y):
                        entity.initialFlip(entity_handler)
            pass

        pass

    def onDestroyed(self,entity_handler,app):
        """
        An entity's destruction function.
        This function will only be run once, when the entity is destroyed,
        and it will ONLY run when the entity is destroyed through the
        destroyEntity function. Useful for wrapping up entity logic, or
        handling events which should happen when an entity is destroyed,
        without including it in all the possible behaviours which might
        be used to destroy entities. Also prevents from having to include
        this type of functionality in each entity's onUpdate event.
        """
        pass

    def onUpdate(self,entity_handler,app):
        """
        An entity's update function.
        Every time the main loop is run, all entities in the
        EntityList are checked to see if their own update
        function should run. If yes, then run the function.
        """
        pass

