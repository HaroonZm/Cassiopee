from sys import stdin
from functools import reduce
from operator import mul

MOD = 10**9 + 7

def input_int():
    return int(stdin.readline())

def input_ints():
    return map(int, stdin.readline().split())

n = input_int()
a = list(input_ints())

# Pré-calcul des clés valides pour c via set-compréhension
c = {abs(n - 1 - i - i): 0 for i in range(n // 2 + 1)}

for x in a:
    if x not in c or c[x] == 2:
        print(0)
        exit()
    c[x] += 1

try:
    cnt = reduce(lambda acc, kv: acc * kv[1] % MOD if (kv[1] == 2 or kv[0] == 0) else (_ for _ in ()).throw(ZeroDivisionError),
                 c.items(), 1)
except ZeroDivisionError:
    print(0)
    exit()

print(cnt)