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
pygame.mixer.set_num_channels(16)

SoundSourceList = []

ChannelList = []

class ChannelHandler:
    """
    
    """
    def __init__(self,channel_id):
        
        self.channel = pygame.mixer.Channel(channel_id)
        self.soundID = ""
        self.entityOwner = 0
        self.force = False

def initChannelList():
    j = pygame.mixer.get_num_channels()
    for i in range(j):
        ChannelList.append(ChannelHandler(i))

    error.addToActionLog("Added Sound Channels 1-"+str(j))

initChannelList()


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

def addSoundSource(name_string,source_string=""):
    """
    Function used to add new sound sources, or any new sound files required.
    This should be used in the main file only, as imported from render.py\n
    IMPORTANT: the only acceptable file types are .ogg and uncompressed .wav files
    """

    try:

        snd = SoundSource()
        snd.SoundID = name_string
        if (source_string == ""): source_string = name_string

        try:
            snd.SoundLoad = pygame.mixer.Sound("assets/sounds/"+source_string+".ogg")
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

def playSound(sound_name="",number_of_loops=0,entityID=0,force_play=False):
    """
    Will play the sound with the given name, looping with the given number of loops.\n
    NOTE: Use -1 as the number of loops if the sound should loop indefinitely.\n
    IMPORTANT: Anytime an entity is playing a sound (which will likely be most of the time),
    there should always be an entity ID passed as an argument. This allows for stopping
    sounds based on which entity started them.\n
    NOTE: The last argument is whether or not to force the sound to play. If this is
    given as True, then if all audio channels are busy, it will force itself into
    a channel that's already playing a sound. Also, if this is given as True, once
    this sound is playing in a channel, it cannot be overridden, even by another
    sound with force_play given as True.
    """
    try:

        flag = False

        for j in ChannelList:
            if (not j.channel.get_busy()):

                j.SoundID = sound_name
                j.entityOwner = entityID
                j.force = force_play

                j.channel.play(getSoundSource(sound_name).SoundLoad,number_of_loops)

                flag = True

                break

        if (not flag):
            for i in ChannelList:
                if (not j.channel.get_busy() or (force_play and (not j.force))):
                    
                    j.SoundID = sound_name
                    j.entityOwner = entityID
                    j.force = force_play

                    j.channel.play(getSoundSource(sound_name).SoundLoad,number_of_loops)

                    break

    except:
        error.causeError("Playing Sound Error: "+sound_name,"There was a problem playing a sound. Either the source for the sound is broken or not present, or there may be an issue with the handlers in sound.py")

def stopSound(sound_name,remove_all=False,entity_id=""):
    try:
        for j in ChannelList:
            if (j.SoundID == sound_name and (entity_id == "" or j.entityOwner == entity_id)):
                j.channel.stop()

                if (not remove_all): break
    except:
        error.causeError("Stopping Sound Error: "+sound_name,"There was a problem stopping a sound. Perhaps the given sound to stop does not exist, or there may be a different problem, either in the file which called this function, or in sound.py")

def stopAllEntitySounds(entity_id):
    try:
        for j in ChannelList:
            if (j.ownerID == entity_id):
                j.channel.stop()
    except:
        error.causeError("Stopping All of an Entity's Sounds Error: "+entity_id,"There was a problem stopping all of an entity's sounds. There may be a problem with the entity, or there may be a different problem, either in the file which called this function, or in sound.py")
