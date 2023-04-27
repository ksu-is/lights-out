"""
The award marker entity class.
"""

import pygame
import util
from common import states
import error
import sound
from entities.Entity import Entity

class EntityAward(Entity):
    """
    The award marker entity class. Should primarily only handle input, lightcontrol will handle most logic
    """
    def __init__(self):
        try:
            super().__init__()
            self.EntityType = 7
            self.EntityName = ""
            self.EntityImageSource = ""

            self.EntityRect = pygame.Rect(0,0,0,0)

            self.EntityVisible = True

            self.EntityDepth = 1000

            self.RestrictUpdate = False
            self.UpdateStates = [states.NORMAL]

            self.RequiresInputs = True #eventually replace this with false, Player and UI elements will likely be the only entities which need inputs

            self.AnimState = 0
            self.AnimDelay = 10

            self.AwardX = 0
            self.AwardY = 0

            self.AwardNumber = 0

            self.Inputs = []

            self.Flag = True

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

        self.AnimState = 1
        self.EntityRect[0] = self.AwardX
        self.EntityRect[1] = self.AwardY - 200

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

        self.EntityRect[0] = self.AwardX

        if self.AnimDelay > 0: 
            self.AnimDelay -= 1
            if self.AnimState == 2:
                self.EntityRect[1] = self.AwardY + self.AnimDelay/2
                if self.AnimDelay == 0:
                    self.AnimState = 0
                    sound.playSound("award_fall")
        else:
            if self.AnimState == 0:
                self.EntityRect[0] = self.AwardX
                self.EntityRect[1] = self.AwardY
            elif self.AnimState == 1:
                self.EntityRect[1] += 5
                if self.EntityRect[1] > self.AwardY:
                    self.AnimState = 2
                    self.AnimDelay = 15

        if self.AnimState == 3:
            if self.AnimDelay > 0: self.AnimDelay -= 1
            else:
                if self.EntityRect[1] < self.AwardY+16: self.EntityRect[1] += 2
                else:   
                    self.EntityRect[1] += 4
                    if self.Flag:
                        self.Flag = False
                        sound.playSound("award_fall")
                

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