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

            # self.SolutionGrid = [[1 for i in range(self.GridWidth)] for j in range(self.GridHeight)]

            self.SolutionGrid = self.getSolutionGrid(0)

            print(self.SolutionGrid)

            self.PowerGrid = [row[:] for row in self.SolutionGrid]

            print(self.PowerGrid)

            self.NumberOfComputerFlips = 5

            self.NumberOfPlayerFlips = self.NumberOfComputerFlips

            self.CanPlayerMove = False

            self.EntityTimers = []

            self.EntityImages = []

            self.MaxMoves = self.NumberOfComputerFlips

            moveSpacing = 10
            moveX = 80-self.MaxMoves*moveSpacing/2
            moveY = 110

            for u in range(self.MaxMoves):
                if u <= self.NumberOfPlayerFlips: self.EntityImages.append(["move_on",pygame.Rect(moveX+moveSpacing*u,moveY,8,8),True])
                else: self.EntityImages.append(["move_off",pygame.Rect(moveX+moveSpacing*u,moveY,8,8),True])


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
                if (self.SolutionGrid[i][j] == 0): tmp_entity.EntityImageSource = "light_off"
            tmp_x += spacing
            tmp_y = initial_y

        self.mixPowerGrid(entity_handler)

        self.CanPlayerMove = True

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

        for timer in self.EntityTimers:
            if timer[0] > 0: timer[0] = timer[0]-1
            else:
                timer[1](entity_handler)
                self.EntityTimers.remove(timer)

        pass

    def setupGrid(self,entity_handler):

        self.SolutionGrid = self.getSolutionGrid(0)

        self.PowerGrid = [row[:] for row in self.SolutionGrid]

        self.NumberOfPlayerFlips = self.NumberOfComputerFlips

        for i in range(len(self.EntityImages)):
            if i <= self.NumberOfPlayerFlips: self.EntityImages[i][0] = "move_on"
            else: self.EntityImages[i][0] = "move_off"

        for entity in entity_handler.EntityList:
            if entity.EntityType == 0:
                entity.EntityVisible = False
                if self.SolutionGrid[entity.PowerX][entity.PowerY] == 1: entity.EntityImageSource = "light_on"
                else: entity.EntityImageSource = "light_off"

        self.mixPowerGrid(entity_handler)

        self.CanPlayerMove = True

        for entity in entity_handler.EntityList:
            if entity.EntityType == 0:
                entity.EntityVisible = True

        pass

    def mixPowerGrid(self,entity_handler):
        for l in range(self.NumberOfComputerFlips):
            t_x = secrets.randbelow(self.GridWidth)
            t_y = secrets.randbelow(self.GridHeight)
            for entity in entity_handler.EntityList:
                if entity.EntityType == 0:
                    if (entity.PowerX == t_x and entity.PowerY == t_y):
                        entity.initialFlip(entity_handler)
        pass

    def getSolutionGrid(self,choice):

        tmpList = [[1 for i in range(self.GridWidth)] for j in range(self.GridHeight)]

        """
        ==================================
        DEPRECATED

        if choice == 0:
            pass
        elif choice == 1:
            tmpList[0] = [0,0,0,0,0,1,0,0]
            tmpList[1] = [0,1,1,0,0,1,1,0]
            tmpList[2] = [0,1,1,0,0,0,1,0]
            tmpList[3] = [0,0,0,0,0,0,1,0]
            tmpList[4] = [0,0,0,0,0,0,1,0]
            tmpList[5] = [0,1,1,0,0,0,1,0]
            tmpList[6] = [0,1,1,0,0,1,1,0]
            tmpList[7] = [0,0,0,0,0,1,0,0]
        elif choice == 2:
            pass
        elif choice == 3:
            pass
        ==================================
        """
            
        return tmpList

    def checkForSolution(self,entity_handler):
        if (self.PowerGrid == self.SolutionGrid):
            self.CanPlayerMove = False

            for entity in entity_handler.EntityList:
                if entity.EntityType == 0:
                    if entity.EntityImageSource == "light_on": entity.EntityImageSource = "correct_on"
                    else: entity.EntityImageSource == "correct_off"

            self.EntityTimers.append([270, self.setupGrid])

    def updateMoveTracker(self,entity_handler):
        self.NumberOfPlayerFlips -= 1
        for i in range(len(self.EntityImages)):
            if i < self.NumberOfPlayerFlips: self.EntityImages[i][0] = "move_on"
            else: self.EntityImages[i][0] = "move_off"
        pass

