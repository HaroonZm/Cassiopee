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
n, k = list(map(int, input().split()))

s = input() + '2'

# 1整数
# n = int(input())

ret = 0

##この文字の次の0まで示す
def next0(l: int):
    if l >= n:
        return l
    l += 1
    while s[l] != '2' and s[l] != '0':
        l += 1
    return min(l, n)

##この文字の次の1まで示す
def next1(l: int):
    if l >= n:
        return l
    l += 1
    while s[l] != '2' and s[l] != '1':
        l += 1
    return min(l, n)

start = 0
end = 0
ret = 0
# まずendをKこ進める
end = next0(end)
for i in range(k):
    end = next1(end)
    end = next0(end)

ret = end - start
#print(start, end, ret)

while end < n:
    start = next1(next0(start))
    end = next0(next1(end))
    ret = max(ret, end - start)
    #print(start, end, ret)
print(ret)