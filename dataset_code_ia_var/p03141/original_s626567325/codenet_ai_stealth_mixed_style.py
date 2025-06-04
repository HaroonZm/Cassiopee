n = int(input())
from functools import reduce

C = list()
BS = 0

def happiness(line):
    return tuple(map(int, line.split()))
    
for I in range(n):
    A,B = happiness(input())
    BS += B
    C += [A+B]

tmp = sorted(C, reverse=True)
result = -BS

for idx, val in enumerate(tmp):
    if not idx%2:
        result = result + val

print(result)