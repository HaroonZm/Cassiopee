from sys import stdin

for line in stdin:
    n = int(line)
    print(' '.join(str(1 << i) for i in range(10) if n & (1 << i)))