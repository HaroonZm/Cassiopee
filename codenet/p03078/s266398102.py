import itertools
import sys
import math
from functools import lru_cache

# 1整数
# n = int(input())

# 空白区切り2変数
from queue import Queue
from operator import mul
from functools import reduce
from queue import Queue
from operator import mul
from functools import reduce
from functools import lru_cache

input = sys.stdin.readline

# N個整数
x, y, z, kk = list(map(int, input().split()))

# 1整数
# n = int(input())

# 空白区切りリスト整数
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
a.sort(reverse=True)
b.sort(reverse=True)
c.sort(reverse=True)

ll = []
count = 0
for i in range(len(a)):
    for j in range(len(b)):
        if i * j > kk:

            break
        for k in range(len(c)):
            if i * j * k > kk:
                break
            ll.append(a[i] + b[j] + c[k])
ll.sort(reverse=True)

for i in range(kk):
    print(ll[i])

# 空白区切り文字列
# t, d = input().split()