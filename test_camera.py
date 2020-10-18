import subprocess
from datetime import datetime

width = 600
height = 600

datetime_string = datetime.today().strftime('%Y-%m-%d-%H%M%S')
print(datetime_string)
output_string = "/home/pi/pictures/" + datetime_string + ".jpg"
take_picture = subprocess.run(["raspistill", "-o", output_string, "-w", str(width), "-h", str(height), "-t", "0"])
print("taken picture" + output_string)