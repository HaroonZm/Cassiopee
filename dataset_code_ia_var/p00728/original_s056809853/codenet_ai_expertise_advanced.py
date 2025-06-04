from itertools import islice, count
from collections import Counter

while True:
    n = int(input())
    if n == 0:
        break
    lst = [int(input()) for _ in range(n)]
    ctr = Counter(lst)
    mx, mn = max(lst), min(lst)
    n2 = n - 2
    filtered = [x for x in lst if x != mx and x != mn]
    sum_vals = sum(filtered)
    if ctr[mx] >= 2:
        sum_vals += mx
    elif ctr[mn] >= 2:
        sum_vals += mn
    print(sum_vals // n2)