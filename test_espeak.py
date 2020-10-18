import subprocess

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