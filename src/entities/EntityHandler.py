"""
The Entity Handler class is responsible for handling all entities and entity related functions.
"""

import error
import pygame
import util
import common

from entities.EntityList import EntityTypeList

class EntityHandler:
    """
    The active instance of EntityHandler. This instance is responsible for nearly all entity-
    related functions, that do not belong in the actual entities. Updating entities,
    creating entities, destroying entities, and maintaining, searching, or clearing the
    EntityList will all be handled by this instance.
    """

    def __init__(self):
        self.EntityList = []
        self.EntityIDGenerator = 1000



    def generateEntityID(self):
        """
        Generates a unique ID for every entity created. Starts at 1001, will increment with
        every entity. This is not the same thing as an entity type or name. Both an entity's
        type and name may be shared between many different instances of the same entity class,
        while an entity's ID is unique to that individual instance. Therefore, an entity's ID
        is what should be used when you want a SINGLE specific entity.
        """
        self.EntityIDGenerator += 1
        return self.EntityIDGenerator



    def createEntity(self,game,entity_type=-1,entity_name="", entity_rect=(0,0,0,0), entity_image_src=""):
        """
        Creates an entity with a given type, and has the option to set other default values.
        However, in most cases, the entity type and the entity rect should be the only arguments
        given. Everything else will be set by the entity itself in its class __init__ and
        onCreated functions.
        NOTE: While other functions can be set up to create entities, all of them should use
        this function as their base. This is the ONLY function that should be used to actually
        do the entity creation. This is because this function only handles setting base attributes,
        and more importantly, adding the entity to the EntityList. If entities are created without
        using this function, they will likely not be on the EntityList, and therefore will not
        be rendered or given updates.
        """
        
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
            entity.onCreated(self,game)
        except:
            error.causeError("Creating Entity Error: "+entity.EntityName,"There was a problem in the onCreated function of this entity")



    def destroyEntity(self,game,entity_id):
        """
        Destroys all entities matching the given reference, either entity ID, entity name,
        or entity type. It is important to note, destruction is effectively removing an
        entity from the EntityList, and running its own onDestroyed function.
        NOTE: This function will destroy ALL entities matching the argument given. If an
        entity ID is provided, then only the matching entity will be destroyed. However,
        if a name is given, any entities with that name will be destroyed, and if a type
        is given, then ALL entities of that type will be destroyed
        """
        for i in self.EntityList:
            if (i.EntityID == entity_id or i.EntityName == entity_id or i.EntityType == entity_id):

                self.EntityList.remove(i)
                error.addToActionLog("Destroyed Entity: "+i.EntityName)

                try:
                    i.onDestroyed(self,game)
                except:
                    error.causeError("Destroying Entity Error: "+i.EntityName,"There was a problem in the onDestroyed function of this entity") 



    def getEntityByID(self,entity_id):
        """
        Gets an entity from the EntityList, based on the given entity ID.
        NOTE: The entity ID is not the same as an entity's type or name.
        Entity ID is a generated number, assigned to every entity as it's
        created, and completely unique to each entity.\n
        See generateEntityID() in EntityHandler.py for more information
        """
        for i in self.EntityList:
            if (i.EntityID == entity_id): return self.EntityList.i


    def update_all_entities(self,game,input_list):
        """
        The basis of the logic side of the main application loop. This function
        runs the onUpdate event for every entity in the EntityList (unless their updates
        are restricted or they shouldn't update based on the current state), as well
        as passing the list of active inputs to entities which require user input
        """
        for i in self.EntityList:
            if ((not i.RestrictUpdate) and game.GameState in i.UpdateStates):
                if (i.RequiresInputs):
                    i.Inputs = input_list
                try:
                    i.onUpdate(self,game)
                except:
                    error.causeError("Updating Entity Error: "+i.EntityName,"There was a problem in the onUpdate function of this entity") 
                i.Inputs = []    

EntityHandler = EntityHandler()