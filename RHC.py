import math
import random
import os

def checkRange(num):
    if num > 512 or num < -512:
        print("Your input must be within the range [512, -512]")
        exit()

x = int(input("Enter a value for x:\n"))
checkRange(x)
y = int(input("Enter a value for y:\n"))
checkRange(y)

print()
print(f"Starting points at: ({x}, {y})")
term_size = os.get_terminal_size()
print(u'\u2500' * term_size.columns)
print()
