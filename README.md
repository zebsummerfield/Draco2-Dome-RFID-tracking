# dome-RFID-tracking
The Durham University Physics Department runs 4 professional telescopes. My internship concerned working towards full automation of these telescopes, largely centered on the project of using RFID technology to fix the tracking of the domes the telescopes reside in. I was given sole responsibility of designing, prototying, implementing and refining this modificaiton to the domes. This included: programming a Raspberry Pi to run several RFID readers simultaneously; programming the Linux computers which run the telescopes to be able to communicate with the Rapberry Pi and request these positional readings; and developing the electrical and mechanical system required to mount the RFID readers and tags in the domes.

This repository contains those scripts and the relevant documentation.

The scripts were built using the mfrc522 library: https://pypi.org/project/mfrc522/.
