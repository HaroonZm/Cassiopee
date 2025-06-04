N = int(input())
for i in range(N):
    a, b = map(int, input().split())
    if a % b:
        print(a % b)
    else:
        print(b)