# This file needs to be run to allow other computers on the astrolab network
# to request the dome azimuth.
# It requires a name server to be running on this machine;
# to start the nameserver run 'pyro5-ns -n 192.168.184.19' in a terminal.

import Pyro5.api
import RPi.GPIO as GPIO
import multiple_handler
import json

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

# function that returns dome azimuth
@Pyro5.api.expose
class handler(object):
    def get_position(self):
        for i in range(6):
            id, text = nfc.read(f"reader{i}", only_id=True)
            if id is not None:
                position = int(dome_data[f"reader{i}"] + id_dict[str(id)]*dome_data['gap'])
                if position > 360:
                    position -= 360
                return position
        return None

# setup pyro5 server     
daemon = Pyro5.server.Daemon(host='192.168.184.19')      # make a Pyro daemon
ns = Pyro5.api.locate_ns()          # find the name server
uri = daemon.register(handler)      # register the handler as a Pyro object
ns.register("handler", uri)         # register the object with a name in the name server
print(uri)
print("Ready.")
daemon.requestLoop()                # start the event loop of the server to wait for calls
