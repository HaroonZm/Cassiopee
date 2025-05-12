x=[[int(c) for c in input().split()] for _ in range(3)]
if 1 == len({r[0]-r[1] for r in x}) == len({r[0]-r[2] for r in x}):
    print('Yes')
else:
    print('No')