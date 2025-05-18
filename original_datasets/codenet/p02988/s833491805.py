import sys
import statistics
input = sys.stdin.readline

n = int(input())
p = list(map(int, input().split()))
counter = 0
for i in range(1, n-1):
    lis = (p[i-1], p[i], p[i+1])
    mid = statistics.median(lis)
    if p[i] == mid:
        counter += 1

print(counter)