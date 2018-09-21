import sys
sys.path.insert(0,"../")
import json
import config
import boto3
from flask import Flask

app = Flask(__name__)
client = boto3.client('sns')
@app.route('/flicker')
def ficker():
    #push to sns
    action_dict = {"action":"flicker"}
    send_message(json.dumps(action_dict),"action")
    return 'flicker'


def send_message(msg,subject:str):

    client.publish(
            TopicArn = config.sns_arn,
            Message = msg,
            Subject = subject,
            MessageStructure = 'string'
        )
    


