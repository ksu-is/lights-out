'''
The Entity Handler class is responsible for handling all entities and entity related functions.
'''

import error
import pygame
import util
import common

from entities.EntityList import EntityTypeList

class EntityHandler:

    def __init__(self):
        self.EntityList = []
        self.EntityIDGenerator = 1000



    def generateEntityID(self):
        self.EntityIDGenerator += 1
        return self.EntityIDGenerator



    def createEntity(self,game,entity_type=-1,entity_name="", entity_rect=(0,0,0,0), entity_image_src=""):
        
        try:

            entity = EntityTypeList.getNewEntity(entity_type)

            entity.EntityID = self.generateEntityID()

            entity.EntityName = entity_name
            entity.EntityImageSource = entity_image_src
            entity.EntityRect = pygame.Rect(entity_rect)

            self.EntityList.append(entity)
            error.addToActionLog("Created Entity: "+entity.EntityName)

        except:
            error.causeError("Creating Entity Error: "+entity.EntityName,"There was a problem in the createEntity function, before getting to the onCreated function")

        try:
            entity.onCreated(self.EntityList,game)
        except:
            error.causeError("Creating Entity Error: "+entity.EntityName,"There was a problem in the onCreated function of this entity")



    def destroyEntity(self,game,entity_id):
        for i in self.EntityList:
            if (i.EntityID == entity_id or i.EntityName == entity_id or i.EntityType == entity_id):

                self.EntityList.remove(i)
                error.addToActionLog("Destroyed Entity: "+i.EntityName)

                try:
                    i.onDestroyed(self.EntityList,game)
                except:
                    error.causeError("Destroying Entity Error: "+i.EntityName,"There was a problem in the onDestroyed function of this entity") 



    def getEntityByID(self,entity_id):
        for i in self.EntityList:
            if (i.EntityID == entity_id): return self.EntityList.i


    def update_all_entities(self,game,input_list):
        for i in self.EntityList:
            if ((not i.RestrictUpdate) and game.GameState in i.UpdateStates):
                if (i.RequiresInputs):
                    i.Inputs = input_list
                try:
                    i.onUpdate(self.EntityList,game)
                except:
                    error.causeError("Updating Entity Error: "+i.EntityName,"There was a problem in the onUpdate function of this entity") 
                i.Inputs = []    

EntityHandler = EntityHandler()