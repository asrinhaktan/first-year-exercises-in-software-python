#mac changer for kali linux

import subprocess
import optparse

parse_object = optparse.OptionParser()
parse_object.add_option("-i","--interface", dest="interface",help="interface to change")
parse_object.add_option("-m","--mac", dest="mac_adress",help="mac adress to change")

print(parse_object.parse_args())

print("mac changer is complete!")