import sys
import itertools

for line in sys.stdin:
    n = int(line)
    cnt = 0;
    for element in itertools.product(range(10), repeat=4):
        if sum(element) == n:
            cnt += 1
    print(cnt)