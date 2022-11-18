"""Portal Configuration"""

# Portal Application Config
ORANGE_DEVICEUID = "dev:5c02723120f3"
BLUE_DEVICEUID = "dev:94deb822f2a6"
# Find the DeviceUID on the small sticker (QR-code and human readable) that
# comes with each Notecard. Or, without the sticker, use `{"req":"hub.get"}`.

THIS_DEVICE = BLUE_DEVICEUID
TARGET_DEVICE = ORANGE_DEVICEUID

# Linux <=> Notecard
NOTECARD_I2C_DEVICE = '/dev/i2c-1'

# Notecard <=> Notehub Project
notehub_productUID = 'com.example.johndoe:portal'
# If you're using a WiFi Notecard, follow this guide to set the wifi password.
# https://dev.blues.io/guides-and-tutorials/notecard-guides/connecting-to-a-wi-fi-access-point/
