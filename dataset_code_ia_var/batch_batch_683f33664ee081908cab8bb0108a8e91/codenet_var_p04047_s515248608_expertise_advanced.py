from itertools import islice

k = int(raw_input())
a = sorted(map(int, raw_input().split()))
print(sum(min(pair) for pair in zip(islice(a, 0, 2*k, 2), islice(a, 1, 2*k, 2))))