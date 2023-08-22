# Reads from the RFID readers and creates a dictionary of all the tag texts,
# where the corresponding ids are the keys and writes it to a json file.

import RPi.GPIO as GPIO
import multiple_handler
import json

# open tag and reader position dictionaries
nfc = multiple_handler.NFC()
nfc.addBoard("reader0", 5)
nfc.addBoard("reader1", 6)
nfc.addBoard("reader2", 20)
nfc.addBoard("reader3", 21)
nfc.addBoard("reader4", 23)
nfc.addBoard("reader5", 24)

with open("id_dict.json", 'r') as f:
    mapping = json.load(f)

try:
    while True:
        for i in range(6):
            id, text = nfc.read(f"reader{i}")
            if id is not None and text not in (None, "", "none"):
                mapping[id] = int(text.strip())
            print(i, " : ", id, " : ", str(text).strip())

finally:
    with open("id_dict.json", 'w') as f:
        json.dump(mapping, f)
    print("cleaning up")
    GPIO.cleanup()