import sys
import math

for line in sys.stdin:
    b = line.strip()
    if b == '0':
        break
    b = int(b)
    max_len = 1
    start_floor = b
    # The length of consecutive floors (k) satisfies k(k+1)/2 <= b + (k-1)*x for some x
    # We try all k from largest possible down to 1
    max_k = int((2*b)**0.5) + 2
    for k in range(max_k, 0, -1):
        # We need to solve for x (lowest floor)
        # sum of k floors starting from x:
        # sum = k*(2x + k -1)/2 = b
        # => 2b = k*(2x + k -1)
        # => 2x + k -1 = 2b/k
        # => 2x = 2b/k - (k-1)
        # x = (2b/k - (k-1)) / 2
        if 2*b % k != 0:
            continue
        val = 2*b//k - (k-1)
        if val <= 0 or val % 2 != 0:
            continue
        x = val // 2
        if x >= 1:
            max_len = k
            start_floor = x
            break
    print(start_floor, max_len)