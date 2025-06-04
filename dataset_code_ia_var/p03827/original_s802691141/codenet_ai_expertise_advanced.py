from itertools import accumulate

n = int(input())
s = input()

deltas = (1 if c == 'I' else -1 for c in s)
prefix_sums = accumulate(deltas)
print(max(0, max(prefix_sums, default=0)))