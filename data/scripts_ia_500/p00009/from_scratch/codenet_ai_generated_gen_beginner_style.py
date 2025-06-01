def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

import sys

for line in sys.stdin:
    n = line.strip()
    if not n.isdigit():
        continue
    n = int(n)
    count = 0
    for i in range(2, n+1):
        if is_prime(i):
            count += 1
    print(count)