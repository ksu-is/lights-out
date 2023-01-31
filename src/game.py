'''

Main game file. Includes setup, game variables, and the main loop

'''

#region Imports

import sys, pygame
pygame.init()

import util

from common import states
from entities.EntityList import EntityTypeList

import error

from entities.Entity import Entity

from entities.EntityHandler import EntityHandler

import render

#endregion

#region Setup constants and display

SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 160, 120

SCREEN_X = 0
SCREEN_Y = 0

DISPLAY_SIZE = DISPLAY_WIDTH, DISPLAY_HEIGHT = 960, 720

DISPLAY_SCALE = DISPLAY_WIDTH / SCREEN_WIDTH

DISPLAY_BLACK = 0, 0, 0
DISPLAY_GREY = 30, 30, 30

window = pygame.display.set_mode(DISPLAY_SIZE, pygame.RESIZABLE)

screen = window.subsurface(0,0,window.get_width(),window.get_height())

pygame.display.set_caption("")

pygame.mouse.set_visible(False)

#endregion

#region Setup game

class MainGame:
    GameState = states.NORMAL

Game = MainGame()
'''
The 'game'. Functionally, this does not do much, nor is it some all-encompassing class containing many different files or functions.
This is primarily a carrier for game-wide information, which may be used in many different locations/situations. The easiest example
is the actual game state (if the game is in its normal state, or if it is paused, etc.).
'''

#endregion


#region Handle images (add images here)

render.addImageSource("player")
render.addImageSource("mouse")
render.addImageSource("intro_ball")

pygame.display.set_icon(render.getImageSource("player").ImageLoad)

#endregion




EntityHandler.createEntity(Game,EntityTypeList.Player,"Player",(16,16,8,8),"player")




#region Render

def render_all():

    try:

        window.fill(DISPLAY_GREY)
        screen.fill(DISPLAY_BLACK)

        render.renderEntities(EntityHandler,screen,DISPLAY_SCALE)

        #always render mouse above all entities
        tmp_img = pygame.transform.scale_by(render.getImageSource("mouse").ImageLoad,DISPLAY_SCALE)
        tmp_imgrect = render.getImageSourceRect("mouse")
        tmp_pos = pygame.mouse.get_pos()
        tmp_mx = (tmp_pos[0])-SCREEN_X
        tmp_my = (tmp_pos[1])-SCREEN_Y
        tmp_mx = util.clamp(tmp_mx,0,screen.get_width())
        tmp_my = util.clamp(tmp_my,0,screen.get_height())
        screen.blit(tmp_img,(tmp_mx-tmp_imgrect.width/2*DISPLAY_SCALE,tmp_my-tmp_imgrect.height/2*DISPLAY_SCALE,0,0))

        pygame.display.flip()

    except:
        error.causeError("Rendering Error","There was an error in the render() function")


def resize_screen():
    '''
    Resize the screen, based on the new size of the actual window.

    NOTE: This is ONLY to be used in the logic portion of the main loop, ONLY when checking the event list, ONLY when the event
    includes a pygame WINDOWRESIZED event
    '''
    global screen
    global DISPLAY_SCALE
    global SCREEN_WIDTH
    global SCREEN_X
    global SCREEN_Y
    try:
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

    except:
        error.causeError("Screen Resizing Error","There was an error while resizing the screen, during a WINDOWRESIZED event")

#endregion

#region Logic

InputList = []

def logic_all():

    global InputList
    global Game

    for event in pygame.event.get():
        if event.type == pygame.QUIT: error.exitSafely()

        if event.type == pygame.WINDOWRESIZED:
            resize_screen()

        InputList.append(event)

    EntityHandler.update_all_entities(Game,InputList)

    InputList = []

#endregion

#region Main loop

while True:

    logic_all()

    render_all()

#endregion
