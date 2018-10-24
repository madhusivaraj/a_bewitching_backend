import RPi.GPIO as GPIO
import time
import os
import subprocess

silhouette_pin = 23 #orange wire

GPIO.setmode(GPIO.BOARD)
GPIO.setup(silhouette_pin, GPIO.OUT)

def silhouette_pin_on():
	GPIO.output(silhouette_pin, True)

def silhouette_pin_off():
	GPIO.output(silhouette_pin, False)

def silhouette_event():
	silhouette_sound = '../media/footsteps.mp3'
	silhouette_pin_on()
	subprocess.Popen(['omxplayer', silhouette_sound])
	time.sleep(2)
	silhouette_pin_off()
