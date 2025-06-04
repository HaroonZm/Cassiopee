s = set()
N = int(input())
for i in range(N):
    data = input().split()
    q = data[0]
    x = data[1]
    if q == '0':
        s |= {x}
        print(len(s))
        continue
    if 1 == int(q):
        out = 1 if x in s else 0
        print(out)
        continue
    [s.remove(x) if x in s else None] # list comprehension as side effect; mimic discard