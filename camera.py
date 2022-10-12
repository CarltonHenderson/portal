import time

from picamera2 import Picamera2

picam2 = Picamera2()

def start():
    preview_config = picam2.create_preview_configuration(main={"size": (800, 600)})
    picam2.configure(preview_config)
    picam2.start()
    time.sleep(2)


def capture(imageName):
    picam2.capture_file(imageName)

def stop():
    picam2.close()
