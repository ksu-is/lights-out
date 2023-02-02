"""
Handle the sound mixer, as well as sound handling. Should have very few imports or connections with
other systems, so as to allow using this file's functionality in many different places (Examples: entities,
main game loop, other unique files/class instances, etc.)\n
NOTE: Much of the functionality of this file is very similar to the functionality found in render.py. 
While the end results are different (rendering images vs. playing sounds + music), the actual loading and
handling of assets is largely the same between the two.
"""

import pygame
import util
import error

pygame.mixer.init()

SoundSourceList = []

class SoundSource:
    """
    Class used for sound sources.

    NOTE: These sources are not defined in entities. These are the actual sound files, given
    an ID (given string as a name) for easy access, and the actual sounds which will be played.
    """
    SoundID = ""
    SoundLoad = 0
    """
    The actual sound, loaded from the sound file, and used for mixing purposes
    """

def addSoundSource(source_string):
    """
    Function used to add new sound sources, or any new sound files required.
    This should be used in the main file only, as imported from render.py\n
    IMPORTANT: the only acceptable file types are .ogg and uncompressed .wav files
    """

    try:

        snd = SoundSource()
        snd.SoundID = source_string
        try:
            snd.SoundLoad = pygame.mixer.Sound("assets/"+source_string+".ogg")
        except:
            snd.SoundLoad = pygame.mixer.Sound("assets/sounds/"+source_string+".wav")
        SoundSourceList.append(snd)

    except:
        error.causeError("Loading Sound Error: "+source_string,"There was a problem loading a sound source file. Check to make sure that all sound files are present, with usable file extensions")

def getSoundSource(source_string):
    """
    Gets the SoundSource object from the list of sound sources,
    based on the given SoundID (which is usually the name of the sound)
    NOTE: SoundSources are NOT the actual sounds. The actual sounds
    will be contained inside of the SoundLoad attributes of SoundSource
    objects. To retrieve the actual sound, you can call this function,
    getSoundSource("example_sound_id").SoundLoad
    """
    for i in SoundSourceList:
        if (i.SoundID == source_string): return i

    return ""

def playSound(sound_name="",number_of_loops=0):
    """
    Will play the sound with the given name, looping with the given number of loops.
    NOTE: Use -1 as the number of loops if the sound should loop indefinitely.
    """
    try:
        getSoundSource(sound_name).SoundLoad.play(number_of_loops)
    except:
        error.causeError("Playing Sound Error: "+sound_name,"There was a problem playing a sound. Either the source for the sound is broken or not present, or there may be an issue with the handlers in sound.py")
