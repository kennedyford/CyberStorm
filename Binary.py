def decode(n):
    AmountofBits = []
    #split the string into array containing n amount of bits
    i = 0
    for x in range(int(length/n)):
        code = int(input[i:i+n], base=2)
        if (code == 8): AmountofBits.pop() #remove last character if code is BackSpace
        else: AmountofBits.append(code)
        i += n

    for char in AmountofBits:
        print(chr(char), end='')
    print()
    #for char in AmountofBits:
    #    print(char, end=' ')

input = input() #get input from stdin
length = len(input)

if (length % 7 == 0): decode(7)
if (length % 8 == 0): decode(8)
