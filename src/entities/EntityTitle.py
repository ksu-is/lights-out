"""
The title text entity class.
"""

import pygame
import util
from common import states
import error
import sound
import math
from entities.Entity import Entity

class EntityTitle(Entity):
    """
    The title button entity class. The actual title text
    """
    def __init__(self):
        try:
            super().__init__()
            self.EntityType = 3
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
            self.AnimTimer = 0

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
        self.EntityRect[1] -= 240

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
                    sound.playSound("button_press")
                    if self.EntityImageSource == "title_on": self.EntityImageSource = "title_off"
                    else: self.EntityImageSource = "title_on"

        pass

        if self.AnimState == 0:
            if self.AnimTimer < 999999: self.AnimTimer += 1
            else: self.AnimTimer = 0
            self.EntityRect[1] = 32+math.cos(self.AnimTimer/60)*2
        elif (self.AnimState == 1):
            if (self.EntityRect[1] < 32): self.EntityRect[1] += 3
            else:
                self.EntityRect[1] = 32
                self.AnimState = 0
                sound.playSound("gui_fall")
        elif (self.AnimState == 2):
            if (self.EntityRect[1] < 152): self.EntityRect[1] += 3
            else:
                self.EntityRect[1] = 152
                self.AnimState = 3
        elif self.AnimState == 3:
            self.EntityRect[1] = 152


