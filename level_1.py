#! /usr/bin/env python

# Usage: ./level_1.py, then input your plaintext

# Hint: this is a chain of easy-to-reverse functions

secret = raw_input("Please enter your plaintext: ")

print secret.encode('hex')[1:] + secret.encode('hex')[::-1][-1]
