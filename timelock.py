#import some stuff
from sys import stdin
from datetime import datetime
from hashlib import md5
import pytz

### VARIABLES ###
DEBUG = False
INTERVAL = 60
CURRENT_TIME = ""
EPOCH_TIME = input()

#removes the spaces of the epoch given and puts it into an array for ease of use
EPOCH_TIME = EPOCH_TIME.split(" ")

#return the datetime of both the current system time and the given epoch time
CURRENT_TIME = datetime.now().replace(microsecond = 0)
EPOCH_TIME = datetime(int(EPOCH_TIME[0]), int(EPOCH_TIME[1]), int(EPOCH_TIME[2]), int(EPOCH_TIME[3]), int(EPOCH_TIME[4]), int(EPOCH_TIME[5]))

#localizes epoch time to local timezone
timezone = pytz.timezone("America/Chicago")
EPOCH_TIME = EPOCH_TIME.astimezone(timezone)

#takes the datetime (in seconds) and determins a delta time
d_time = CURRENT_TIME.timestamp() - EPOCH_TIME.timestamp()
d_time -= (d_time % 60) #makes sure the code only lasts for the current minute

# hashes the delta time variable twice at once
myHash = md5((md5(str(int(d_time)).encode())).hexdigest().encode()).hexdigest()

# debug section
if (DEBUG == True):
    print(f"Current datetime: {CURRENT_TIME}")
    print(f"Epoch datetime: {EPOCH_TIME}")
    print(f"Current Time in seconds: {CURRENT_TIME.timestamp()}")
    print(f"Epoch Time in seconds: {EPOCH_TIME.timestamp()}")
    print(f"d-time: {CURRENT_TIME.timestamp() - EPOCH_TIME.timestamp()}")
    print(f"new d-time: {d_time}")
    print(f"first hash: {md5(str(int(d_time)).encode()).hexdigest()}")
    print(f"socond hash: {myHash}")
    print("Code: ", end='')


### More Declarations ###
code = ""
letters = ['a', 'b', 'c', 'd', 'e', 'f']
nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

i = 0
lettersInCode = 0
numsInCode = 0


#gets the first two letters [a-f] from left to right and appends it to the code
while (i < len(myHash)):
    for letter in letters:
        if (myHash[i] == letter):
            code += letter
            lettersInCode += 1
            break
        
    if (lettersInCode == 2):
        break
    
    i += 1

#resets the i counter to search the hash from right to left
i = len(myHash) - 1

#gets the first two numbers [0-9] from right to left and appends it to the code
while (i > -1):
    for num in nums:
        if (myHash[i] == num):
            code += num
            numsInCode += 1
            break
    if (numsInCode == 2):
        break

    i -= 1

#returns the code to stdout
print(code)


    
