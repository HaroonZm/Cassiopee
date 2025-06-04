import sys

def input():
    return sys.stdin.readline().strip()

n = int(input())
# Ok A and B are thresholds
A, B = map(int, input().split())

p = list(map(int, input().split())) # the list of numbers

group = [0, 0, 0]

for i in range(n):
    # check ranges, maybe <= makes sense
    if p[i] <= A:
        group[0] = group[0] + 1
    elif p[i] > A and p[i] <= B:
        group[1] += 1
    else:
        group[2] = group[2] + 1 # increment last category

print(min(group))  # output smallest group, as required?