"""

Main application file. Includes setup, application variables, and the main loop

"""

#region Imports

import sys 
import pygame
pygame.init()

import error

error.addToActionLog("Setup application")

import util

from common import states
from entities.EntityList import EntityTypeList

from entities.Entity import Entity

from entities.EntityHandler import EntityHandler

import render

import sound

#endregion



#region Setup constants and display

SCREEN_SIZE = SCREEN_WIDTH, SCREEN_HEIGHT = 160, 120

SCREEN_X = 0
SCREEN_Y = 0

DISPLAY_SIZE = DISPLAY_WIDTH, DISPLAY_HEIGHT = 960, 720

DISPLAY_SCALE = DISPLAY_WIDTH / SCREEN_WIDTH

DISPLAY_BLACK = 0, 0, 0
DISPLAY_GREY = 30, 30, 30

WINDOW_COLOR = DISPLAY_GREY
SCREEN_COLOR = DISPLAY_BLACK

SCREEN_MAX_FPS = 144

window = pygame.display.set_mode(DISPLAY_SIZE, pygame.RESIZABLE)

screen = window.subsurface(0,0,window.get_width(),window.get_height())

pygame.display.set_caption("")

pygame.mouse.set_visible(True)

#endregion

#region Setup game

class MainApp:
    AppState = states.NORMAL

App = MainApp()
"""
The 'app'. Functionally, this does not do much, nor is it some all-encompassing class containing many different files or functions.
This is primarily a carrier for app-wide information, which may be used in many different locations/situations. The easiest example
is the actual app state (if the app is in its normal state, or if it is paused, etc.).
"""

error.addToActionLog("Application setup complete: Begin loading assets")

#endregion


#region Handle images (add images here)

render.addImageSource("light_on")
render.addImageSource("light_off")
render.addImageSource("light_flash")
render.addImageSource("correct_on")
render.addImageSource("correct_off")
render.addImageSource("wrong_on")
render.addImageSource("wrong_off")
render.addImageSource("move_on")
render.addImageSource("move_off")
render.addImageSource("undo_on")
render.addImageSource("undo_off")
render.addImageSource("undo_hover")
render.addImageSource("title_on")
render.addImageSource("title_off")
render.addImageSource("normal_on")
render.addImageSource("normal_off")
render.addImageSource("quit_on")
render.addImageSource("quit_off")
render.addImageSource("quit_hover")
render.addImageSource("score_small")
render.addImageSource("score_medium")
render.addImageSource("score_big")

error.addToActionLog("Loading assets: All images loaded")

pygame.display.set_icon(render.getImageSource("score_big").ImageLoad)

#endregion


#region Handle sounds (add sounds here)

sound.addSoundSource("main_menu","ambientmain_0")

error.addToActionLog("Loading assets: All sounds loaded")

#endregion


#EntityHandler.createEntity(App,EntityTypeList.LightControl,(0,0,0,0),"LightControl","")
EntityHandler.createEntity(App,EntityTypeList.Title,(43,32,88,16),"Title","title_on")
EntityHandler.createEntity(App,EntityTypeList.Normal,(53,64,48,16),"Normal","normal_off")

sound.playSound("main_menu",-1)


#region Render

def render_all():

    try:

        window.fill(WINDOW_COLOR)
        screen.fill(SCREEN_COLOR)

        render.renderEntities(EntityHandler,screen,DISPLAY_SCALE)

        #always render mouse above all entities
        #render.renderMouse("mouse",screen,DISPLAY_SCALE,SCREEN_X,SCREEN_Y)

        pygame.display.flip()

    except:
        error.causeError("Rendering Error","There was an error in the render_all() function")


def resize_screen():
    """
    Resize the screen, based on the new size of the actual window.

    NOTE: This is ONLY to be used in the logic portion of the main loop, ONLY when checking the event list, ONLY when the event
    includes a pygame WINDOWRESIZED event
    """
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
    global App

    global screen
    global DISPLAY_SCALE
    global SCREEN_X
    global SCREEN_Y

    for event in pygame.event.get():
        if event.type == pygame.QUIT: error.exitSafely()

        if event.type == pygame.WINDOWRESIZED:
            resize_screen()

        InputList.append(event)

    tmp_m_coords = util.getApplicationMouseCoords(screen,DISPLAY_SCALE,SCREEN_X,SCREEN_Y)

    EntityHandler.update_all_entities(App,InputList,tmp_m_coords)

    InputList = []

#endregion


#region Main loop

error.addToActionLog("Running application: Beginning main loop")

ApplicationClock = pygame.time.Clock()

while True:

    logic_all()

    render_all()

    ApplicationClock.tick(SCREEN_MAX_FPS)

    pygame.display.set_caption("FPS: "+str(round(ApplicationClock.get_fps(),2)))


#endregion
