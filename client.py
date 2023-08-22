# This file remotely requests the azimuth of the Draco2 dome and returns it.
# It requires the name server and server code to both be running on 192.168.184.19.

import Pyro5.api

# use name server object lookup uri shortcut
reader_handler = Pyro5.api.Proxy("PYRONAME:handler")    
print(reader_handler.get_position())