'''

This is a game in python.

'''

#region Imports

import sys, pygame
pygame.init()

import render_helper as rh

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
    GameState = "begin"

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

#endregion

addImageSource("player")
addImageSource("intro_ball")

pygame.display.set_icon(getImageSource("player").ImageLoad)

#endregion

#region Handle entities

#list of all entity types (classes). used as a list of constants to create entities through destroyEntity

class EntityTypes:
    def __init__(self):
        Player = 0
        Wall = 1
        Enemy = 2
        Example = 3

entities = EntityTypes()




EntityIDGenerator = 1000

def generateEntityID():
    global EntityIDGenerator
    EntityIDGenerator += 1
    return EntityIDGenerator

EntityList = []

class Entity:
    def __init__(self):
            self.EntityID = 0
            self.EntityName = ""
            self.EntityImageSource = ""

            self.EntityRect = pygame.Rect(0,0,0,0)

            self.EntityVisible = True


def createEntity(entity_name, entity_rect=(0,0,0,0), entity_image_src=""):
    entity = Entity()

    entity.EntityID = generateEntityID()

    entity.EntityName = entity_name
    entity.EntityImageSource = entity_image_src
    entity.EntityRect = pygame.Rect(entity_rect)
    EntityList.append(entity)

def destroyEntity(entity_id):
    for i in EntityList:
        if (i.EntityID == entity_id or i.EntityName == entity_id):
            print("destroyed "+i.EntityName)
            EntityList.remove(i)

def getEntityByID(entity_id):
    for i in EntityList:
        if (i.EntityID == entity_id): return EntityList.i

#endregion

createEntity("Player",(40,16,8,8),"player")

speed = [1, 1]

ball = pygame.image.load("assets/intro_ball.gif")
ballrect = ball.get_rect()

def render():
    screen.fill(DISPLAY_BLACK)

    for i in EntityList:
        if (i.EntityVisible == True and i.EntityImageSource != ""):
            tmp_rect = i.EntityRect
            screen.blit(pygame.transform.scale_by(getImageSource(i.EntityImageSource).ImageLoad,DISPLAY_SCALE),(tmp_rect.left*DISPLAY_SCALE,tmp_rect.top*DISPLAY_SCALE,0,0))

    pygame.display.flip()


#region Main loop

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                print("hello")
                destroyEntity("Player")

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > DISPLAY_WIDTH:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > DISPLAY_HEIGHT:
        speed[1] = -speed[1]

    render()

#endregion
