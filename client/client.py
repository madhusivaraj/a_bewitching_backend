import os
import sys
sys.path.insert(0, "../")
import config
import boto3

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
        WaitTimeSeconds=20
    )
    print(response, end="\n\n")
    
    if 'Messages' in response:
        message = response['Messages'][0]
        receipt_handle = message['ReceiptHandle']
        
        client.delete_message(
            QueueUrl=config.sqs_url,
            ReceiptHandle=receipt_handle
        )