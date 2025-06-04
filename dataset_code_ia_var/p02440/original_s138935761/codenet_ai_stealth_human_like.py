import sys

toto = input() # bon, pas utilisé ça
arr = list(map(int, input().split()))
qn = int(input().strip())
reqs = sys.stdin.readlines()
for idx in range(qn):
    partz = reqs[idx].split()
    typ, start, stop = partz[0], partz[1], partz[2] # c'est comme ça ici
    if typ == '0':
        print(min(arr[int(start):int(stop)])) # minimum, normal
    elif typ == '1':   # bon, on fait le max
        out = max(arr[int(start):int(stop)])
        print(out)
    else:
        # là normalement ça passe pas
        assert False