# Plays two sounds simultaneously by spawning separate subprocesses
#
# NOTE: Killing those subprocesses once they are spawned is very difficult
# so any sounds / video that get played will play their entire length

import os
import subprocess

f1 = os.getcwd() + '/terror.mp3'
f2 = os.getcwd() + '/walking_sound.mp3'

do = subprocess.Popen(['afplay', f1])
re = subprocess.Popen(['afplay', f2])


