#!/usr/bin/python3
import sys
from os import system as cmd

# get IP
ip = input("Enter the host address to scan: ")
# default nmap
cmd('nmap '+ip+' -oA normalscan')
# seperating opened ports
cmd("cat normalscan.nmap | grep open | awk -F/ '{print $1}' ORS=',' | rev | cut -c 2- | rev > opened-ports.txt")
# opening ports file
f=open("opened-ports.txt", "r")
ports = f.read()
print("\nOPENED PORTS:")
print(ports)
# scanning only the opened ports
cmd('nmap -sC -sV '+ip+' -p'+ports)
# deleting extra files ( I used -oN flag but it took more time than -oA. So, I used -oA and deleting the extra stuffs here )
cmd('rm opened-ports.txt normalscan.gnmap normalscan.xml normalscan.nmap')
