import math
import random
import os

# Check range of x and y


def checkRange(num):
    if num > 512 or num < -512:
        print("Your input must be within the range [512, -512]")
        exit()


localMin = float()

x = float(input("Enter a value for x:\n"))
checkRange(x)
y = float(input("Enter a value for y:\n"))
checkRange(y)

p = int(input("Enter a value for p:\n"))
inputz = float(input("Enter a value for z:\n"))
z = [-inputz, inputz]

seed = str(input("Would you like to use a seed? (y/n)\n"))
if seed == "y" or seed == "yes":
    seed = float(input("What would you like to use for the seed?\n"))
    random.seed(seed)
else:
    seed = None
    random.seed()

# Print (x, y), p, and z
print()
print(f"Starting points at: ({x}, {y})")
print(f"Number of neighbors \"p\" is {p}")
print(f"Neighborhood size \"z\" is {z}")
if seed:
    print(f"Seed: {seed}")
term_size = os.get_terminal_size()
print(u'\u2500' * term_size.columns)
print()

# Function f(x, y)


def f(x, y):
    ans = float(
        -(y + 47) * math.sin(math.sqrt(abs((x/2) + (y + 47)))) -
        x * math.sin(abs(x - (y+47)))
    )
    return ans


def zFuncX(x):
    newX = x + random.uniform(z[0], z[1])

    if x > 512 or x < -512:
        zFuncX(x)
    else:
        return newX


def zFuncY(y):
    newY = y + random.uniform(z[0], z[1])

    if y > 512 or y < -512:
        zFuncY(y)
    else:
        return newY


# Initial (x, y)
localMin = f(x, y)


def RHC(x, y, p, z):
    for i in range(1, p+1):
        newX = zFuncX(x)
        newY = zFuncY(y)

        print(f"{newX}, {newY}")


print("Initial (x, y):")
print(f"f({x}, {y}) = {localMin}")
print()

RHC(x, y, p, z)
