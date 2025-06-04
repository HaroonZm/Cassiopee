import sys
import statistics
input = sys.stdin.readline

n = int(input())
p = list(map(int, input().split()))
counter = 0
i = 1
while i < n - 1:
    a = p[i-1]
    b = p[i]
    c = p[i+1]
    if (a <= b <= c) or (c <= b <= a):
        counter += 1
    i += 1
print(counter)