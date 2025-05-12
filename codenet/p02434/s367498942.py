n, seq = [int(x) for x in input().split()]
L = []
for i in range(n):
    L.append([])

for i in range(seq):
    c, t, x = [ int(x) for  x in (input() + " 0").split()][:3]
    if c == 0:
        L[t].append(x)
    elif c == 1:
        print( " ".join(map(str,L[t])) )
    elif c == 2:
        L[t].clear()
    else:
        pass