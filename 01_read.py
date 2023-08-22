# This file reads from an RFID reader and waits until it can read a tag before continuing.
# It can only run with 1 reader connected.

import RPi.GPIO as GPIO
from mfrc522.SimpleMFRC522 import SimpleMFRC522

reader = SimpleMFRC522()

print("Hold a tag near the reader")

try:
    while True:
        id, text = reader.read()
        print(id)
        print(text)

finally:
    print("cleaning up")
    GPIO.cleanup()
