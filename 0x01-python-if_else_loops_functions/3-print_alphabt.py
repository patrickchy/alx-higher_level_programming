#!/usr/bin/python3

output = ""

for letter in range(ord('a'), ord('z') + 1):

    if (chr(letter) != 'e' and chr(letter) != 'q'):
        print("{}".format(chr(letter)), end='')
