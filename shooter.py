import time
import os

from picamera2 import Picamera2, Preview

os.chdir('/root/dataset')

images = [i for i in os.listdir(os.getcwd()) if i.lower().startswith('image')]
if images:
    newest = max(images,key=os.path.getmtime)
else:
    newest = 'image0.jpg'

number = int(''.join([i for i in newest if i.isdigit()]))

picam2 = Picamera2()
picam2.start_preview(Preview.QTGL)

preview_config = picam2.create_preview_configuration()
capture_config = picam2.create_still_configuration()
picam2.configure(preview_config)

picam2.start()
time.sleep(2)

picam2.switch_mode_and_capture_file(capture_config, 'test_full'+str(number+1)+'.jpg')