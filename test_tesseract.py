import subprocess
from datetime import datetime
import RPi.GPIO as GPIO
#import time

width = 600
height = 600

# SET GPIO SETTINGS
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(24,GPIO.OUT)


datetime_string = datetime.today().strftime('%Y-%m-%d-%H%M%S')
print(datetime_string)
output_string = "/home/pi/pictures/" + datetime_string + ".jpg"

#Turn led on
print("LED on")
GPIO.output(24,GPIO.HIGH)

# Take picture
take_picture = subprocess.run(["raspistill", "-o", output_string, "-w", str(width), "-h", str(height)], shell=True)
print("taken picture" + output_string)

# Turn led off
GPIO.output(24,GPIO.LOW)

# Convert picture to right format

# Run tesseract

# Speak converted text
string_to_speak = 'Welcome to the new things here, it is awesome isn\'t it?'


# https://www.dexterindustries.com/howto/make-your-raspberry-pi-speak/
# https://github.com/DexterInd/Raspberry_Pi_Speech/blob/master/speak_text.py


def speak(input_string):
    input_string = input_string.replace('\'', '')
    input_string = input_string.replace('"', '')
    input_string = input_string.replace(' ', '_')
    subprocess.run(['espeak -s 120 --stdout > /home/pi/speak.wav '+input_string], shell=True)
    subprocess.run(["aplay /home/pi/speak.wav"], shell=True)

speak(string_to_speak)