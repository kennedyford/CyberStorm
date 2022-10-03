import sys

LOWERCASE = "abcdefghijklmnopqrstuvwxyz"
UPPERCASE = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"



input = ""
for line in sys.stdin:
    input += line



def encrypt(key):
    key = key.replace(" ","").lower()
    cipher = ""
    i = 0
    for x in input:
        if (65 <= ord(x) <= 90):
            encrypted_char = ((ord(x)-65) + (ord(key[i%len(key)])-97)) % 26
            cipher += UPPERCASE[encrypted_char]
            i += 1
        elif(97 <= ord(x) <= 122):
            encrypted_char = ((ord(x)-97) + (ord(key[i%len(key)])-97)) % 26
            cipher += LOWERCASE[encrypted_char]
            i += 1
        else:
            cipher += x
    return cipher



def decrypt(key):
    key = key.replace(" ","").lower()
    cipher = ""
    i = 0
    for x in input:
        if (65 <= ord(x) <= 90):
            decrypted_char = (26 + (ord(x)-65) - (ord(key[i%len(key)])-97)) % 26
            cipher += UPPERCASE[decrypted_char]
            i += 1
        elif(97 <= ord(x) <= 122):
            decrypted_char = (26 + (ord(x)-97) - (ord(key[i%len(key)])-97)) % 26
            cipher += LOWERCASE[decrypted_char]
            i += 1
        else:
            cipher += x
    return cipher



if (sys.argv[1] == "-e"):
    print(encrypt(sys.argv[2]))
elif (sys.argv[1] == "-d"):
    print(decrypt(sys.argv[2]))
