# Plays two sounds simultaneously by spawning separate subprocesses
#
# NOTE: Killing those subprocesses once they are spawned is very difficult
# so any sounds / video that get played will play their entire length

import os
import time
import subprocess

f1 = 'static.mp4'
f2 =  'static_sound.mp3'


do = subprocess.Popen(['omxplayer', '-b', f1, '&'])
re = subprocess.Popen(['omxplayer',  '-o',  'local', f2, '&'])

time.sleep(10)

do.kill()
re.kill()
