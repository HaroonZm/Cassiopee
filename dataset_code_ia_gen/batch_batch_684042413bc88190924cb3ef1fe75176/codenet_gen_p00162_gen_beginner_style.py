import sys

def is_hamming_number(x):
    if x == 1:
        return True
    for p in [2, 3, 5]:
        while x % p == 0:
            x //= p
    return x == 1

for line in sys.stdin:
    line = line.strip()
    if line == "0":
        break
    m, n = map(int, line.split())
    count = 0
    for num in range(m, n + 1):
        if is_hamming_number(num):
            count += 1
    print(count)