"""Use a cellular/wifi Notecard to send/receive images to/from Notehub.io

init_notecard(...) needs to be run once on startup. Afterward send_to_notehub()
and get_from_notehub() can be called, one at a time, as desired.
"""

import io
import base64

import notecard  # pip3 install note-python
from PIL import Image  # pip3 install Pillow
from periphery import I2C  # pip install python-periphery


CARD = 0  # notecard


def init_notecard(notehub_productuid, i2c_device_file_path):
    """Run once at startup before send_to_notehub() or get_from_notehub()"""
    global CARD

    port = I2C(i2c_device_file_path)
    CARD = notecard.OpenI2C(port, 0, 0)

    req = {'req': 'hub.set'}
    req['product'] = notehub_productuid
    req['mode'] = 'continuous'
    req['sync'] = True
    res = CARD.Transaction(req)
    print(res)
    res = CARD.Transaction({
        "req": "file.delete",
        "files": ["image.qi"]
    })
    print(res)


def send_to_notehub(imageName, destDeviceUID):
    """Compresses and encodes an image. Then sends the encoding to the Notecard
    which will forward it to Notehub as soon as cellular signal is found."""

    # load image from file
    imageData = Image.open(imageName)
    imageData = imageData.resize((240, 200))

    imageData = imageData.convert('RGB')

    # Qual 1, 2 have a ~3kb filesize, q3 bumps to 4k with no notable change
    imageData.save('temp.webp', 'webp', optimize=True, quality=2)
    # Image.close(imageName)

    # convert b64
    with open("temp.webp", "rb") as image_file:
        b64Data = base64.b64encode(image_file.read()).decode('UTF-8')

        # send a note.add with the image as the body
        req = {'req': 'note.add'}
        req['file'] = 'image.qo'
        req['sync'] = True
        req['body'] = {
            'image': b64Data,
            'destDeviceUID': destDeviceUID
        }
        res = CARD.Transaction(req)
        print(res)


def get_from_notehub(imageName):
    """If an image is the inbound queue, image.qi, decode and save the image."""

    req = {'req': 'note.get'}
    req['file'] = 'image.qi'
    req['sync'] = True
    req['delete'] = True

    res = CARD.Transaction(req)
    if not ('body' in res and 'image' in res['body']):
        print("can't get image from notehub right now")
        print(res)
        return

    b64Data = res['body']['image']
    imageData = Image.open(io.BytesIO(base64.b64decode(b64Data)))
    imageData = imageData.convert('RGB')
    imageData.save(imageName, 'jpeg')
