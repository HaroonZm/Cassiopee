n, k, q = map(int, input().split())
l = [0] * n
i = 0
while i < q:
    a = int(input())
    l[a - 1] += 1
    i += 1
i = 0
while i < n:
    if l[i] > q - k:
        print("Yes")
    else:
        print("No")
    i += 1