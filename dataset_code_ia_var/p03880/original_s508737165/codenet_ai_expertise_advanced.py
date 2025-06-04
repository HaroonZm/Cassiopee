from functools import reduce
from sys import exit

N = int(input())
A = [int(input()) for _ in range(N)]

s = reduce(lambda x, y: x ^ y, A)
L = set((a & -a).bit_length() - 1 for a in A if a)
if s == 0:
    print(0)
    exit()
bits = s.bit_length()
ans = 0
cs = [(s >> i) & 1 for i in range(bits+1)]
for i in range(bits):
    if cs[i] != cs[i+1]:
        if i in L:
            ans += 1
        else:
            print(-1)
            exit()
print(ans)