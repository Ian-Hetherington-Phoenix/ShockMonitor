#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import SendEmail

sender = SendEmail.Emailer()

sendTo = 'Ian@phoenixfirebird.co.uk'
emailSubject = "Impact Alert"
emailContent = "An Impact has been detected"

#GPIO SETUP
channel = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

def callback(channel):
        if GPIO.input(channel):
                print ("Movement Detected! - should send email")
                #Sends an email to the "sendTo" address with the specified "emailSubject" as the subject and "emailContent" as the email content.
                sender.sendmail(sendTo, emailSubject, emailContent)  
                
        else:
                print ("Movement Detected !")

GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
GPIO.add_event_callback(channel, callback)  # assign function to GPIO PIN, Run function on change

# infinite loop
while True:
        time.sleep(1)