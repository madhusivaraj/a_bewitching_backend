import os
import sys
import glog as log
import json
sys.path.insert(0, "../")
import config
import boto3
import trigger
import subprocess
import baby_step
import RPi.GPIO as GPIO

#setup GPIO pins
GPIO.setmode(GPIO.BOARD)
#Step 16 Dir 18 Ground: 14, Step 21 Dir 23 G 25, Step 35 Dir 37 G 39
baby_step_dirs = [(16,18),(21,23),(35,37)]
GPIO.setup(16,GPIO.OUT)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(21,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(35,GPIO.OUT)
GPIO.setup(37,GPIO.OUT) 

CLIENT_WAIT_TIME=20


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
    print(response) 
    if 'Messages' in response:
        message = response['Messages'][0]
        body = message['Body']
        receipt_handle = message['ReceiptHandle']
        #print(body, end="\n\n")
         
        data = json.loads(body)
        #print(data)

        action = json.loads(data["Message"])
        if 'action' in action:
            #Turn on led eyes, move heads and trigger laughs
            if (action['action'] == 'doll'):
                #only delete if we have to
                baby_step.stepBabies(baby_step_dirs,800)
                client.delete_message(
                    QueueUrl=config.sqs_url,
                    ReceiptHandle=receipt_handle
                )

    else:
        #print(response, end="\n\n")
        pass

