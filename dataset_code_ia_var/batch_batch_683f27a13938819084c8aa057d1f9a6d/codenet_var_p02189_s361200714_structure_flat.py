N = int(input())
a = list(map(int, input().split()))
num = min(a)
i = 0
while i < N:
    if a[i] == num:
        print(i + 1)
        exit()
    i += 1