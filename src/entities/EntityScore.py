"""
The quit button entity class.
"""

import pygame
import util
from common import states
import error
import sound
from entities.Entity import Entity
import math

class EntityScore(Entity):
    """
    The score entity class. Should primarily only handle rendering, lightcontrol will handle most logic
    """
    def __init__(self):
        try:
            super().__init__()
            self.EntityType = 6
            self.EntityName = ""
            self.EntityImageSource = ""

            self.EntityRect = pygame.Rect(0,0,0,0)

            self.EntityVisible = True

            self.EntityDepth = 1000

            self.RestrictUpdate = False
            self.UpdateStates = [states.NORMAL]

            self.RequiresInputs = True #eventually replace this with false, Player and UI elements will likely be the only entities which need inputs

            self.EntityImages = []

            self.Inputs = []

            self.Wins = 0

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

        self.Wins = 0

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
    
    def addWin(self,entity_handler):
        self.Wins += 1

        tmp_image = "score_small"

        tmp_x = 116
        tmp_y = 21
        tmp_s = 4

        tmp_row = util.clamp(math.floor((self.Wins-1)/5),0,math.floor((self.Wins-1)/5))
        tmp_column = self.Wins-tmp_row*5

        tmp_x += 5*tmp_column
        tmp_y += 8*tmp_row

        if tmp_column == 5:
            if math.remainder(tmp_row+1,3) == 0: tmp_image = "score_big"
            else: tmp_image = "score_medium"

        if tmp_image == "score_big":
            tmp_s = 6
            tmp_y -= 1
        self.EntityImages.append([tmp_image,pygame.Rect(tmp_x,tmp_y,tmp_s,tmp_s),True])