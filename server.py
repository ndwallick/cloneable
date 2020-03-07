# Master server to process UDP commands from PC

import socket
from picamera import PiCamera
from time import sleep
import sys


# Print python version
print('Python version:', sys.version)

# Initialize camera
camera = PiCamera()
camera.resolution = (3280,2464)

UDP_IP = "10.255.255.255"   # address to listen for messages on (10.255.255.255 is broadcast address)
UDP_PORT = 5005             # port to listen on

# Initialize socket
#                    Socket family         UDP
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  # Create socket object
sock.bind((UDP_IP, UDP_PORT))                            # Bind ip and port to socket object

# Endless loop listening for commands from PC
while True:
    print('listening for UDP messages...    Press ctrl-c to quit')

    data, addr = sock.recvfrom(1024) # blocking until message is received, buffer size is 1024 bytes
    print("received message:", data)
    
    if data==b'pic':
        # Take pic
        print('warming up camera')
        sleep(2)
        print('capturing pic')
        camera.capture('image.jpg')
        print('done!')
    elif data==b'qit':
        # Quit script
        print('quitting server.py')
        quit()
    else:
        print('unknown command')