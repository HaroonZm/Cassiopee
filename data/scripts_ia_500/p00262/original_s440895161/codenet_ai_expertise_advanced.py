from math import isqrt

def is_sankaku(v):
    x = isqrt(8*v + 1)
    return x * x == 8*v + 1 and (x - 1) % 2 == 0

def check(lst):
    return all(v == i + 1 for i, v in enumerate(lst))

while True:
    N = int(input())
    if N == 0:
        break

    lst = list(map(int, input().split()))
    if not is_sankaku(sum(lst)):
        print(-1)
        continue

    result = -1
    for count in range(10000):
        if check(lst):
            result = count
            break
        spam = len(lst)
        lst = [x - 1 for x in lst if x > 1]  # x > 1 since x-1 > 0
        lst.append(spam)

    print(result)