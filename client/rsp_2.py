import RPi.GPIO as GPIO
import time
import os
import subprocess

silhouette_pin = 23 #orange wire

GPIO.setmode(GPIO.BOARD)
GPIO.setup(silhouette_pin, GPIO.OUT)

silhouette_sound = '../media/footsteps.mp3'


def silhouette_pin_on():
	GPIO.output(silhouette_pin, True)

def silhouette_pin_off():
	GPIO.output(silhouette_pin, False)

def silhouette_event():
	subprocess.Popen(['omxplayer', silhouette_sound, '&'])
	
	silhouette_pin_on()
	time.sleep(2)
	silhouette_pin_off()

def cleanup():
	GPIO.cleanup()

try:
	silhouette_pin_off()
	while True:
		silhouette_event()
		time.sleep(5)
except KeyboardInterrupt:
	cleanup()