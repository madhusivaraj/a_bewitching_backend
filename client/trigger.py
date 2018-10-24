# Triggers audio and visual effects 

import os
import subprocess

#Plays static on tv and static noises on tv/speakers
def tv(video, static): 
        os.system("omxplayer " + video)

def audio(audiofile):
        os.system("omxplayer --vol 800 " + audiofile)
