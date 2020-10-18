import subprocess

string_to_speak = 'Welcome to the new things here, it is awesome isn\'t it?'





def speak(input_string):
    string_to_speak = string_to_speak.replace('\'', '')
    string_to_speak = string_to_speak.replace('"', '')
    string_to_speak = string_to_speak.replace(' ', '_')
    subprocess.run(['espeak --stdout > /home/pi/speak.wav '+string_to_speak], shell=True)
    subprocess.run(["aplay /home/pi/speak.wav"], shell=True)

speak(string_to_speak)