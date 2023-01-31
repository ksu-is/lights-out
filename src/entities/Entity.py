'''
The base entity class.
\n Most likely, every entity in the game will be inherited from this file and its children.
\nThis will probably not be used to create actual game entities.
'''

import pygame
import util
from common import states
import error

class Entity:
    '''
    The highest level Entity class. All entities will be either instances of this class or (more likely) instances
    of its children classes. Contains basic entity functionality, including basic rendering, updating, creating,
    and destroying
    '''
    def __init__(self):
        try:
            self.EntityID = 0
            self.EntityType = -1
            self.EntityName = ""
            self.EntityImageSource = ""

            self.EntityRect = pygame.Rect(0,0,0,0)

            self.EntityVisible = True

            self.RestrictUpdate = False
            self.UpdateStates = [states.NORMAL]

            self.RequiresInputs = True #eventually replace this with false, Player and UI elements will likely be the only entities which need inputs

            self.Inputs = []
        except:
            error.causeError("Entity Initializing Error","There was an error in the __init__ function for an entity. This means it happened BEFORE finishing either the createEntity or onCreated functions")

    def onCreated(self,entity_handler,game):
        '''
        An entity's creation function.
        This function will only be run once, when the entity is created,
        and it will ONLY run when the entity is created through the
        createEntity method. Useful for initial actions for entities and
        behaviour that should be run immediately for the entity, but
        that don't make sense to include in __init__
        '''
        pass

    def onDestroyed(self,entity_handler,game):
        '''
        An entity's destruction function.
        This function will only be run once, when the entity is destroyed,
        and it will ONLY run when the entity is destroyed through the
        destroyEntity function. Useful for wrapping up entity logic, or
        handling events which should happen when an entity is destroyed,
        without including it in all the possible behaviours which might
        be used to destroy entities. Also prevents from having to include
        this type of functionality in each entity's onUpdate event.
        '''
        pass

    def onUpdate(self,entity_handler,game):
        '''
        An entity's update function.
        Every time the main loop is run, all entities in the
        EntityList are checked to see if their own update
        function should run. If yes, then run the function.
        '''
        
        for event in self.Inputs:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    entity_handler.destroyEntity(game,"Player")
        pass

