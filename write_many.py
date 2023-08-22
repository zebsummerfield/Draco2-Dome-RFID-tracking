# This file is used to number tags starting from the variable 'count'.
# It can only run with 1 reader connected.

import RPi.GPIO as GPIO
from mfrc522.SimpleMFRC522 import SimpleMFRC522
import time

reader = SimpleMFRC522()
count = 1
previous = []

try:
    while True:
 
        time.sleep(0.2)
        id, text = reader.read()
        print(id, str(text).strip())
        if isinstance(id, int) and not str(text).strip() in previous:
        
            while not str(text).strip() == str(count):
                time.sleep(0.2)
                reader.write(str(count))
                time.sleep(0.1)
                id, text = reader.read()
                
            print(f'written {str(count)}')
            previous.append(str(count))
            count += 1 
  
finally:
    print("cleaning up")
    GPIO.cleanup()
