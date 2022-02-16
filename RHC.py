import math

def checkRange(num):
    if num > 512 or num < -512:
        print("Your input must be within the range [512, -512]")
        exit()

x = int(input("Enter a value for x:\n"))
checkRange(x)
y = int(input("Enter a value for y:\n"))
checkRange(y)

print()
print(x)
print(y)