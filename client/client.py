import os
import boto3

sns = boto3.resource('sns')
subscription = sns.Subscription('arn')
