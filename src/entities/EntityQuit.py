"""
The quit button entity class.
"""

import pygame
import util
from common import states
import error
import sound
from entities.Entity import Entity

class EntityQuit(Entity):
    """
    The quit button entity class. Should primarily only handle input, lightcontrol will handle most logic
    """
    def __init__(self):
        try:
            super().__init__()
            self.EntityType = 5
            self.EntityName = ""
            self.EntityImageSource = ""

            self.EntityRect = pygame.Rect(0,0,0,0)

            self.EntityVisible = True

            self.EntityDepth = 1000

            self.RestrictUpdate = False
            self.UpdateStates = [states.NORMAL]

            self.RequiresInputs = True #eventually replace this with false, Player and UI elements will likely be the only entities which need inputs

            self.AnimState = 0

            self.FinalX = 0
            self.FinalY = 0

            self.Inputs = []

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

        self.FinalX = self.EntityRect[0]
        self.FinalY = self.EntityRect[1]

        self.EntityRect[0] -= 48
        self.AnimState = 1

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
        
        if self.getCanPlayerMove(entity_handler):
            if entity_handler.mouseOverEntity(self):
                self.EntityImageSource = "quit_hover"
            elif self.EntityImageSource != "quit_off": self.EntityImageSource = "quit_off"


        for event in self.Inputs:
            if event.type == pygame.MOUSEBUTTONUP:
                if entity_handler.mouseOverEntity(self):
                    if self.getCanPlayerMove(entity_handler):
                        sound.playSound("button_press")
                        self.EntityImageSource = "quit_on"
                        self.getLightControl(entity_handler).EntityTimers.append([5, self.getLightControl(entity_handler).quitGame])
                        self.getLightControl(entity_handler).CanPlayerMove = False

        if self.AnimState == 0:
            self.EntityRect[0] = self.FinalX
            self.EntityRect[1] = self.FinalY
        elif self.AnimState == 1:
            if self.EntityRect[0] < self.FinalX: self.EntityRect[0] += 2
            else: self.AnimState = 0
        elif self.AnimState == 2:
            if self.EntityRect[0] > self.EntityRect[0]-48: self.EntityRect[0] -= 2
            else: entity_handler.destroyEntity("Quit")

        pass

    def getLightControl(self,entity_handler):
        for entity in entity_handler.EntityList:
            if entity.EntityType == 1:
                return entity
        return None

    def getCanPlayerMove(self,entity_handler):
        tmp = self.getLightControl(entity_handler)
        if tmp != None:
            return tmp.CanPlayerMove
        return False