import os
import sys
import glog as log
sys.path.insert(0, "../")
import config
import boto3

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
        action = json.dumps(body)
        if (action['action'] == 'footsteps'):
            sound_path = "../media/foootsteps.mp3"
            play_sound(sound_path)
        client.delete_message(
            QueueUrl=config.sqs_url,
            ReceiptHandle=receipt_handle
        )
    else:
        #print(response, end="\n\n")
        pass
def play_sound(path):
        sound_path = "../media/foootsteps.mp3"
        os.system("omxplayer --vol 1000 " + path)

