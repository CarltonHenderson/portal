#! /usr/bin/env python3

import notecomm
import camera
import time
import config

def main():
    notecomm.init_notecard()
    camera.start()
    while True:
        camera.capture('here.jpg')
        notecomm.send_to_notehub('here.jpg', config.target_device)
        notecomm.get_from_notehub('there.jpg')
        #display.show("there.jpg")
        time.sleep(5)
    camera.stop()



if __name__ == "__main__":
    main()