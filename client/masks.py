import RPi.GPIO as GPIO
import time

def drop(control_pin):
    #Turn control pins off to release magnet
    GPIO.output(control_pin, False)

    time.sleep(1.0) #Make sure masks release

    #Turn magnet back on
    GPIO.output(control_pin, True)

def cleanup():
    GPIO.cleanup()
