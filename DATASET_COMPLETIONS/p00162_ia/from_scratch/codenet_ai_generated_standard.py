import sys
from bisect import bisect_left, bisect_right

def generate_hamming(max_val):
    hamming = [1]
    i2 = i3 = i5 = 0
    while True:
        next2 = hamming[i2] * 2
        next3 = hamming[i3] * 3
        next5 = hamming[i5] * 5
        nxt = min(next2, next3, next5)
        if nxt > max_val:
            break
        hamming.append(nxt)
        if nxt == next2: i2 += 1
        if nxt == next3: i3 += 1
        if nxt == next5: i5 += 1
    return hamming

hamming_nums = generate_hamming(10**6)
input = sys.stdin.read().strip().split('\n')
for line in input:
    if line == '0':
        break
    m,n = map(int,line.split())
    left = bisect_left(hamming_nums, m)
    right = bisect_right(hamming_nums, n)
    print(right - left)