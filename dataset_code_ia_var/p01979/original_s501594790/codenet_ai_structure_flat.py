from collections import deque
import itertools as it
import sys
import math

sys.setrecursionlimit(1000000)

INF = 10 ** 18
MOD = 10 ** 9 + 7

N = input()
S = ['?'] * 20

stack = []
stack.append( (S[:], 0, 0) )
res = 0

while stack:
    S_now, index, cnt = stack.pop()
    if index == 20:
        if cnt == 0:
            continue
        ans = 0
        S_ = list(S_now)
        for i in range(20):
            if S_[i] != '?':
                continue
            for j in range(10):
                S_[i] = str(j)
                check_num = int(''.join(S_).replace('?', '9'))
                if check_num > int(N):
                    break
                else:
                    ans += 10 ** S_.count('?')
            S_[i] = '?'
        ans *= (-1) ** (cnt + 1)
        res += ans
        continue
    stack.append((S_now[:], index + 1, cnt))
    if index <= 16:
        S_ = list(S_now)
        S_[index] = '5'
        S_[index + 1] = '1'
        S_[index + 3] = '3'
        stack.append((S_, index + 4, cnt + 1))

print(res)