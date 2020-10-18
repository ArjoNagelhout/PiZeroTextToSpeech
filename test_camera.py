import subprocess

width = 600
height = 600

take_picture = subprocess.run(["raspistill", "-o", "~/pictures/image.jpg", "-w", str(width), "-h", str(height)])
print(take_picture.returncode)