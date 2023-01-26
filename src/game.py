'''

Main game file. Includes setup, game variables, and the main loop

'''

#region Imports

import sys, pygame
pygame.init()

import util

from common import states
from common import EntityTypeList

import error

from entities.Entity import Entity

#endregion

#region Setup constants and display

SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 160, 120

SCREEN_X = 0
SCREEN_Y = 0

DISPLAY_SIZE = DISPLAY_WIDTH, DISPLAY_HEIGHT = 960, 720

DISPLAY_SCALE = DISPLAY_WIDTH / SCREEN_WIDTH

DISPLAY_BLACK = 0, 0, 0
DISPLAY_GREY = 50, 50, 50

window = pygame.display.set_mode(DISPLAY_SIZE, pygame.RESIZABLE)

screen = window.subsurface(0,0,window.get_width(),window.get_height())

pygame.display.set_caption("")

pygame.mouse.set_visible(False)

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
addImageSource("mouse")
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

    try:
        entity.onCreated(EntityList,Game)
    except:
        error.causeError("Creating Entity Error: "+entity.EntityName,"There was a problem in the onCreated function of this entity")

def destroyEntity(entity_id):
    for i in EntityList:
        if (i.EntityID == entity_id or i.EntityName == entity_id or i.EntityType == entity_id):
            print("destroyed "+i.EntityName)
            EntityList.remove(i)
            try:
                i.onDestroyed(EntityList,Game)
            except:
                error.causeError("Destroying Entity Error: "+i.EntityName,"There was a problem in the onDestroyed function of this entity") 

def getEntityByID(entity_id):
    for i in EntityList:
        if (i.EntityID == entity_id): return EntityList.i

#endregion

#endregion




createEntity(EntityTypeList.Player,"Player",(16,16,8,8),"player")




#region Render

def render():

    window.fill(DISPLAY_GREY)
    screen.fill(DISPLAY_BLACK)

    for i in EntityList:
        if (i.EntityVisible == True and i.EntityImageSource != ""):
            tmp_rect = i.EntityRect
            tmp_img = pygame.transform.scale_by(getImageSource(i.EntityImageSource).ImageLoad,DISPLAY_SCALE)
            tmp_imgrect = getImageSourceRect(i.EntityImageSource)
            screen.blit(tmp_img,((tmp_rect.centerx-tmp_imgrect.width/2)*DISPLAY_SCALE,(tmp_rect.centery-tmp_imgrect.height/2)*DISPLAY_SCALE,0,0))

    #always render mouse above all entities
    tmp_img = pygame.transform.scale_by(getImageSource("mouse").ImageLoad,DISPLAY_SCALE)
    tmp_imgrect = getImageSourceRect("mouse")
    tmp_pos = pygame.mouse.get_pos()
    tmp_mx = (tmp_pos[0])-SCREEN_X
    tmp_my = (tmp_pos[1])-SCREEN_Y
    tmp_mx = util.clamp(tmp_mx,0,screen.get_width())
    tmp_my = util.clamp(tmp_my,0,screen.get_height())
    screen.blit(tmp_img,(tmp_mx-tmp_imgrect.width/2*DISPLAY_SCALE,tmp_my-tmp_imgrect.height/2*DISPLAY_SCALE,0,0))

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

InputList = []

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        if event.type == pygame.WINDOWRESIZED:
            flag = True
            tmp_width = 1.6
            tmp_height = 1.2
            while flag:
                if (flag and tmp_width < pygame.display.get_window_size()[0]-1.6): tmp_width += 1.6
                else: flag = False
                if (flag and tmp_height <pygame.display.get_window_size()[1]-1.2): tmp_height += 1.2
                else: flag = False

            tmp_x = (pygame.display.get_window_size()[0]-tmp_width)/2
            tmp_y = (pygame.display.get_window_size()[1]-tmp_height)/2

            screen = window.subsurface((tmp_x,tmp_y,tmp_width,tmp_height))

            DISPLAY_SCALE = tmp_width / SCREEN_WIDTH

            SCREEN_X = tmp_x
            SCREEN_Y = tmp_y

            #pygame.transform.scale(screen,pygame.display.get_window_size())
            print("x: "+str(tmp_x)+", y: "+str(tmp_y))

        InputList.append(event)

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                print("hello")
                destroyEntity("Player")

    update_all_entities(pygame.event.get())

    InputList = []

    render()

#endregion
