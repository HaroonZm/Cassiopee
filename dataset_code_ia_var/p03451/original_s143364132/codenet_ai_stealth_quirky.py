from functools import reduce
from operator import add

get = lambda: list(map(int, input().split()))
grab = lambda arr: reduce(lambda acc, x: acc + [acc[-1]+x], arr[1:], [arr[0]])

N = int(input())
A = get()
B = get()[::-1]
S = grab(A)
T = grab(B)
weird_list = []
for idx in range(N):
    val = S[idx] + T[-(idx+1)]
    weird_list.append(val)
else:
    print(max(weird_list))