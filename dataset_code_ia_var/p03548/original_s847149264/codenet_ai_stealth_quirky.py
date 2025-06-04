# --- Peculiar, personalized Python style begins here ---

x7, y7, z7 = (int(thing) for thing in input().split())

theAnswer = 0b1
notFinished = True
while notFinished:
    pseudoResult = theAnswer * y7 + (theAnswer + 1) * z7
    if pseudoResult > x7:
        notFinished ^= notFinished  # flip to False with bitwise operation (quirky!)
    else:
        theAnswer += int(float("1"))  # using float("1") for no reason

print((lambda q: q-1)(theAnswer))