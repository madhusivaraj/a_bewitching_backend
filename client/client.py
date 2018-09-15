import os
import sys
sys.path.insert(0, "../")
import config
import boto3

client = boto3.client(
    'sns', 
    region_name=config.aws_default_region,
    aws_access_key_id=config.aws_access_key_id,
    aws_secret_access_key=config.aws_secret_access_key
)

client.subscribe(
    TopicArn=config.sns_arn,
    Protocol='sqs',
    Endpoint=config.sqs_arn
)
