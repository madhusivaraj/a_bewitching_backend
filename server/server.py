import sys
sys.path.insert(0,"../")
import json
import config
import boto3
from flask import Flask, render_template, request

app = Flask(__name__)
client = boto3.client('sns')

@app.route('/flicker', methdos=['POST'])
def flicker():
    #push to sns
    if request.form['trigger'] == 1:
        action_dict = {"action":"flicker"}
        send_message(json.dumps(action_dict),"action")
        return 'flicker'
    return False


@app.route('/')
def index():
    return render_template('index.html')

def send_message(msg,subject:str):

    client.publish(
            TopicArn = config.sns_arn,
            Message = msg,
            Subject = subject,
            MessageStructure = 'string'
        )
    


