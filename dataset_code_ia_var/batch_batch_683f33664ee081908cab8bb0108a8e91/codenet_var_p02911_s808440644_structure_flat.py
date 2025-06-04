n, k, q = map(int, input().split())
pnt = [0] * n
i = 0
while i < q:
    j = int(input())
    pnt[j - 1] += 1
    i += 1
i = 0
while i < n:
    if pnt[i] + k - q > 0:
        print("Yes")
    else:
        print("No")
    i += 1