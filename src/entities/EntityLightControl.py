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

            self.GridWidth = 7  #default 7, maximum 8
            self.GridHeight = 7 #default 7, maximum 8

            # self.SolutionGrid = [[1 for i in range(self.GridWidth)] for j in range(self.GridHeight)]



            self.NumberOfComputerFlips =  7#should be 7

            self.NumberOfPlayerFlips = self.NumberOfComputerFlips

            self.CanPlayerMove = False

            self.EntityTimers = []

            self.EntityImages = []

            self.MaxMoves = self.NumberOfComputerFlips

            '''
            moveSpacing = 10
            moveX = 80-(self.MaxMoves)*moveSpacing/2-1
            moveY = 110

            self.TrackerY = moveY

            moveY += 32

            for u in range(self.MaxMoves):
                if u <= self.NumberOfPlayerFlips: self.EntityImages.append(["move_on",pygame.Rect(moveX+moveSpacing*u,moveY,8,8),True])
                else: self.EntityImages.append(["move_off",pygame.Rect(moveX+moveSpacing*u,moveY,8,8),True])
            '''
            self.MoveTracker = []

            self.TrackerState = 0

            self.Difficulty = 0
            


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

        self.Difficulty = self.EntityRect[0]

        if self.Difficulty == 0:
            self.GridHeight = 7
            self.GridWidth = 7
            self.NumberOfComputerFlips = 7
        elif self.Difficulty == 1:
            self.GridHeight = 5
            self.GridWidth = 5
            self.NumberOfComputerFlips = 4
        elif self.Difficulty == 2:
            self.GridHeight = 6
            self.GridWidth = 6
            self.NumberOfComputerFlips = 5

        #====================

        self.SolutionGrid = self.getSolutionGrid(0)

        print(self.SolutionGrid)

        self.PowerGrid = [row[:] for row in self.SolutionGrid]

        print(self.PowerGrid)

        self.NumberOfPlayerFlips = self.NumberOfComputerFlips

        self.MaxMoves = self.NumberOfComputerFlips

        moveSpacing = 10
        moveX = 80-(self.MaxMoves)*moveSpacing/2-1
        moveY = 110

        self.TrackerY = moveY

        moveY += 32

        for u in range(self.MaxMoves):
            if u <= self.NumberOfPlayerFlips: self.EntityImages.append(["move_on",pygame.Rect(moveX+moveSpacing*u,moveY,8,8),True])
            else: self.EntityImages.append(["move_off",pygame.Rect(moveX+moveSpacing*u,moveY,8,8),True])

        #====================

        spacing = 12

        initial_x = 32
        initial_x = 80-(self.GridWidth*spacing)/2
        initial_y = 16
        initial_y = 60-(self.GridHeight*spacing)/2+4

        tmp_x = initial_x
        tmp_y = initial_y

        for i in range(self.GridWidth):
            for j in range(self.GridHeight):
                tmp_entity = entity_handler.createEntity(app,0,(tmp_x,-16,8,8),"Light","light_on")
                tmp_entity.PowerX = i
                tmp_entity.PowerY = j
                tmp_entity.LightX = tmp_x
                tmp_entity.LightY = tmp_y
                tmp_entity.AnimState = 1
                tmp_entity.AnimDelay = (i+(self.GridWidth-j)*self.GridWidth)*8
                tmp_y += spacing
                if (self.SolutionGrid[i][j] == 0): tmp_entity.EntityImageSource = "light_off"
            tmp_x += spacing
            tmp_y = initial_y

        self.mixPowerGrid(entity_handler)

        entity_handler.createEntity(app,2,(4,110,32,8),"Undo","undo_off")
        entity_handler.createEntity(app,5,(4,4,32,8),"Quit","quit_off")
        entity_handler.createEntity(app,6,(0,0,0,0),"Score","")

        self.CanPlayerMove = True

        self.EntityTimers.append([180,self.letPlayerMove])

        self.TrackerState = 1


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

        image_y = self.EntityImages[0][1][1]

        if self.TrackerState == 0:
            image_y = self.TrackerY
        elif self.TrackerState == 1:
            if image_y > self.TrackerY: image_y -= 1
            else: self.TrackerState = 0
        elif self.TrackerState == 2:
            if image_y < self.TrackerY+32: image_y += 1
            else: self.TrackerState = 3

        for image in self.EntityImages:
            image[1][1] = image_y

        pass

    def setupGrid(self,entity_handler):

        self.SolutionGrid = self.getSolutionGrid(0)

        self.PowerGrid = [row[:] for row in self.SolutionGrid]

        self.NumberOfPlayerFlips = self.NumberOfComputerFlips

        self.MoveTracker = []

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
            sound.playSound("stage_clear")

            for entity in entity_handler.EntityList:
                if entity.EntityType == 0:
                    if entity.EntityImageSource == "light_on": entity.EntityImageSource = "correct_on"
                    else: entity.EntityImageSource == "correct_off"
                if entity.EntityType == 6:
                    entity.addWin(entity_handler)

            self.EntityTimers.append([270, self.setupGrid])
        elif self.NumberOfPlayerFlips == 1:
            sound.playSound("stage_incorrect")
            self.CanPlayerMove = False
            for i_entity in entity_handler.EntityList:
                if i_entity.EntityType == 0:
                    if i_entity.EntityImageSource == "light_on": i_entity.EntityImageSource = "wrong_on"
                    else: i_entity.EntityImageSource == "wrong_off"
            self.EntityTimers.append([180,self.undoMove])
            self.EntityTimers.append([180,self.resetLightImages])

    def updateMoveTracker(self,entity_handler):
        self.NumberOfPlayerFlips -= 1
        for i in range(len(self.EntityImages)):
            if i < self.NumberOfPlayerFlips: self.EntityImages[i][0] = "move_on"
            else: self.EntityImages[i][0] = "move_off"
        pass

    def undoMove(self,entity_handler):

        tmp_tuple = self.MoveTracker.pop()

        for entity in entity_handler.EntityList:
            if entity.EntityType == 0:
                if (entity.PowerX == tmp_tuple[0] and entity.PowerY == tmp_tuple[1]):
                    entity.initialFlip(entity_handler)

        self.NumberOfPlayerFlips += 2
        self.updateMoveTracker(entity_handler)
        self.CanPlayerMove = True

    def resetLightImages(self,entity_handler):
        for entity in entity_handler.EntityList:
            if entity.EntityType == 0:
                if self.PowerGrid[entity.PowerX][entity.PowerY] == 1: entity.EntityImageSource = "light_on"
                else: entity.EntityImageSource = "light_off"

    def letPlayerMove(self,entity_handler):
        self.CanPlayerMove = True

    def quitGame(self,entity_handler):
        for entity in entity_handler.EntityList:
            if entity.EntityType == 0:
                entity.AnimState = 3
                entity.AnimDelay = (entity.PowerX+(self.GridWidth-entity.PowerY)*self.GridWidth)*5
            if entity.EntityType == 2 or entity.EntityType == 5:
                entity.AnimState = 2


        self.EntityTimers.append([300,self.returnToTitle])
        self.EntityTimers.append([1,self.clearAwards])
        self.EntityTimers.append([30,self.clearTrackerAnim])


    def returnToTitle(self,entity_handler):
        entity_handler.destroyEntity("Score")
        entity_handler.destroyEntity(self.EntityID)

        for entity in entity_handler.EntityList:
            if entity.EntityType == 3:
                entity.AnimState = 1
                entity.EntityRect[1] = 32-240
            if entity.EntityType == 4:
                entity.AnimState = 1
                entity.EntityRect[1] = 64-200
                entity.resetImages(entity_handler)
            
        entity_handler.destroyEntity("Award")

    def clearAwards(self,entity_handler):
        for entity in entity_handler.EntityList:
            if entity.EntityType == 7:
                entity.AnimState = 3
                entity.AnimDelay = entity.AwardNumber * 10

    def clearTrackerAnim(self,entity_handler):
        self.TrackerState = 2
        