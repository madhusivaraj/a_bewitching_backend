import os
import sys
import glog as log
import json
sys.path.insert(0, "../")
import config
import boto3

CLIENT_WAIT_TIME=20

# Create SQS client
client = boto3.client('sqs')

def play_sound(path):
        os.system("omxplayer --vol 1000 " + path)
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
            if (action['action'] == 'footsteps'):
                sound_path = "../media/walking_sound.mp3"
                play_sound(sound_path)
                #only delete if we have to
                client.delete_message(
                    QueueUrl=config.sqs_url,
                    ReceiptHandle=receipt_handle
                )
    else:
        #print(response, end="\n\n")
        pass

