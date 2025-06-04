from collections import Counter
from itertools import accumulate
import sys
M = 10**5 + 2
prime = [0]*M
for i in range(2, M):
    if prime[i]:
        continue
    for j in range(i, M, i):
        if not prime[j]:
            prime[j] = i
def pd(x):
    C = Counter()
    while x > 1:
        C[prime[x]] += 1
        x //= prime[x]
    return C
def check(x):
    C = pd(x)
    if len(C) > 2:
        return True
    if len(C) == 1:
        if list(C.values())[0] >= 4:
            return True
        return False
    if all(1 == a for a in C.values()):
        return False
    return True
M -= 1
table = [0, 0] + [check(x) for x in range(2, M)] 
table = list(accumulate(table))
for _ in range(int(input())):
    q = int(sys.stdin.readline())
    print(table[q])