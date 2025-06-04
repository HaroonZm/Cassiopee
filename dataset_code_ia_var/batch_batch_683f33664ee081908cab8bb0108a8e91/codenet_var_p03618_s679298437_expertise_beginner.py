import sys

A = sys.stdin.readline().strip()

count = {}
for c in A:
    if c in count:
        count[c] += 1
    else:
        count[c] = 1

total = 0
for c in count:
    total += count[c]

answer = 0
for c in count:
    total -= count[c]
    answer += count[c] * total

print(answer + 1)