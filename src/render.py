"""
The main rendering handler. Contains the most important functions for rendering the display
and all active entities
"""

import pygame
import error
import util

ImageSourceList = []

#region Load image helpers

class ImageSource:
    """
    Class used for image sources.

    NOTE: These sources are not defined in entities. These are the actual image files, given
    an ID (given string as a name) for easy access, and the actual surfaces which will be
    used for rendering.
    """
    ImageID = ""
    ImageLoad = 0
    """
    The actual surface, loaded from the image file, and used for rendering purposes
    """

def addImageSource(source_string):
    """
    Function used to add new image sources, or any new image files required.
    This should be used in the main file only, as imported from render.py
    """

    try:

        img = ImageSource()
        img.ImageID = source_string
        img.ImageLoad = pygame.image.load("assets/images/"+source_string+".gif")
        ImageSourceList.append(img)

    except:
        error.causeError("Loading Image Error: "+source_string,"There was a problem loading an image source file. Check to make sure that all image files are present, with usable file extensions")

def getImageSource(source_string):
    """
    Gets the ImageSource object from the list of image sources,
    based on the given ImageID (which is usually the name of the image)
    NOTE: ImageSources are NOT the actual images. The actual surfaces
    will be contained inside of the ImageLoad attributes of ImageSource
    objects. To retrieve the actual surface, you can call this function,
    getImageSource("example_image_id").ImageLoad
    """
    for i in ImageSourceList:
        if (i.ImageID == source_string): return i

    return ""

def getImageSourceRect(source_string):
    """
    Gets an ImageSource's rect, first finding the ImageSource from
    the list of image sources, then finding the rect of the retrieved
    ImageSource.
    """
    for i in ImageSourceList:
        if (i.ImageID == source_string): return i.ImageLoad.get_rect()

    return -1


def renderEntities(entity_handler,screen,display_scale):
    """
    Render all entities in the EntityList. Should only be called in the render portion
    of the main application loop, and should only be called once.
    """
    for i in entity_handler.EntityList:
        if (i.EntityVisible == True and i.EntityImageSource != ""):
            tmp_rect = i.EntityRect
            tmp_img = pygame.transform.scale_by(getImageSource(i.EntityImageSource).ImageLoad,display_scale)
            tmp_imgrect = getImageSourceRect(i.EntityImageSource)
            screen.blit(tmp_img,((tmp_rect.centerx-tmp_imgrect.width/2)*display_scale,(tmp_rect.centery-tmp_imgrect.height/2)*display_scale,0,0))

def renderMouse(mouse_img,screen,display_scale,screen_x,screen_y):
    """
    Render the mouse with an image, based on the given image name.
    Will also scale appropriately based on the screen + window size.
    """
    tmp_img = pygame.transform.scale_by(getImageSource(mouse_img).ImageLoad,display_scale)
    tmp_imgrect = getImageSourceRect("mouse")
    tmp_pos = pygame.mouse.get_pos()
    tmp_mx = (tmp_pos[0])-screen_x
    tmp_my = (tmp_pos[1])-screen_y
    tmp_mx = util.clamp(tmp_mx,0,screen.get_width())
    tmp_my = util.clamp(tmp_my,0,screen.get_height())
    screen.blit(tmp_img,(tmp_mx-tmp_imgrect.width/2*display_scale,tmp_my-tmp_imgrect.height/2*display_scale,0,0))
    

#endregion

