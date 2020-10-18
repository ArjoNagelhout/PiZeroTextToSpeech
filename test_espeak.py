import subprocess

string_to_speak = "Welcome to the new things here, it is awesome isn't it?"

#cmd_beg= 'espeak '
#cmd_end= 'aplay /home/pi/Text.wav' # To play back the stored .wav file and to d$
#cmd_out= '--stdout > /home/pi/Text.wav ' # To store the voice file

#text = input("Enter the Text: ")
#print(text)

#Replacing ' ' with '_' to identify words in the text entered
#text = text.replace(' ', '_')

#Calls the Espeak TTS Engine to read aloud a Text



def speak(input_string):
    subprocess.run(["espeak --stdout > /home/pi/speak.wav "+input_string], shell=True)
    subprocess.run(["aplay /home/pi/speak.wav"], shell=True)

speak(string_to_speak)