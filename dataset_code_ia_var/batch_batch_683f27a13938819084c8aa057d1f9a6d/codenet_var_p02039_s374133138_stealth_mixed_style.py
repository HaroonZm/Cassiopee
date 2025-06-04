res = []
from functools import reduce
for _ in range(int(input())):
    line = input()
    x, y, z, w = (int(t) for t in line.split())
    answer = 0
    i = x
    while i <= z:
        def calc(k, accum):
            if i%2==1 and k%2==0:
                return accum
            return accum+1
        answer = reduce(lambda acc, val: calc(val, acc), range(y, w+1), answer)
        i += 1
    res.append(answer)
[x for x in map(print, res)]