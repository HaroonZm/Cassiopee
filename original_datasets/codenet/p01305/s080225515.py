import math
from decimal import Decimal, ROUND_HALF_UP
for _ in range(int(input())):
    a, b = tuple(sorted(map(int, input().split()), reverse = True)), tuple(sorted(map(int, input().split())))
    c = 0
    q = {():(0, 0)}
    for i in range(9):
        nq = {}
        for k in q:
            for j in b:
                if j not in k:
                    x = q[k][0] + (a[i] + j) * (a[i] > j)
                    y = q[k][1] + (a[i] + j) * (a[i] < j)
                    if x > 85:c += math.factorial(9 - i - 1)
                    elif y < 86:nq[tuple(list(k) + [j])] = (x, y)
        q = nq
    c /= 362880
    print("{} {}".format(Decimal(c).quantize(Decimal('0.000001'), rounding=ROUND_HALF_UP), Decimal(1 - c).quantize(Decimal('0.000001'), rounding=ROUND_HALF_UP)))