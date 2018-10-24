import sys
sys.path.insert(0,"../")
import json
import config
import boto3
from flask import Flask, render_template, request, jsonify, url_for
import time

app = Flask(__name__)
client = boto3.client('sns')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/turn_on_tv', methods=['POST'])
def turn_on_tv():
    try:
        action_dict = {"action":"turn_on_tv"}
        send_message(json.dumps(action_dict),"action")
        return jsonify(success=True)
    except:
        return jsonify(success=False)

@app.route('/silhouette_event', methods=['POST'])
def silhouette_event():
    try:
        action_dict = {"action":"silhouette_event"}
        send_message(json.dumps(action_dict),"action")
        return jsonify(success=True)
    except:
        return jsonify(success=False)

@app.route('/sounds', methods=['POST'])
def fog():
    try:    
        print("done")
        action_dict = {"action":"footsteps"}
        send_message(json.dumps(action_dict),"action")
        return jsonify(success=True)
    except:
        return jsonify(success=False)

@app.route('/coffin', methods=['POST'])
def coffin():
    try:
        action_dict = {"action":"coffin"}
        send_message(json.dumps(action_dict),"action")
        return jsonify(success=True)
    except:
        return jsonify(success=False)

@app.route('/doll', methods=['POST'])
def doll():
    try:
        action_dict = {"action":"doll"}
        send_message(json.dumps(action_dict),"action")
        return jsonify(success=True)
    except:
        return jsonify(success=False)

@app.route('/tv', methods=['POST'])
def tv():
    try:
        action_dict = {"action":"tv"}
        send_message(json.dumps(action_dict),"action")
        return jsonify(success=True)
    except:
        return jsonify(success=False)

def send_message(msg,subject:str):
  print("hello?")
  a =  client.publish(
            TopicArn = config.sns_arn,
            Message = msg,
            Subject = subject,
            MessageStructure = 'string'
        )
  print(a)

if __name__ == '__main__':
    app.run(debug=True)
