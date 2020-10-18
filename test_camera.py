import subprocess

width = 600
height = 600

take_picture = subprocess.run(["raspistill", "-o", "/home/pi/pictures/image.jpg", "-w", str(width), "-h", str(height), "-t", "0"])
print(take_picture.returncode)