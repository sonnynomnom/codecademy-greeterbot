from time import sleep
import datetime

# Import Raspberry Pi GPIO library
import RPi.GPIO as GPIO
import os, sys
import pygame
import random

player = pygame.mixer
player.init()

audio_path = 'audio-files/'
audio_files = os.listdir(audio_path)

GPIO.setmode(GPIO.BCM)
pir_sensor = 4
led = 17

GPIO.setup(pir_sensor, GPIO.IN)
GPIO.setup(led, GPIO.OUT)

# print "The current local date time is ", datetime.datetime.now()

MyDateTime = datetime.datetime.now()

print("Day of month :")
print(MyDateTime.day)
print("Month :")
print(MyDateTime.month)
print("Year  :")
print(MyDateTime.year)
print("Hour  :")
print(MyDateTime.hour)

print("Initialzing PIR Sensor......")
sleep(3)

print("Starting")

GPIO.output(led, False)

try:
    sleep(2) # stabilize sensor
    while True:
        
        if ((MyDateTime.weekday() != 6 or MyDateTime.weekday() != 7) and (MyDateTime.hour >= 8 and MyDateTime.hour <= 10)):
            
            sleep(1)
            current_state = GPIO.input(pir_sensor)
            
            if current_state:
            
                file = random.choice(audio_files)
            
                if "mp3" in file:
                    path = "audio-files/{}".format(file)
                    player.music.load(path)
                    player.music.play()
                    while player.music.get_busy() == True:
                        continue
                print('motion detected!')
                GPIO.output(led, True)
                sleep(5) # led turns on for .5 sec
                GPIO.output(led, False)
            
                sleep(5) # to avoid multiple detections
            sleep(0.1) # loop, delay
            
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
