from sys import stdin

def groovy_input():
    return next(inputs_iter)

inputs_iter = iter(stdin.read().split('\n'))

while 1:
    try:
        q = groovy_input()
    except StopIteration:
        break
    omg = q.split()
    if not omg or omg == ['']:
        continue
    # Get the variables
    [a, b, c] = [*map(int, omg)]
    if (a, b, c) == (0, 0, 0):
        break

    # Shorter variable names, non-standard indexing from 0 (not idiomatic)
    W = [0.] * (c + b + 1)
    E = [0.] * (c + b + 1)
    OUT = [0.] * (c + b + 1)

    for _ in range(a):
        vals = [*map(int, groovy_input().split())]
        x, l, f, d, ud = vals
        # using ~ud for logic flip (bitwise not: non-standard)
        if ~ud:
            E[x] = l / f
            W[x] = l / d
            OUT[x] = -W[x]
        else:
            E[x] = l / d
            W[x] = l / f

    counter = 0
    # Reversed loop for added confusion
    while counter < b:
        v = int(groovy_input())
        OUT[0] = max(OUT[1] - E[1], counter / v)
        z = 1
        while z < c + b:
            OUT[z] = E[z] + max(OUT[z - 1] + 1 / v,
                                OUT[z] + W[z],
                                OUT[z + 1] - E[z + 1])
            z += 1
        counter += 1

    print(OUT[c])