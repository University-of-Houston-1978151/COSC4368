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

p = int(250)
z = float(0.5)
#p = int(input("Enter a value for p:\n"))
#z = float(input("Enter a value for z:\n"))

seed = str(input("Would you like to use a seed? (y/n)\n"))
if seed == "y" or seed == "yes":
    seed = float(input("What would you like to use for the seed?\n"))
    random.seed(seed)
else:
    seed = None
    random.seed(99)

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
    ans = float((-y-47) * math.sin(math.sqrt(abs((x/2) + (y+47)))
                                   ) - x * math.sin(math.sqrt(abs(x - (y + 47)))))
    return ans


# Initial (x, y)
original = {
    "sol": [x, y],
    "fsol": f(x, y),
    "p": p
}
best = {
    "sol": [x, y],
    "fsol": f(x, y),
    "neighbor": None
}

localMin = f(x, y)

count = 1
check = False


def RHC(x, y, p, z, localMin):
    global original
    global best
    global count
    global check

    p -= 1
    count += 1

    newX = x + random.uniform(-z, z)
    while x > 512 or x < -512:
        newX = x + random.uniform(-z, z)
    newY = y + random.uniform(-z, z)
    while y > 512 or y < -512:
        newY = y + random.uniform(-z, z)

    newSol = f(newX, newY)
    print(f"{count} | f({newX}, {newY}) = {newSol}")

    if newSol < best['fsol']:
        check = True
        best['fsol'] = newSol
        best['sol'] = [newX, newY]
        best['neighbor'] = count
        print(f"New local minimum is now {best['fsol']}")

    if p != 0:
        RHC(x, y, p, z, localMin)
    else:
        print(u'\u2500' * term_size.columns)
        if check == True:
            check = False
            RHC(x, y, original['p'], z, best['fsol'])


print(
    f"{count} | f({original['sol'][0]}, {original['sol'][1]}) = {original['fsol']}"
)
RHC(x, y, p-1, z, localMin)

print()
print()
print("Results of RHC")
print()
print("Input")
print(f"- Starting Point: ({original['sol'][0]}, {original['sol'][1]})")
print(f"- p: {p}")
print(f"- z: {z}")
if seed:
    print(f"- Seed: {seed}")
print(f"- Solution: {original['fsol']}")
print()
print("Best Solution")
print(f"- Solution: ({best['sol'][0]}, {best['sol'][1]})")
print(f"- Neighbor ID: {best['neighbor']}")
print(f"- Total Neighbors: {count}")
print(f"- f(sol): {best['fsol']}")
print()
print()
#print("Initial (x, y):")
#print(f"f({x}, {y}) = {localMin}")
# print()
#print(u'\u2500' * term_size.columns)

#lM = RHC(x, y, p, z, localMin)

# print()
# print()
#print("Results of RHC")
# print()
# print("Input")
#print(f"- Starting Point: ({x}, {y})")
#print(f"- p: {p}")
#print(f"- z: {z}")
# if seed:
#    print(f"- Seed: {seed}")
#print(f"- Solution: {origSol}")
# print()
##print("Best Solution")
#print(f"- Solution: ({bestSolCoords[0]}, {bestSolCoords[1]})")
#print(f"- Neighbor ID: {bestSolNeighbor}")
#print(f"- Total Neighbors: {count}")
#print(f"- f(sol): {lM}")
# print()
# print()
