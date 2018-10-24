import os
import sys
import json
import subprocess 
import time

sys.path.insert(0, "../")
import config

import boto3

import RPi.GPIO as GPIO

CLIENT_WAIT_TIME=20

# Create SQS client
client = boto3.client('sqs')

# Set up rpi functions:
# Orange wire
silhouette_pin = 23 

GPIO.setmode(GPIO.BOARD)
GPIO.setup(silhouette_pin, GPIO.OUT)
# This turns the pins off

silhouette_sound = '../media/footsteps.mp3'

def cleanup():
	GPIO.cleanup()

def silhouette_pin_on():
	GPIO.output(silhouette_pin, True)

def silhouette_pin_off():
	GPIO.output(silhouette_pin, False)

def footsteps_sound():
	subprocess.Popen(['omxplayer', silhouette_sound, '&'])

def silhouette_event():
	footsteps_sound()
	silhouette_pin_on()
	time.sleep(2)
	silhouette_pin_off()


# Code for client!
try:
	while True:
		response = client.receive_message(
			QueueUrl=config.sqs_url,
			AttributeNames=[
				'SentTimestamp'
			],
			MaxNumberOfMessages=1,
			MessageAttributeNames=[
				'All'
			],
			WaitTimeSeconds=CLIENT_WAIT_TIME
		)
		print(response) 
		if 'Messages' in response:
			message = response['Messages'][0]
			body = message['Body']
			receipt_handle = message['ReceiptHandle']
			#print(body, end="\n\n")
			
			data = json.loads(body)
			#print(data)

			action = json.loads(data['Message'])
			if 'action' in action:
				if (action['action'] == 'silhouette_event'):
					silhouette_event()
					
					#only delete if we have to
					client.delete_message(
						QueueUrl=config.sqs_url,
						ReceiptHandle=receipt_handle
					)
		else:
			#print(response, end="\n\n")
			pass

except KeyboardInterrupt:
	cleanup()