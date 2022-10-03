# import some stuff
import sys

# reads the key file into binary
key = open('key', 'rb').read()

# reads in what we're xor-ing
text = sys.stdin.buffer.read()

final = []

# for the range of (if the key is smaller than the text: len(text); otherwise, len(key))
for i in range(len(text) if len(key) < len(text) else len(key)):

    # xor's the text and the length and appends it to the final array
    final.append(text[i%len(text)] ^ key[i%len(key)])

# writes the final array to stdout as a bytearray 
sys.stdout.buffer.write(bytearray(final))
