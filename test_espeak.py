import subprocess

string_to_speak = "Welcome to the new things here, it is awesome isn't it?"





def speak(input_string):
    subprocess.run(["espeak 'Dit is stom' --stdout > /home/pi/speak.wav"], shell=True)
    subprocess.run(["aplay /home/pi/speak.wav"], shell=True)

speak(string_to_speak)