#################################
# RSP: IP
#
# Sits in control box in chandelier
# Controls lights on and off
# Controls Solenoid release 
##############################

import os
import sys
import glog as log
sys.path.insert(0, "../")
import config
import boto3
import RPi.GPIO as GPIO
import time
import lights

CLIENT_WAIT_TIME=20

light_control_pin_1 = 32
light_control_pin_2 = 36
mask_control_pin = 23

GPIO.setmode(GPIO.BOARD)
GPIO.setup([control_pin_1, control_pin_2],GPIO.OUT)

# Create SQS client
client = boto3.client('sqs')

while(True):
    response = client.receive_message(
        QueueUrl=config.sqs_url,
        AttributeNames=[
            'SentTimestamp'
        ],
        MaxNumberOfMessages=1,
        MessageAttributeNames=[
            'All'
        ],
        WaitTimeSeconds=CLIENT_WAIT_TIME
    )
    
    #Actions to listen for:
    #   1) Lights Off
    #   2) Drop masks
    if 'Messages' in response:
        message = response['Messages'][0]
        body = message['Body']
        receipt_handle = message['ReceiptHandle']
        
        data = json.loads(body)

        action = json.loads(data['Message'])

        if 'action' in action:
            if action['action'] == 'turn_off_lights':
                lights.all_off(light_control_pin_1, light_control_pin_2)
                time.sleep(10)
                lights.all_on(light_control_pin_1, light_control_pin_2)

                client.delete_message(
                    QueueUrl=config.sqs_url,
                    ReceiptHandle=receipt_handle
                )

            if action['action'] == 'drop_masks':
                masks.drop(mask_control_pin)

                client.delete_message(
                    QueueUrl=config.sqs_url,
                    ReceiptHandle=receipt_handle
                )

    else:
#        print(response, end="\n\n")
         pass
