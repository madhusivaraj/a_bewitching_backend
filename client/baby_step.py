import RPi.GPIO as GPIO

import time
"""
 baby_step_dirs is a list of tuples of (step_pin,dir_pin)
"""
def stepBabies(baby_step_dirs,no_steps):
    for i in baby_step_dirs:
        GPIO.output(i[1],True)
    for i in range(no_steps):
        for j in baby_step_dirs:
            GPIO.output(j[0],True)
            time.sleep(0.001)
            GPIO.output(j[0],False)
    for i in baby_step_dirs:
        GPIO.output(i[1],False)
    for i in range(no_steps):
        for j in baby_step_dirs:
            GPIO.output(j[0],True)
            time.sleep(0.001)
            GPIO.output(j[0],False)
    
