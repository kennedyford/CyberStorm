# import some stuff
import socket
from sys import stdout
from time import time

# Will print out our delta time if set to True
DEBUG = False

# Pivot points to be changed depending on the time delay
PIVOT_ZERO = 0.025
PIVOT_ONE = 0.1

# empty string to append the binary message to for decoding
message = ""

# ip and port variables for connecting to a server
ip = "138.47.99.64" 
port = 12000

# Our decode function from our previous programs
def decode(data):
    AmountofBits = []
    #split the string into array containing n amount of bits
    i = 0
    for x in range(int(len(data)/8)):
        char = int(data[i:i+8], base=2)
        if (char == 8): AmountofBits.pop() #remove last character if code is BackSpace
        else: AmountofBits.append(chr(char))
        i += 8
    return AmountofBits

# connects to the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((ip, port))
print("Connected to the server...\n")

# until the message has all been printed out, record the time between
# each message sent, and record its value in the delta variable

data = s.recv(4096).decode()
while (data.rstrip("\n") != "EOF"):
    stdout.write(data) # print(data)
    stdout.flush()

    t0 = time()
    data = s.recv(4096).decode()
    t1 = time()
    delta = round(t1 - t0, 3)

    # if DEBUG is set to True, it will als print out the delta time variable
    if (DEBUG == True):
        stdout.write(" {}\n".format(delta))
        stdout.flush()

    # creates the secret message in binary depending on the difference between
    # the delta time and the pivot points
    if (abs(PIVOT_ZERO - delta) < abs(PIVOT_ONE - delta)):
        message += "0"
    else:
        message += "1"

# decodes the binary into ascii and prints out the result
decoded_message = decode(message)
for c in decoded_message:
    print(c, end='')

# ends the connection with the server 
s.close()
