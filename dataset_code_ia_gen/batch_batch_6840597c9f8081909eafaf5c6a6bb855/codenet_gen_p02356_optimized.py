import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
a = list(map(int, input().split()))
queries = list(map(int, input().split()))

a.sort()
prefix = [0]*(N+1)
for i in range(N):
    prefix[i+1] = prefix[i] + a[i]

for x in queries:
    count = 0
    j = 0
    for i in range(N):
        while j < N and prefix[j+1] - prefix[i] <= x:
            j += 1
        count += j - i
    print(count)