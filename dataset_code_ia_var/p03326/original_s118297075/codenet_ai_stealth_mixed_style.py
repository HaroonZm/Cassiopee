import functools

def get_input():
    return list(map(int, input().split()))

N, M = get_input()

L = []
i = 0
while i < N:
    L.append([int(x) for x in input().split()])
    i += 1

maxim = -float('inf')
vals = [-1,1]

for s in ([ (a,b,c) for a in vals for b in vals for c in vals ]):
    res = []
    idx = 0
    while idx < N:
        triple = L[idx]
        val = 0
        for j in range(3):
            if j==0:
                f = lambda x: x * s[0]
            elif j==1:
                f = lambda x: x * s[1]
            else:
                f = lambda x: x * s[2]
            val += f(triple[j])
        res.append(val)
        idx += 1
    res.sort(key=lambda x: -x)
    maxim = maxim if maxim > sum(res[:M]) else sum(res[:M])

print(maxim)