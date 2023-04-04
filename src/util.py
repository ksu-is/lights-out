"""
Helper functions which are not specific to any one section of the program.
Math functions, string manipulation functions, etc.
"""

import pygame

def clamp(value,minimum,maximum):
    """
    Returns the given value clamped between the given minimum and maximum, i.e.,
    if the value is less than the minimum, the minimum will be returned. If the
    value is greater than the maximum, the maximum will be returned. Otherwise,
    the value will be returned.
    """
    return (max(minimum,min(value,maximum)))

def isPointInRect(location,rect):
    """
    Tests if a given point (x,y) is within a given Rect (x, y, width, height).
    Returns either True or False
    """
    return location[0] > rect[0] and location[0] < rect[0] + rect[2] and location[1] > rect[1] and location[1] < rect[1] + rect[3]

def getApplicationMouseCoords(screen,display_scale,screen_x,screen_y):
    """
    Get the mouse position 'on screen', i.e., in terms of the application's own 'x' and 'y' coordinates
    """
    tmp_pos = pygame.mouse.get_pos()
    tmp_mx = (tmp_pos[0])-screen_x
    tmp_my = (tmp_pos[1])-screen_y
    tmp_mx = clamp(tmp_mx,0,screen.get_width())
    tmp_my = clamp(tmp_my,0,screen.get_height())

    return (tmp_mx/display_scale, tmp_my/display_scale)