#!/usr/bin/python3
import io
import sys
import argparse

STORE = True
BITMODE = True
SENTINEL = bytearray(b"\x00\xff\x00\x00\xff\x00")
OFFSET = 0
INTERVAL = 1
args = ""


#######################
### PARSE ARGUMENTS ###
#######################
def print_help():
    print(f"Usage: {sys.argv[0]} -(sr) -(bB) [-o<val>] [-i<val>] -w<val> [-h<val>]\n\
 -s      store\n -r      retrieve\n -b      bit mode\n -B      Byte mode\n\
 -o<val> set offset to <val> (default is 0)\n -i<val> set interval to <val> (default is 1)\n\
 -w<val> set wrapper file to <val>\n -h<val> set hidden file to <val>")
while(True):
    if (len(sys.argv) < 2):
        print_help()
        break
    #Chooses whether store or retrieve mode
    if (sys.argv[1] == "-s"): STORE = True
    elif (sys.argv[1] == "-r"): STORE = False
    else:
        print_help()
        break
    #Chooses either BIT or BYTE mode
    if (sys.argv[2]) == "-b": BITMODE = True
    elif (sys.argv[2]) == "-B": BITMODE = False
    else: 
        print_help()
        break
    #if use argparse need version 3.2
    #Setup and parse arguments for files , interval, and offset
    parser = argparse.ArgumentParser(add_help=False, usage="%(prog)s -(sr) -(bB) [-o<val>] [-i<val>] -w<val> " + ("-h<val>" if (STORE) else "[-h<val>]"))
    parser.add_argument("-s", action="store_true")
    parser.add_argument("-r", action="store_true")
    parser.add_argument("-b", action="store_true")
    parser.add_argument("-B", action="store_true")
    parser.add_argument("-o", type=int, default=0, help="Bits to skip before starting to process wrapper")
    parser.add_argument("-i", type=int, default=1, help="Space between information in wrapper")
    parser.add_argument("-w", type=ascii, help="Wrapper file", required=True)
    if (STORE): parser.add_argument("-h", type=ascii, help="File to store in the Wrapper", required=True)
    args = parser.parse_args()
    OFFSET = args.o
    INTERVAL = args.i
    break

#BITMODE
if (BITMODE):
    #STORING
    if (STORE):
        #Read the wrapper and hidden files as binarary
        wrapper = bytearray(open(args.w.replace("'", ""), "rb").read())
        hidden = bytearray(open(args.h.replace("'", ""), "rb").read()) + SENTINEL
        i = 0
        while (i < len(hidden)):
            #For every bit in hidden file
            for j in range(0, 8):
                #Set last bit of wrapper to 0
                wrapper[OFFSET] &= 0b11111110
                #Set last bit off wrapper to first bit of hidden
                wrapper[OFFSET] |= (hidden[i] & 0b10000000) >> 7 
                #Set first bit of hidden to the next bit
                hidden[i] = (hidden[i] << 1) & 0b11111111
                OFFSET += INTERVAL
            i += 1
        sys.stdout.buffer.write(wrapper)
    #RETRIEVE
    else:
        #Read wrapper as binary
        wrapper = bytearray(open(args.w.replace("'", ""), "rb").read())
        hidden = bytearray()

        i = 0
        while (OFFSET < len(wrapper) - 8 and i != len(SENTINEL)):
            b = 0
            #For every bit in wrapper
            for j in range(0, 8):
                #SET b to last bit of wrapper
                b |= (wrapper[OFFSET] & 0b00000001)
                if (j < 7):
                    #Shift b by 1
                    b = (b << 1)
                    OFFSET += INTERVAL
            hidden.append(b)
            #if i = 6 we have the whole sentinel
            if (b == SENTINEL[i]): i += 1
            else: i = 0
            OFFSET += INTERVAL
        
        sys.stdout.buffer.write(hidden[:-len(SENTINEL)])

#BYTE
else:
    #STORING
    if (STORE):
        #READ WRAPPER FILE BYTES AND HIDDEN FILE BYTES
        wrapper = bytearray(open(args.w.replace("'", ""), "rb").read())
        hidden = bytearray(open(args.h.replace("'", ""), "rb").read())
        i = 0
        while (i < len(hidden)):
            #SET wrapper byte to hidden byte
            wrapper[OFFSET] = hidden[i]
            OFFSET += INTERVAL
            i+=1

        i=0
        #Write sentinel
        while (i < len(SENTINEL)):
            #Set wrapper byte to sentinel byte
            wrapper[OFFSET] = SENTINEL[i]
            OFFSET += INTERVAL
            i+=1
        sys.stdout.buffer.write(wrapper)
    #RETRIEVE
    else:
        #READ WRAPPER FILE BYTES
        wrapper = bytearray(open(args.w.replace("'",""), "rb").read())
        hidden = bytearray()

        i=0
        #Loop over wrapper until sentinel is found
        while (OFFSET < len(wrapper) and i != len(SENTINEL)):
            #If Wrapper equals sentinel byte
            if (wrapper[OFFSET] == SENTINEL[i]): i += 1
            else: i = 0
            hidden.append(wrapper[OFFSET])
            OFFSET += INTERVAL
        #WRITE HIDDEN TO STDOUT WITHOUT SENTINEL
        sys.stdout.buffer.write(hidden[:-len(SENTINEL)])
        
