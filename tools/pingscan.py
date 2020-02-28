#!/usr/bin/python3
import sys
from scapy.all import *

if len(sys.argv) != 2:
	print("Usage: python3 pingscan.py 192.168.0.1")
	sys.exit(1)

ping = IP(dst=sys.argv[1])/ICMP()
res = sr1(ping,timeout=1,verbose=0)
if res == None :
	print("This host is down")
else:
	print("This host is up")




