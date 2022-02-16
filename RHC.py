import math
from termios import IXOFF

x = int(input("Enter a value for x:\n"))
y = int(input("Enter a value for y:\n"))

if x > 512 or x < -512:
    print("\"x\" must be within the [-512, 512] range.")
    exit()

if y > 512 or y < -512:
    print("\"y\" must be within the [-512, 512] range.")
    exit()

print()
print(x)
print(y)