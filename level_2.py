#! /usr/bin/env python

# Usage: ./level_2.py, then input your plaintext

# hint: the solution to this is surprisingly similar to level 0

secret = raw_input("Please enter your plaintext: ")

output = ""

for char in secret:
    output += chr(ord(char) ^ 0xFF)

print output.encode('hex')
