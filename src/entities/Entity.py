'''
The base entity class.
\n Most likely, every entity in the game will be inherited from this file and its children.
\nThis will probably not be used to create actual game entities.
'''

import pygame
from common import states

class Entity:
    def __init__(self):
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

    def update(self,entity_list,game):
        '''
        An entity's update function.
        Every time the main loop is run, all entities in the
        EntityList are checked to see if their own update
        function should run. If yes, then run the function.
        '''
        pass

