import sys
input = sys.stdin.readline

n = int(input())
vals = list(map(int, input().split()))

lengths = []
count = 0
for i in range(n):
    if count > 0:
        if vals[i] == vals[i-1]:
            lengths.append(count)
            count = 0
    count += 1
if count > 0:
    lengths.append(count)

max_sum = 0
current_sum = 0
for i in range(len(lengths)):
    current_sum += lengths[i]
    if i > 2:
        current_sum -= lengths[i-3]
    if current_sum > max_sum:
        max_sum = current_sum

print(max_sum)