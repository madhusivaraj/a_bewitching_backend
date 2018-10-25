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

#Welcome should trigger:
# Pi 0: play welcome track
# Pi 2: Play welcome track
# IP: turn on lights
@app.route('/welcome', methods=['POST'])
def welcome():
    try:
        action_dict = {"action":"pi0_welcome"}
        send_message(json.dumps(action_dict),"action")

        return jsonify(success=True)
    except:
        return jsonify(success=False)


#Turn on tv should trigger:
# Pi 0: Turn on static.mp4, play static_sound.mp3
# Pi 2: Play static_sound.mp3
@app.route('/turn_on_tv', methods=['POST'])
def turn_on_tv():
    try:
        action_dict = {"action":"turn_on_tv"}
        send_message(json.dumps(action_dict),"action")

        return jsonify(success=True)
    except:
        return jsonify(success=False)


#Turning off overhead lights should trigger:
# ip: Turn off all lights
# pi 2: play shriek.mp3 
@app.route('/turn_off_lights', methods=['POST'])
def turn_off_lights():
    try: 
        action_dict = {"action":"turn_off_lights"}
        send_message(json.dumps(action_dict),"action")
        
        return jsonify(success=True)
    except:
        return jsonify(success=False)

@app.route('/turn_on_lights', methods=['POST'])
def turn_on_lights():
    try: 
        action_dict = {"action":"turn_on_lights"}
        send_message(json.dumps(action_dict),"action")
        
        return jsonify(success=True)
    except:
        return jsonify(success=False)


#silhouette_event should trigger:
# Pi 2: turn on floodlight
# Pi 0: play creepy_whisper.mp3
@app.route('/silhouette_event', methods=['POST'])
def silhouette_event():
    try:
        action_dict = {"action":"silhouette_event"}
        send_message(json.dumps(action_dict),"action")
        return jsonify(success=True)
        
        
    except:
        return jsonify(success=False)

#Doll event should trigger:
# Pi 1: Rotate baby's head and turn on eyes
# Pi 2: Play child laugh
# Pi 0: Play child laugh
@app.route('/doll', methods=['POST'])
def doll():
    try:
        action_dict = {"action":"doll"}
        send_message(json.dumps(action_dict),"action")
        return jsonify(success=True)
    except:
        return jsonify(success=False)

#Drop masks should trigger:
# IP: release magnets 
# Pi 2: play mutters.mp3
@app.route('/masks', methods=['POST'])
def masks():
    try:
   
        action_dict = {"action":"play_mutters"}
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
