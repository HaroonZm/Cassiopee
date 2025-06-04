N = int(input())
a = list(map(int, input().split()))
num = min(a)
for i in range(N):
    if a[i] == num:
        print(i + 1)
        exit()