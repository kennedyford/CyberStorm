# CyberStorm
CyberStorm is a problem solving competition at Louisiana Tech University which is done by the students taking CSC 442 - Introduction to Cyber Security.
In the class, we were divided into groups and then developed these programs that we used to solve the challenges in the competition. The team that I was apart of earned second place overall in the competition. Below, I will break down some of the programs and describe them briefly.

<h4> Binary.py </h4>
  > A program that takes a large amount of binary numbers, and then decodes the binary into either 7-bit or 8-bit ASCII.

<h4> chat-client.py </h4>
  > Receives a message from a server and then measures the timing between the characters. These times will then be used to evaluate to either a 0 or a 1 which will then be passed into the Binary.py file to decode a hidden message.

<h4> fetch.py </h4>
  > Connects to a server based on an IP and a port number, signs in using a given username and password, goes to a directory that is specified, and reads in the permissions of each file in the directory. Then, it reads in any "-" as a 0 and anything else (permissions and folder specifications) as a 1 and then decodes the binary using our
Binary.py file
