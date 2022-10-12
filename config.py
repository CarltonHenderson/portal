import notecomm

this_devUID = notecomm.card.Transaction({"req": "hub.get"})["device"]
orange_devUID = "dev:5c02723120f3"
blue_devUID = "dev:94deb822f2a6"

target_device = blue_devUID if this_devUID == blue_devUID else orange_devUID

debug=True
if debug:
    target_device = orange_devUID
