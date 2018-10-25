import RPi.GPIO as GPIO
import time


def all_off(control_pin_1, control_pin_2):
    GPIO.output(control_pin_1,False)
    GPIO.output(control_pin_2,False)
    time.sleep(1.0)

def all_on(control_pin_1, control_pin_2):
    GPIO.output(control_pin_1,True)
    GPIO.output(control_pin_2,True)
    time.sleep(1.0)

def first_off(control_pin_1):
    GPIO.output(control_pin_1, False)
    time.sleep(1.0)

def first_on(control_pin_1):
    GPIO.output(control_pin_1, True)
    time.sleep(1.0)

def second_off(control_pin_2):
    GPIO.output(control_pin_2, False)
    time.sleep(1.0)

def second_on(control_pin_2):
    GPIO.output(control_pin_2, True)
    time.sleep(1.0)

def cleanup():
    GPIO.cleanup()
