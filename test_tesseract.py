import subprocess
from datetime import datetime
from picamera import PiCamera
import RPi.GPIO as GPIO

# Pictures directory
directory_string = "/home/pi/pictures/"

# Initialize camera
camera = PiCamera()
#camera.resolution = (600, 600)

# Set pin modes for GPIO
led_pin = 24
button_pin = 23

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# LED
GPIO.setup(led_pin,GPIO.OUT)

# BUTTON
GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)


# Function that takes a picture, post-processes it, uses tesseract to convert it to text and converts that to audio using espeak. 
def convert_image_to_audio():
    speak("Capture image")

    # Step 1: Get datetime string
    datetime_string = datetime.today().strftime('%Y-%m-%d-%H%M%S')
    print("Step 1: Datetime string "+datetime_string)

    # Step 2: Turn the LED on
    GPIO.output(led_pin,GPIO.HIGH)
    print("Step 2: LED on")

    # Step 3: Take the picture
    
    # Old method:
    #take_picture = subprocess.run(["raspistill", "-o", output_string, "-w", str(width), "-h", str(height)], "-t", "0", shell=True)
    #take_picture = subprocess.run(["raspistill -o "+output_string+" -w 600 -h 600 -t 0"], shell=True)

    # New method:
    output_string = directory_string + datetime_string + ".jpg"
    camera.capture(output_string)
    print("Step 3: Taken picture " + output_string)

    # Step 4: Turn the LED off
    GPIO.output(led_pin,GPIO.LOW)
    print("Step 4: LED off")

    # Step 5: Post-process the image using imagemagick
    output_string_postprocessed = directory_string + datetime_string + "-postprocessed.jpg"
    subprocess.run(['convert', output_string, '-threshold 50% ', output_string_postprocessed])
    print("Step 5: Post-processed image "+output_string_postprocessed)

    # Step 6: Use Tesseract
    output_string_tesseract = directory_string + datetime_string + "-tesseract"
    subprocess.run(['tesseract', output_string_postprocessed, output_string_tesseract])
    output_string_tesseract = output_string_tesseract+".txt"
    print("Step 6: Performed tesseract conversion "+output_string_tesseract)

    # Step 7: Get string from file
    string_to_speak = ""
    with open(output_string_tesseract, 'r') as file:
        string_to_speak = file.read()
    print("Step 7: Read string to speak from file "+string_to_speak)

    # Step 8: Speak string
    if string_to_speak != "":
        speak("Found text")
        speak(string_to_speak)
    else:
        speak("Didn't find text")
    
    print("Step 8: Spoke string")


# Function that takes an input string and automatically speaks it using espeak and aplay
def speak(input_string):
    # https://www.dexterindustries.com/howto/make-your-raspberry-pi-speak/
    # https://github.com/DexterInd/Raspberry_Pi_Speech/blob/master/speak_text.py
    
    #input_string = re.sub(r'\W+', '', input_string)
    input_string = input_string.replace('\'', '')
    input_string = input_string.replace('"', '')
    input_string = input_string.replace('\n', '_')
    input_string = input_string.replace(' ', '_')
    subprocess.run(['espeak -s 120 --stdout > /home/pi/speak.wav '+input_string], shell=True)
    subprocess.run(["aplay /home/pi/speak.wav"], shell=True)


# Run the main thread
if __name__ == "__main__":
    speak("I have started up")
    while True:
        button_state = GPIO.input(button_pin)
        if button_state == False:
            convert_image_to_audio()