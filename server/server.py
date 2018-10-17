import sys
sys.path.insert(0,"../")
import json
import config
import boto3
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
client = boto3.client('sns')

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/flicker', methods=['POST'])
def flicker():
    try:
        action_dict = {"action":"flicker"}
        send_message(json.dumps(action_dict),"action")
        return jsonify(success=True)
    except:
        return jsonify(success=False)

@app.route('/clown', methods=['POST'])
def clown():
    try:
        action_dict = {"action":"clown"}
        send_message(json.dumps(action_dict),"action")
        return jsonify(success=True)
    except:
        return jsonify(success=False)

@app.route('/blinds', methods=['POST'])
def blinds():
    action_dict = {"action":"blinds"}
    send_message(json.dumps(action_dict),"action")
    return 'blinds opexned'

@app.route('/shadow', methods=['POST'])
def shadow():
    action_dict = {"action":"shadow"}
    send_message(json.dumps(action_dict),"action")
    return 'shadow flashed'

@app.route('/fog', methods=['POST'])
def fog():
    action_dict = {"action":"fog"}
    send_message(json.dumps(action_dict),"action")
    return 'fog released'

@app.route('/coffin', methods=['POST'])
def coffin():
    action_dict = {"action":"coffin"}
    send_message(json.dumps(action_dict),"action")
    return 'coffin opened'

@app.route('/doll', methods=['POST'])
def doll():
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
