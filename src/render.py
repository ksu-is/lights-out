'''
The main rendering handler. Contains the most important functions for rendering the display
and all active entities
'''

import pygame
import error

ImageSourceList = []

#region Load image helpers

class ImageSource:
    '''
    Class used for image sources.

    NOTE: These sources are not defined in entities. These are the actual image files, given
    an ID (given string as a name) for easy access, and the actual surfaces which will be
    used for rendering.
    '''
    ImageID = ""
    ImageLoad = 0
    '''
    The actual surface, loaded from the image file, and used for rendering purposes
    '''

def addImageSource(source_string):
    '''
    Function used to add new image sources, or any new image files required. This should be used in the main file only.
    '''

    try:

        img = ImageSource()
        img.ImageID = source_string
        img.ImageLoad = pygame.image.load("assets/"+source_string+".gif")
        ImageSourceList.append(img)

    except:
        error.causeError("Loading Image Error: "+source_string,"There was a problem loading an image source file. Check to make sure that all image files are present, with usable file extensions")

def getImageSource(source_string):
    for i in ImageSourceList:
        if (i.ImageID == source_string): return i

    return ""

def getImageSourceRect(source_string):
    for i in ImageSourceList:
        if (i.ImageID == source_string): return i.ImageLoad.get_rect()

    return -1


def renderEntities(entity_handler,screen,display_scale):
    for i in entity_handler.EntityList:
        if (i.EntityVisible == True and i.EntityImageSource != ""):
            tmp_rect = i.EntityRect
            tmp_img = pygame.transform.scale_by(getImageSource(i.EntityImageSource).ImageLoad,display_scale)
            tmp_imgrect = getImageSourceRect(i.EntityImageSource)
            screen.blit(tmp_img,((tmp_rect.centerx-tmp_imgrect.width/2)*display_scale,(tmp_rect.centery-tmp_imgrect.height/2)*display_scale,0,0))


#endregion

