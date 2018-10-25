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

    try:
        action_dict = {"action":"play_static_sounds"}
        send_message(json.dumps(action_dict),"action")
        return jsonify(success=True)
    except:
        return jsonify(success=False)


#Turning off lights 
@app.route('/turn_off_lights', methods=['POST'])
def turn_off_lights():
    try: 
        action_dict = {"action":"turn_off_lights"}
        send_message(json.dumps(action_dict),"action")
        return jsonify(success=True)
    except:
        return jsonify(success=False)

    try: 
        action_dict = {"action":"play_music_box_1"}
        send_message(json.dumps(action_dict),"action")
        return jsonify(success=True)
    except:
        return jsonify(success=False)

    
    try: 
        action_dict = {"action":"play_music_box_2"}
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


@app.route('/doll', methods=['POST'])
def doll():
    try:
        action_dict = {"action":"doll"}
        send_message(json.dumps(action_dict),"action")
        return jsonify(success=True)
    except:
        return jsonify(success=False)

    try:
        action_dict = {"action":"play_child_laughs_2"}
        send_message(json.dumps(action_dict),"action")
        return jsonify(success=True)
    except:
        return jsonify(success=False)

    try:
        action_dict = {"action":"play_child_laughs_2"}
        send_message(json.dumps(action_dict),"action")
        return jsonify(success=True)
    except:
        return jsonify(success=False)

@app.route('/masks', methods=['POST'])
def doll():
    try:
        action_dict = {"action":"drop_masks"}
        send_message(json.dumps(action_dict),"action")
        return jsonify(success=True)
    except:
        return jsonify(success=False)
    
    try:
        action_dict = {"action":"play_whispers"}
        send_message(json.dumps(action_dict),"action")
        return jsonify(success=True)
    except:
        return jsonify(success=False)

    try:
        #Second whispers event for second raspberry pi
        action_dict = {"action":"play_whispers_2"}
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
