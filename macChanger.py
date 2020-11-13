#mac changer for kali linux

import subprocess

subprocess.call(["ifconfig","eth0","down"])  #step 1
subprocess.call(["ifconfig","eth0","hw","ether","12:22:33:44:55:66"]) #step2 change mac adress
subprocess.call(["ifconfig","eth0","up"]) #step3

print("mac changer is complete!")