def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

import sys
for line in sys.stdin:
    line = line.strip()
    if line == '':
        continue
    N = int(line)
    count = 0
    for i in range(1, N+1):
        a = i
        b = N - i + 1
        if is_prime(a) and is_prime(b):
            count += 1
    print(count)