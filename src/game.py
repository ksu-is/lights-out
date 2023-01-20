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

#endregion

addImageSource("player")
addImageSource("intro_ball")

def getImageSource(source_string):
    for i in ImageSourceList:
        if (i.ImageID == source_string): return i

    return ""

#endregion

EntityIDGenerator = 1000

EntityList = []

class Entity:
    EntityID = EntityIDGenerator
    EntityIDGenerator += 1
    EntityName = ""
    EntityImageSource = ""

    EntityRect = pygame.Rect(0,0,0,0)

    EntityVisible = True

def createEntity(entity_name, entity_image_src, entity_rect):
    entity = Entity()
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

createEntity("Player","player",(32,32,8,8))

speed = [1, 1]

ball = pygame.image.load("assets/intro_ball.gif")
ballrect = ball.get_rect()

def render():
    screen.fill(DISPLAY_BLACK)

    for i in EntityList:
        if (i.EntityVisible == True):
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
