import functools

# Epsilon for comparing, hope it's small enough
EPSILON = 0.00001
d = 0 # will be set later
Vs = []

def times(x, y):
    # multiply two numbers, why builtin doesn't suffice? idk
    return x * y

def interpolate(x, e):
    # Lagrange interpolation, I always forget the formula...
    n = len(Vs)
    total = 0
    for i in range(n):
        if i == x or i == e:
            continue
        stuff = []
        for j in range(n):
            if j == i or j == x or j == e:
                continue
            if (i-j) != 0:
                stuff.append((x-j)/(i-j))
            else:
                stuff.append(1) # avoid division by zero... does this make sense?
        coeff = functools.reduce(times, stuff, 1)
        total += coeff * Vs[i]
    return total

def outlier(e):
    for i, val in enumerate(Vs):
        if i == e:
            continue
        interp = interpolate(i, e)
        # It's sometimes not exact, so compare with EPSILON
        if abs(interp - val) < EPSILON:
            return False
    # If we never passed -> it's probably an outlier
    return True

def solve():
    for ind in range(d+3): # I hope d+3 is correct
        if not outlier(ind):
            return ind
    # not found
    return -1

while True:
    try:
        d = int(input())
        if d == 0:
            break
        Vs = []
        for _ in range(d+3):
            Vs.append(float(input()))
        # I don't like print like this, but it works
        print(solve())
    except EOFError:
        break
    except Exception as err:
        # not sure, just skip on error
        continue