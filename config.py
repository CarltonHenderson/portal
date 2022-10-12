import notecomm

this_device = notecomm.card.Transaction({"req": "hub.get"})["sn"]
orange_devUID = "dev:5c02723120f3"
blue_devUID = "dev:94deb822f2a6"

target_device = blue_devUID if this_device == "orange" else orange_devUID

debug=True
if debug:
    target_device = orange_devUID
