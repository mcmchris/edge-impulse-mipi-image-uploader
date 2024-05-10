import time
import os
import keyboard

from picamera2 import Picamera2, Preview

os.chdir('/root/edge-impulse-mipi-image-uploader/dataset')

images = [i for i in os.listdir(os.getcwd()) if i.lower().startswith('image')]
if images:
    newest = max(images, key=os.path.getmtime)
else:
    newest = 'image0.jpg'

number = int(''.join([i for i in newest if i.isdigit()]))

picam2 = Picamera2()
picam2.start_preview(Preview.DRM, x=0, y=0, width=1080, height=1080)

preview_config = picam2.create_preview_configuration()
#capture_config = picam2.create_still_configuration()
picam2.still_configuration.size = (224, 224)
picam2.configure(preview_config)

picam2.start()
#time.sleep(2)

while(True):
    print("Press [s] to take a picture...")
    key = keyboard.wait()
    if(key == "s"):  
        print("Picture taken")
        picam2.switch_mode_and_capture_file("still", 'image'+str(number+1)+'.jpg')
    else:
        print("Wrong key pressed")

