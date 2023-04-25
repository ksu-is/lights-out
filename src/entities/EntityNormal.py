"""
The normal play button entity class.
"""

import pygame
import util
from common import states
import error
import sound
from entities.Entity import Entity

class EntityNormal(Entity):
    """
    The normal play button entity class. Should begin a normal game
    """
    def __init__(self):
        try:
            super().__init__()
            self.EntityType = 4
            self.EntityName = ""
            self.EntityImageSource = ""

            self.EntityRect = pygame.Rect(0,0,0,0)

            self.EntityVisible = True

            self.EntityDepth = 1000

            self.RestrictUpdate = False
            self.UpdateStates = [states.NORMAL]

            self.RequiresInputs = True #eventually replace this with false, Player and UI elements will likely be the only entities which need inputs

            self.Inputs = []

            self.AnimState = 0

            self.EntityImages.append(["normal_off",pygame.Rect(0,0,48,16),True])
            self.EntityImages.append(["normal_on",pygame.Rect(0,0,48,16),True])

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
        self.EntityRect[1] -= 200

        self.EntityImages[0][1][0] = self.EntityRect[0]
        self.EntityImages[1][1][0] = self.EntityRect[0]

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

        self.EntityImages[0][1][1] = self.EntityRect[1]
        self.EntityImages[1][1][1] = self.EntityRect[1]+24

        self.EntityImages[0][1][0] = self.EntityRect[0]
        self.EntityImages[1][1][0] = self.EntityRect[0]



        for event in self.Inputs:
            if event.type == pygame.MOUSEBUTTONUP:
                if entity_handler.mouseOverEntity(self):
                    if self.EntityImageSource == "normal_off" and self.AnimState == 0:
                        self.EntityImageSource = "normal_on"
                        self.AnimState = 2
                        for entity in entity_handler.EntityList:
                            if entity.EntityType == 3:
                                entity.AnimState = 2

        if (self.AnimState == 1):
            if (self.EntityRect[1] < 64): self.EntityRect[1] += 3
            else:
                self.EntityRect[1] = 64
                self.AnimState = 0
        elif (self.AnimState == 2):
            if (self.EntityRect[1] < 184): self.EntityRect[1] += 3
            else:
                self.EntityRect[1] = 184
                self.AnimState = 0

                self.beginGame(entity_handler,app,0)

                #entity_handler.createEntity(app,1,(0,0,0,0),"LightControl","")

        pass

    def beginGame(self,entity_handler,app,difficulty):
        entity = entity_handler.createEntity(app,1,(0,0,0,0),"LightControl","")
        entity.Difficulty = difficulty

