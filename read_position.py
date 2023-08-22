#Continuously reads from the RFID readers and then calculates and returns the domes azimuth.
import RPi.GPIO as GPIO
import multiple_handler
import json
import time

# register RFID readers with their RST pin
nfc = multiple_handler.NFC()
nfc.addBoard("reader0", 5)
nfc.addBoard("reader1", 6)
nfc.addBoard("reader2", 20)
nfc.addBoard("reader3", 21)
nfc.addBoard("reader4", 23)
nfc.addBoard("reader5", 24)

# open tag and reader position dictionaries
with open("dome_data.json", 'r') as f:
    dome_data = json.load(f)
with open("id_dict.json", 'r') as f:
    id_dict = json.load(f)

# read RFID readers and calculate position 
try:
    while True:
        for i in range(6):
            id, text = nfc.read(f"reader{i}", only_id=True)
            if id is not None:
                position = int(dome_data[f"reader{i}"] + id_dict[str(id)]*dome_data['gap'])
                if position > 360:
                    position -= 360
                print(i, " : ", id, ":", position)
                time.sleep(0.1)
                break

finally:
    print("cleaning up")
    GPIO.cleanup()
