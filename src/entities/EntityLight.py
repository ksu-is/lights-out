"""
The light entity class.
"""

import pygame
import util
from common import states
import error
import sound
from entities.Entity import Entity

class EntityLight(Entity):
    """
    The light entity class. Should handle all possible states a 'light' may have
    """
    def __init__(self):
        try:
            super().__init__()
            self.EntityType = 0
            self.EntityName = ""
            self.EntityImageSource = ""

            self.EntityRect = pygame.Rect(0,0,0,0)

            self.EntityVisible = True

            self.EntityDepth = 1000

            self.RestrictUpdate = False
            self.UpdateStates = [states.NORMAL]

            self.RequiresInputs = True #eventually replace this with false, Player and UI elements will likely be the only entities which need inputs

            self.Inputs = []

            self.PowerX = 0
            self.PowerY = 0

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
        


        for event in self.Inputs:
            if event.type == pygame.MOUSEBUTTONUP:
                if entity_handler.mouseOverEntity(self):
                    if self.getCanPlayerMove(entity_handler):
                        self.initialFlip(entity_handler)
                        # self.getLightControl(entity_handler).CanPlayerMove = False

        pass

    def initialFlip(self,entity_handler):
        for entity in entity_handler.EntityList:
            if entity.EntityType == 0:
                if abs(self.PowerX-entity.PowerX)<=1 and abs(self.PowerY-entity.PowerY)<=1:
                    entity.secondaryFlip(entity_handler)
        if self.getLightControl(entity_handler) != None:
            if self.getLightControl(entity_handler).CanPlayerMove:
                self.getLightControl(entity_handler).checkForSolution(entity_handler)
                self.getLightControl(entity_handler).updateMoveTracker(entity_handler)

    def secondaryFlip(self,entity_handler):
        if self.EntityImageSource == "light_off":
            self.EntityImageSource = "light_on"
            if (self.getLightControl(entity_handler) != None):
                self.getLightControl(entity_handler).PowerGrid[self.PowerX][self.PowerY] = 1
        else:
            self.EntityImageSource = "light_off"
            if (self.getLightControl(entity_handler) != None):
                self.getLightControl(entity_handler).PowerGrid[self.PowerX][self.PowerY] = 0

    def getLightControl(self,entity_handler):
        for entity in entity_handler.EntityList:
            if entity.EntityType == 1:
                return entity
            else: return None

    def getCanPlayerMove(self,entity_handler):
        tmp = self.getLightControl(entity_handler)
        if tmp != None:
            return tmp.CanPlayerMove
        return False