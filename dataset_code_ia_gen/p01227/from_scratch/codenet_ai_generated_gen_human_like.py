import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    houses = list(map(int, input().split()))
    if k >= n:
        print(0)
        continue
    distances = []
    for i in range(n-1):
        distances.append(houses[i+1] - houses[i])
    distances.sort(reverse=True)
    # Remove the k-1 largest gaps to form k segments
    answer = sum(distances[k-1:])
    print(answer)