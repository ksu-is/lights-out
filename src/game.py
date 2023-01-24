'''

Main game file. Includes setup, game variables, and the main loop

'''

#region Imports

import sys, pygame
pygame.init()

import render_helper as rh

from common import states

import entities.Entity

#endregion

#region Setup constants and display

SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 160, 120

DISPLAY_SIZE = DISPLAY_WIDTH, DISPLAY_HEIGHT = 960, 720

DISPLAY_SCALE = DISPLAY_WIDTH / SCREEN_WIDTH

DISPLAY_BLACK = 0, 0, 0

screen = pygame.display.set_mode(DISPLAY_SIZE)

pygame.display.set_caption("")

#endregion

#region Setup game



class MainGame:
    GameState = states.NORMAL

Game = MainGame()

#endregion


#region Load images (add line for every image file)

ImageSourceList = []

#region Load image helpers

class ImageSource:
    ImageID = ""
    ImageLoad = 0

def addImageSource(source_string):
    img = ImageSource()
    img.ImageID = source_string
    img.ImageLoad = pygame.image.load("assets/"+source_string+".gif")
    ImageSourceList.append(img)

def getImageSource(source_string):
    for i in ImageSourceList:
        if (i.ImageID == source_string): return i

    return ""

def getImageSourceRect(source_string):
    for i in ImageSourceList:
        if (i.ImageID == source_string): return i.ImageLoad.get_rect()

    return -1



#endregion

addImageSource("player")
addImageSource("intro_ball")

pygame.display.set_icon(getImageSource("player").ImageLoad)

#endregion

#region Handle entities

#list of all entity types (classes). used as a list of constants to create entities through destroyEntity

class EntityTypes:
    def __init__(self):

        self.Player = 0
        self.Wall = 1
        self.Enemy = 2
        self.Example = 3

    def getNewEntity(self,entity_type):
        match entity_type:

            case self.Player:
                return Entity()

            case self.Wall:
                return Entity()

            case _:
                return Entity()

EntityTypeList = EntityTypes()

EntityIDGenerator = 1000

def generateEntityID():
    global EntityIDGenerator
    EntityIDGenerator += 1
    return EntityIDGenerator

EntityList = []

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

def createEntity(entity_type=-1,entity_name="", entity_rect=(0,0,0,0), entity_image_src=""):
    entity = EntityTypeList.getNewEntity(entity_type)

    entity.EntityID = generateEntityID()

    entity.EntityName = entity_name
    entity.EntityImageSource = entity_image_src
    entity.EntityRect = pygame.Rect(entity_rect)
    EntityList.append(entity)

def destroyEntity(entity_id):
    for i in EntityList:
        if (i.EntityID == entity_id or i.EntityName == entity_id or i.EntityType == entity_id):
            print("destroyed "+i.EntityName)
            EntityList.remove(i)

def getEntityByID(entity_id):
    for i in EntityList:
        if (i.EntityID == entity_id): return EntityList.i

#endregion




createEntity(EntityTypeList.Player,"Player",(16,16,8,8),"player")




#region Render

def render():
    screen.fill(DISPLAY_BLACK)

    for i in EntityList:
        if (i.EntityVisible == True and i.EntityImageSource != ""):
            tmp_rect = i.EntityRect
            tmp_img = pygame.transform.scale_by(getImageSource(i.EntityImageSource).ImageLoad,DISPLAY_SCALE)
            tmp_imgrect = getImageSourceRect(i.EntityImageSource)
            screen.blit(tmp_img,((tmp_rect.centerx-tmp_imgrect.width/2)*DISPLAY_SCALE,(tmp_rect.centery-tmp_imgrect.height/2)*DISPLAY_SCALE,0,0))

    pygame.display.flip()


#endregion

#region Logic

def update_all_entities(input_list):
    for i in EntityList:
        if ((not i.RestrictUpdate) and Game.GameState in i.UpdateStates):
            if (i.RequiresInputs):
                i.Inputs = input_list
            i.update(EntityList,Game)         

#endregion

#region Main loop

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                print("hello")
                destroyEntity("Player")

    update_all_entities(pygame.event.get())

    render()

#endregion
