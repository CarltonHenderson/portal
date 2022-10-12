import notecard
from PIL import Image
import base64

notehub_uid = 'com.blues.portal'
port = I2C('/dev/i2c-1')
card = notecard.OpenI2C(port, 0, 0)

# init needs to be run once on startup, afterward
# repeatedly alternate send and rcv between the  cards

def init_notecard():
    req = {'req': 'hub.set'}
    req['product'] = notehub_uid
    req['mode'] = 'continuous'
    req['sync'] = True
    res = card.Transaction(req)
    print(res)

def send_to_notehub():
    #load image from file 
    imageData = Image.open('imageIn.jpg')
    imageData = imageData.resize((240, 200))

    imageData = imageData.convert('RGB')

    # Qual 1, 2 have a ~3kb filesize, q3 bumps to 4k with no notable change
    imageData.save('imageIn.webp', 'webp', optimize = True, quality = 2)
    Image.close('imageIn.jpg')

    #convert b64
    b64Data = base64.b64encode(Image.open(b'imageIn.webp'))

    #send a note.add with the image as the body
    req = {'req': 'note.add'}
    req['file'] = 'image.qo'
    req['sync'] = True
    req['body'] = {
    'image': b64Data,
    }
    res = card.Transaction(req)
    print(res)

def get_from_notehub():
    req = {'req': 'note.get'}
    req['file'] = 'image.qi'
    req['sync'] = True

    res = card.Transaction(req)
    #print(res)
    b64Data = res['image']
    imageData = base64.b64decode(b64Data)
    imageData = imageData.convert('RGB')
    imageData.save('imageOut.jpg', 'jpeg')