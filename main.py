#! /usr/bin/env python3

import time
import notecomm
import camera
import config


def main():
    notecomm.init_notecard(config.notehub_productUID,
                           config.NOTECARD_I2C_DEVICE)
    camera.start()
    while True:
        camera.capture('here.jpg')
        notecomm.send_to_notehub('here.jpg', config.TARGET_DEVICE)
        notecomm.get_from_notehub('there.jpg')
        # display.show("there.jpg")
        time.sleep(5)


if __name__ == "__main__":
    main()
