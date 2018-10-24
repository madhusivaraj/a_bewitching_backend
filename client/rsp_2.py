import RPi.GPIO as GPIO
import time

silhouette_pin = 23 #orange wire

GPIO.setmode(GPIO.BOARD)
GPIO.setup(silhouette_pin, GPIO.OUT)

def silhouette_pin_on():
	GPIO.output(silhouette_pin, True)

def silhouette_pin_off():
	GPIO.output(silhouette_pin, False)
  
