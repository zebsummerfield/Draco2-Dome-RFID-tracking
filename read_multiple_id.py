#Continuously reads and returns only ids from 6 RFID readers.

import RPi.GPIO as GPIO
import multiple_handler

# register RFID readers with their RST pin
nfc = multiple_handler.NFC()
nfc.addBoard("reader0", 5)
nfc.addBoard("reader1", 6)
nfc.addBoard("reader2", 20)
nfc.addBoard("reader3", 21)
nfc.addBoard("reader4", 23)
nfc.addBoard("reader5", 24)

try:
    while True:
        for i in range(6):
            id, text = nfc.read(f"reader{i}", only_id=True)
            print(i, " : ", id)

finally:
    print("cleaning up")
    GPIO.cleanup()
