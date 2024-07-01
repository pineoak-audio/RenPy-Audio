############################################################################################################
##                                                                                                        ##
##                              ╔═╗╦ ╦╔╦╗╦╔═╗  ╔╦╗╔═╗╔╗╔╔═╗╔═╗╔═╗╦═╗                                      ##
##                              ╠═╣║ ║ ║║║║ ║  ║║║╠═╣║║║╠═╣║ ╦║╣ ╠╦╝                                      ##
##                              ╩ ╩╚═╝═╩╝╩╚═╝  ╩ ╩╩ ╩╝╚╝╩ ╩╚═╝╚═╝╩╚═                                      ##
##                                                                                                        ##
##                       This file contains scripts intended to manage audio.                             ##
##                                                                                                        ##
############################################################################################################

## TABLE OF CONTENTS
##
## 1. DEFINITIONS
##    1.1. General Settings, Title, and Test Effects
##    1.2. Music, Ambiance, Sound Effects, and UI
##         1.2.1. Music
##         1.2.2. Ambiance
##         1.2.3. Sound Effects
##         1.2.4. UI - Interface Interaction Sounds  
##
## 2. MIXERS & CHANNELS
##    2.1. Registry - Channel: SFX & Environment
##    2.2. Registry - Channel: SFX & Environment
##    2.3. Registry - Channel: SFX & Environment


# (!) TODO ----------------------------------------------------------------------------------------------

# TODO [ ] Create a mixer for UI using "renpy.music.alias_channel(3, 'ui')" on line 25
#          of the script renpy\common\00mixers.rpy, located in the engine folder.

# TODO [ ] Delete
#

# TODO [ ] Create a mixer for UI using "renpy.music.alias_channel(3, 'ui')" on line 25
#          of the script renpy\common\00mixers.rpy, located in the engine folder.


## 1. DEFINITIONS ############################################################################################
##
## Reference: https://www.renpy.org/doc/html/python.html

## 1.1. DEFINITIONS - General Settings, Title, and Test Effects ----------------------------------------------

## These five variables control, among other things, which mixers are shown to the player by 
## default. Setting one of them to False will hide the appropriate mixer.


define config.has_sound = True
define config.has_music = True
define config.has_ui    = True
define config.has_voice = False # Foi desativado por não ser usado

## To allow the user to play a test sound on the sound or voice channel,
## uncomment a line below and use it to set a sample sound for playback.

# define config.sample_sound = "sound.ogg"
# define config.sample_voice = "voice.ogg"

## Uncomment the following line to set an audio file that will play while
## the player is in the main menu. This file will continue playing during the
## game until it is stopped or another file is played.

define config.main_menu_music = "audio/mus/halloween.ogg"

## 1.2. DEFINITIONS - Music, Ambiance, Sound Effects, and UI -----------------------------------------------

## 1.2.1. Music
define audio.mus_city =       "audio/mus/01/00_city.ogg"
define audio.mus_house =      "audio/mus/02/00_house.ogg"
define audio.mus_club =       "audio/mus/03/00_club.ogg"

## 1.2.2. Ambiance
define audio.env_birds =      "audio/env/birds.ogg"
define audio.env_rain =       "audio/env/rain.ogg"
define audio.env_talk =       "audio/env/talk.ogg"

## 1.2.3. Sound Effects
define audio.sfx_shot =       "audio/sfx/gunshot.ogg"
define audio.sfx_thunder =    "audio/sfx/thunder.ogg"
define audio.sfx_door =       "audio/sfx/door.ogg"

## 1.2.4. UI - Interface Interaction Sounds. Use "activate_sound ui.b_click" on buttons 
define audio.ui_click =       "audio/ui/btn_click.ogg"
define audio.ui_hover =       "audio/ui/btn_hover.ogg"
define audio.ui_pressed =     "audio/ui/btn_pressed.ogg"
define audio.ui_return =      "audio/ui/btn_return.ogg"
define audio.ui_pages =       "audio/ui/btn_pages.ogg"
define audio.ui_choice =      "audio/ui/btn_choice.ogg"
define audio.ui_save =        "audio/ui/btn_save.ogg"
define audio.ui_load =        "audio/ui/btn_load.ogg"

## 2. MIXERS & CHANNELS #####################################################################################
## https://www.renpy.org/doc/html/audio.html?highlight=register_channel#renpy.music.register_channel
##
## MIXERS:  Mixers are known as Voltage Controlled Amplifiers (VCAs), which are responsible 
##          for controlling the overall volume of a subgroup of faders we call Channels. To
##          register, use the renpy.music.alias_channel() method in the 
##          renpy\common\00mixers.rpy file located in the engine folder. 
##
## CHANNELS:  Channels are subgroups and play only one audio at a time. They are linked to Mixers (VCAs)
##            and can be registered using the renpy.music.register_channel() method.

init python:

    ## 2.1. Registry - Channel: SFX & Environment
    renpy.music.register_channel("sfx01", "sfx", loop=False)
    renpy.music.register_channel("sfx02", "sfx", loop=False)
    renpy.music.register_channel("env01", "sfx", tight=True, loop=True)
    renpy.music.register_channel("env02", "sfx", tight=True, loop=True)
    renpy.music.register_channel("env03", "sfx", tight=True, loop=True)
    renpy.music.register_channel("env04", "sfx", tight=True, loop=True)
    
    ## 2.2. Registry - Channel: Music
    renpy.music.register_channel("patA", "music", tight=True, loop=True)
    renpy.music.register_channel("patB", "music", tight=True, loop=True)
    renpy.music.register_channel("drum", "music", tight=True, loop=True)
    renpy.music.register_channel("bass", "music", tight=True, loop=True)
    
    ## 2.3. Registry - Channel: UI
    renpy.music.register_channel("ui","ui")
    
