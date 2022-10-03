from ftplib import *

# Determines whether the program will translate a 7 or 10 bit code
METHOD = "10"

# FTP server info for ease of access
IP = "138.47.135.156"
PORT = 8008
USER = "thesun"
PASSWORD = "primusprovocatione"
Directory = "/.secretstorage/.folder2/.howaboutonemore" #+ METHOD
files = []

# login to the server, obtain the desired files in the desired directory, and then exits.
ftp = FTP()
ftp.connect(IP, PORT)
ftp.login(USER, PASSWORD)
ftp.cwd(Directory)
ftp.dir(files.append)
ftp.quit()

# decode function taken from Binary.py
def decode(data):
    AmountofBits = []
    #split the string into array containing n amount of bits
    i = 0
    for x in range(int(len(data)/7)):
        char = int(data[i:i+7], base=2)
        if (char == 8): AmountofBits.pop() #remove last character if code is BackSpace
        else: AmountofBits.append(chr(char))
        i += 7
    return AmountofBits

# converts the permissions into binary and returns the string.
def translate(data):
    binary = ""
    for c in data:
        if c == '-': binary += "0"
        else: binary += "1"
    return binary

code = ""
for f in files:
    if METHOD == "7":
        # if the method is 7, it checks if the file meets the 7 bit code requirements,
        # it then isolates the desired permissions for decoding.
        if f[:3] == "---":
            code += f[3:10]
    elif METHOD == "10":
        # if the method is 10, it isolated the permissions of each file for decoding
        code += f[:10]

# translates the permissions into binary, and then decodes the binary into ascii characters
message = decode(translate(code))

# prints the final decoded message
for c in message:
    print(c, end='')
