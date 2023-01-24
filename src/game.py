'''

Main game file. Includes setup, game variables, and the main loop

'''

#region Imports

import sys, pygame
pygame.init()

from common import states
from common import EntityTypeList

import error

from entities.Entity import Entity

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


#region Handle images (add images here)

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

#region Handle entities (add entities here)

def getNewEntity(entity_type):
    match entity_type:

        case EntityTypeList.Player:
            return Entity()

        case EntityTypeList.Wall:
            return Entity()

        case _:
            return Entity()

#region Handle entity helpers

EntityIDGenerator = 1000

def generateEntityID():
    global EntityIDGenerator
    EntityIDGenerator += 1
    return EntityIDGenerator

EntityList = []

def createEntity(entity_type=-1,entity_name="", entity_rect=(0,0,0,0), entity_image_src=""):
    entity = getNewEntity(entity_type)

    entity.EntityID = generateEntityID()

    entity.EntityName = entity_name
    entity.EntityImageSource = entity_image_src
    entity.EntityRect = pygame.Rect(entity_rect)
    EntityList.append(entity)

    entity.onCreated(EntityList,Game)

def destroyEntity(entity_id):
    for i in EntityList:
        if (i.EntityID == entity_id or i.EntityName == entity_id or i.EntityType == entity_id):
            print("destroyed "+i.EntityName)
            EntityList.remove(i)
            i.onDestroyed(EntityList,Game)

def getEntityByID(entity_id):
    for i in EntityList:
        if (i.EntityID == entity_id): return EntityList.i

#endregion

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
            try:
                i.onUpdate(EntityList,Game)
            except:
                error.causeError("Updating Entity Error: "+i.EntityName,"There was a problem in the onUpdate function of this entity") 
            i.Inputs = []        

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
