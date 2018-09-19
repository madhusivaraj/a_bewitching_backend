import os
import sys
sys.path.insert(0, "../")
import config
import boto3

CLIENT_WAIT_TIME=20

# Create SQS client
client = client = boto3.client(
    'sqs', 
    region_name=config.aws_default_region,
    aws_access_key_id=config.aws_access_key_id,
    aws_secret_access_key=config.aws_secret_access_key
)

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

        client.delete_message(
            QueueUrl=config.sqs_url,
            ReceiptHandle=receipt_handle
        )
    else:
        print(response, end="\n\n")