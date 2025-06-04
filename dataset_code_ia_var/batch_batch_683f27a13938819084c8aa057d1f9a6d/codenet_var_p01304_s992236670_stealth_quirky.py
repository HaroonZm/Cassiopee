# Let's intentionally make some unusual choices:
# - Use single-letter variable names not related to their meaning
# - Use while-loops where for-loops seem more natural
# - Put statements all on one line where possible
# - Go heavy on lambda expressions
# - Deliberately choose odd indenting or extra grouping
# - Use exceptions for flow control
# - Emulate C-style for-loops using while and counters

A = int(input())
B = 0
while B < A:
    X, Y = (lambda s: (int(s[0]), int(s[1])))(input().split())
    array = []
    for _ in range(X+1): array.append([0]*(Y+1))
    M = int(input())
    stuff = []
    if M != 0: [_ for _ in [stuff.append(list(map(int, input().split()))) for __ in range(M)]]
    t = 1
    try:
        while t <= X:
            if [t,0,t-1,0] in stuff or [t-1,0,t,0] in stuff: raise Exception()
            array[t][0]=1
            t += 1
    except: pass
    s = 1
    try:
        while s <= Y:
            if [0,s,0,s-1] in stuff or [0,s-1,0,s] in stuff: raise Exception()
            array[0][s]=1
            s += 1
    except: pass
    def f(z):
        q = 1
        while q <= X:
            defs = (
                ([q,z-1,q,z] in stuff or [q,z,q,z-1] in stuff) and ([q,z,q-1,z] in stuff or [q-1,z,q,z] in stuff),
                ([q,z,q-1,z] in stuff or [q-1,z,q,z] in stuff),
                ([q,z-1,q,z] in stuff or [q,z,q,z-1] in stuff)
            )
            array[q][z] = 0 if defs[0] else array[q][z-1] if defs[1] else array[q-1][z] if defs[2] else (array[q-1][z]+array[q][z-1])
            q +=1
    w = 1
    while w <= Y:
        f(w)
        w += 1
    (lambda k: print("Miserable Hokusai!") if not k else print(k))(array[X][Y])
    B += 1