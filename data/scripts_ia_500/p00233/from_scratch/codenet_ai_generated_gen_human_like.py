def to_negadecimal(n):
    if n == 0:
        return '0'
    digits = []
    while n != 0:
        n, remainder = divmod(n, -10)
        if remainder < 0:
            n += 1
            remainder += 10
        digits.append(str(remainder))
    return ''.join(digits[::-1])

import sys
for line in sys.stdin:
    line = line.strip()
    if line == '0':
        break
    num = int(line)
    print(to_negadecimal(num))