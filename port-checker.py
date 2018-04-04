#!/usr/bin/python
import socket

print " Port Open/Close Checker by Aga Ismail"

print " fb: www.fb.com/manguree "
print " email: agaesmaeel@gmail.com "

print "__________________________________________________________"

print " "

ip = raw_input("Enter the ip: ")
port = input("Enter the port number: ")
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if sock.connect_ex((ip,port)):
        print "Port", port, "is closed"
else:
        print "Port", port, "is open"




