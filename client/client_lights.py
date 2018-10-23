import os
import sys
import glog as log
sys.path.insert(0, "../")
import config
import boto3
from gpiozero import LED
led = LED(17)

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
    
    if 'Messages' in response:
        message = response['Messages'][0]
        body = message['Body']
        receipt_handle = message['ReceiptHandle']

        print(body, end="\n\n")
        led.on()
        client.delete_message(
            QueueUrl=config.sqs_url,
            ReceiptHandle=receipt_handle
        )
    else:
        #print(response, end="\n\n")
        pass
