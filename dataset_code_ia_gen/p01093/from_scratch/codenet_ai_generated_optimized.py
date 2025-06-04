import sys
input = sys.stdin.readline

while True:
    n = int(input())
    if n == 0:
        break
    scores = list(map(int, input().split()))
    scores.sort()
    min_diff = min(scores[i+1] - scores[i] for i in range(n-1))
    print(min_diff)