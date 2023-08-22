# This file writes to an RFID reader and waits until it can write to a tag before continuing.
# It can only run with 1 reader connected.

import RPi.GPIO as GPIO
from mfrc522.SimpleMFRC522 import SimpleMFRC522

reader = SimpleMFRC522()

try:
    while True:
        text = input('New Text: ')
        print("Now scan a tag to write")
        id, text = reader.write(text) 
        print("written")
        
        print(id)
        print(text)
finally:
    print("cleaning up")
    GPIO.cleanup()
