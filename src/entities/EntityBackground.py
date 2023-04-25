"""
The entity background class.
\n Most likely, every entity in the app will be inherited from this file and its children.
\nThis will probably not be used to create actual app entities.
"""

import pygame
import util
from common import states
import error
import sound

class EntityBackground:
    """
    The background Entity class. All entities will be either instances of this class or (more likely) instances
    of its children classes. Contains basic entity functionality, including basic rendering, updating, creating,
    and destroying
    """
    def __init__(self):
        try:
            self.EntityID = 0
            self.EntityType = 8
            self.EntityName = ""
            self.EntityImageSource = ""

            self.FirstTickActive = True

            self.EntityRect = pygame.Rect(0,0,0,0)

            self.EntityVisible = False

            self.EntityDepth = 1001

            self.RestrictUpdate = False
            self.UpdateStates = [states.NORMAL]

            self.RequiresInputs = True #eventually replace this with false, Player and UI elements will likely be the only entities which need inputs

            self.Inputs = []
            self.MouseCoords = (0,0)


            self.AnimMax = 10
            self.AnimDelay = self.AnimMax

            #each entity image will have 3 attributes: image source (string), location (rect), and visible (boolean)
            self.EntityImages = []

            self.EntityImages.append(["background_small",pygame.Rect(0,0,160,120),True])
            self.EntityImages.append(["background_small",pygame.Rect(0,120,160,120),True])

            self.EntityImages.append(["background_small",pygame.Rect(-160,0,160,120),True])
            self.EntityImages.append(["background_small",pygame.Rect(-160,120,160,120),True])

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
        self.EntityVisible = False
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
        if self.AnimDelay > 0: self.AnimDelay -= 1
        else:
            self.AnimDelay = self.AnimMax
            for image in self.EntityImages:
                image[1][1] -= 1
                if image[1][1] <= -120:
                    image[1][1] = 120

                image[1][0] += 1
                if image[1][0] >= 160:
                    image[1][0] = -160

        pass

