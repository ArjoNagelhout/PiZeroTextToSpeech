import subprocess

string_to_speak = 'Welcome to the new things here, it is awesome isnt it?'





def speak(input_string):
    subprocess.run(['espeak --stdout > /home/pi/speak.wav '+string_to_speak], shell=True)
    subprocess.run(["aplay /home/pi/speak.wav"], shell=True)

speak(string_to_speak)