from functools import reduce
from sys import stdin, exit

n = int(stdin.readline())
a = [int(stdin.readline()) for _ in range(n)]

max_len = max(a, key=lambda x: x.bit_length()).bit_length()

exist = [False] * (max_len + 1000)
for val in a:
    b = val.bit_length()
    for j in range(b-1, -1, -1):
        if (val >> j) & 1:
            exist[b-1-j] = True
            break

axor = reduce(lambda x, y: x ^ y, a)
if not axor:
    print(0)
    exit()

la = axor.bit_length()
ans = 0
num = axor
i = 0
while i < la:
    if (num >> (la - 1 - i)) & 1:
        if not exist[la - 1 - i]:
            print(-1)
            exit()
        ans += 1
        if la - 1 - i == 0:
            break
        num ^= (1 << (la - 1 - i)) - 1
    i += 1

print(ans)