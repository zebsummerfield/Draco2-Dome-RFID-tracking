# In this file a class is defined for an object which handles multiple RFID readers.

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import spidev
import time

class NFC():
    def __init__(self, bus=0, device=0, spd=1000000):
        self.reader = SimpleMFRC522()
        self.close()
        self.boards = {}
        
        self.bus = bus
        self.device = device
        self.spd = spd

        GPIO.cleanup()
        GPIO.setmode(GPIO.BCM)


    def reinit(self):
        self.reader.READER.spi = spidev.SpiDev()
        self.reader.READER.spi.open(self.bus, self.device)
        self.reader.READER.spi.max_speed_hz = self.spd
        self.reader.READER.MFRC522_Init()

    def close(self):
        self.reader.READER.spi.close()

    def addBoard(self, rid, pin):
        GPIO.setup(pin, GPIO.OUT)
        self.boards[rid] = pin

    def selectBoard(self, rid):
        for loop_id in self.boards:
            GPIO.output(self.boards[loop_id], loop_id == rid)
        if not rid in self.boards and not rid=="none":
            print("readerid " + rid + " not found")
            return False
        return True

    def read(self, rid, only_id=False):
        if not self.selectBoard(rid):
            return None, None

        time.sleep(0.01)
        self.reinit()
        time.sleep(0.01)
        cid, val = self.retry_read(only_id=only_id)
        time.sleep(0.01)
        self.close()
        time.sleep(0.01)

        self.selectBoard("none")
        return cid, val


    def retry_read(self, only_id=False, max_retries=3):
        retries=0
        while retries < max_retries:
            if not only_id:
                id, text = self.reader.read_no_block()
            else:
                id = self.reader.read_id_no_block()
                text = None
            if id is not None:
                return id, text
            time.sleep(0.01)
            retries += 1
        return None, None

    def write(self, rid, value):
        if not self.selectBoard(rid):
            return False

        time.sleep(0.01)
        self.reinit()
        time.sleep(0.01)
        self.reader.write_no_block(value)
        time.sleep(0.01)
        self.close()
        time.sleep(0.01)

        self.selectBoard("none")
        return True
