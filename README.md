# CyberStorm
CyberStorm is a problem solving competition at Louisiana Tech University which is done by the students taking CSC 442 - Introduction to Cyber Security.
In the class, we were divided into groups and then developed these programs that we used to solve the challenges in the competition. The team that I was apart of earned second place overall in the competition. Below, I will break down some of the programs and describe them briefly.

<h4> Binary.py </h4>
A program that takes a large amount of binary numbers, and then decodes the binary into either 7-bit or 8-bit ASCII.

<h4> chat-client.py </h4>
Receives a message from a server and then measures the timing between the characters. These times will then be used to evaluate to either a 0 or a 1 which will then be passed into the Binary.py file to decode a hidden message.

<h4> fetch.py </h4>
Connects to a server based on an IP and a port number, signs in using a given username and password, goes to a directory that is specified, and reads in the permissions of each file in the directory. Then, it reads in any "-" as a 0 and anything else (permissions and folder specifications) as a 1 and then decodes the binary using our
Binary.py file

<h4> Steg.py </h4>
A program which can both decode and encode steganography files. It gives the user many different options when encoding or decoding such as bit or byte mode, bits to skip before processing, space between the information in the wrapper, etc. More information about steganography <a href="https://en.wikipedia.org/wiki/Steganography">here</a>

<h4> timelock.py / timelockC.py </h4>
Takes the current time and hashes it twice. It then takes the first two letters in the hash and then the first two numbers from the right and uses it as a sort of multi-factor authentication. (timelockC.py adds a firth character and was created / edited during the challenge on the fly)

<h4> vigenere.py </h4>
Performs a vigenere cipher on a given message using a given key. Learn more information about the vigenere cipther <a href="https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher">here</a>

<h4> XOR.py </h4>
Inacts an Exclusive Or logical operation on the bits of two elements (strings, files, images, etc.)

<br><br><br>
<footer align="center"> **NOTE: Although I did write many of these programs myself, I did not write all of them myself. Additional credit for these programs goes to Austin Belmonte, Meagan Kropp, Leandro Londin, Stephanie Orellana, and Terence Tugwell </footer>
