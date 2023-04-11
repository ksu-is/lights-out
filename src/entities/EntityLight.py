"""
The light entity class.
"""

import pygame
import util
from common import states
import error
import sound
from entities.Entity import Entity
import math

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

            self.LightX = 0
            self.LightY = 0
            self.AnimState = 0
            self.AnimDelay = 0

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
                        self.getLightControl(entity_handler).MoveTracker.append((self.PowerX,self.PowerY))
                        # self.getLightControl(entity_handler).CanPlayerMove = False


        if self.AnimState != 0:
            if self.AnimDelay > 0: self.AnimDelay -= 1
            else:
                if self.AnimState == 1:
                    if self.EntityRect[1] < self.LightY:
                        self.EntityRect[1] += 5
                    elif self.EntityRect[1] > self.LightY:
                        self.EntityRect[1] = self.LightY
                        self.AnimState = 2
                        self.AnimDelay = 15

                elif self.AnimState == 2:
                    self.EntityRect[1] = self.LightY - math.cos(self.AnimDelay)*2
                    if self.AnimDelay == 0: self.AnimState = 0
        else:
            self.EntityRect[0] = self.LightX
            self.EntityRect[1] = self.LightY
        

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
        return None

    def getCanPlayerMove(self,entity_handler):
        print(entity_handler.EntityList)
        tmp = self.getLightControl(entity_handler)
        if tmp != None:
            return tmp.CanPlayerMove
        return False