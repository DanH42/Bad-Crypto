#! /usr/bin/env python

# Usage: ./level_4.py, then input your plaintext

# hint: character by character encoding is a bad idea

secret = raw_input("Please enter your plaintext: ")

def encrypt_char(char):
    char = ord(char)
    char <<= 2
    char &= 0xFF
    char ^= 0xFF
    char >>= 1
    char = chr(char)
    return(char)

output = ""

for char in secret:
    output += encrypt_char(char)

print output.encode('hex')
