import sys
sys.path.insert(0,"../")
import json
import config
import boto3
from flask import Flask, render_template, request

app = Flask(__name__)
client = boto3.client('sns')

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/flicker', methods=['POST'])
def ficker():
    #push to sns
    action_dict = {"action":"flicker"}
    send_message(json.dumps(action_dict),"action")
    return 'flickered'

@app.route('/clown', methods=['POST'])
def clown():
    #push to sns
    action_dict = {"action":"clown"}
    send_message(json.dumps(action_dict),"action")
    return 'clown dropped'

@app.route('/blinds', methods=['POST'])
def blinds():
    #push to sns
    action_dict = {"action":"blinds"}
    send_message(json.dumps(action_dict),"action")
    return 'blinds opened'

@app.route('/shadow', methods=['POST'])
def shadow():
    #push to sns
    action_dict = {"action":"shadow"}
    send_message(json.dumps(action_dict),"action")
    return 'shadow flashed'

@app.route('/fog', methods=['POST'])
def fog():
    #push to sns
    action_dict = {"action":"fog"}
    send_message(json.dumps(action_dict),"action")
    return 'fog released'

@app.route('/coffin', methods=['POST'])
def coffin():
    #push to sns
    action_dict = {"action":"coffin"}
    send_message(json.dumps(action_dict),"action")
    return 'coffin opened'

@app.route('/doll', methods=['POST'])
def doll():
    #push to sns
    action_dict = {"action":"doll"}
    send_message(json.dumps(action_dict),"action")
    return 'doll head turned'

def send_message(msg,subject:str):

    client.publish(
            TopicArn = config.sns_arn,
            Message = msg,
            Subject = subject,
            MessageStructure = 'string'
        )
    


