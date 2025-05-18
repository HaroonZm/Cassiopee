N = int(input())
for i in range(N):
    a, b = map(int, input().split())
    print(a % b if a % b else b)