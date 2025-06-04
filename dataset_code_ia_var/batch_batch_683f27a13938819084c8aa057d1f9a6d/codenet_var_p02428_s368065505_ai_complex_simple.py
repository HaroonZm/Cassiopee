import functools
import operator

n = int(input())
temp0 = input().split()
k, *rest = map(int, temp0)
T = rest

m = 1 << n

for i in range(m):
    temp = list(map(lambda x: (i >> x) & 1, range(n)))
    flag = all(map(lambda t: operator.getitem(temp, t), T))
    if flag:
        temp2 = list(filter(lambda x: (i >> x) & 1, range(n)))
        print(i, end="")
        print(":" + ("" if i == 0 else " " + " ".join(map(str, temp2))))