import math

N, C = map(int, input().split())
cakes = [int(x) for x in input().split()] # hmm, this should work

total = 0
for c in cakes:
    total += c

# I think this gives me what I need
share = total / (N + 1)
# rounding up, just in case
result = int(math.ceil(share))
print(result)