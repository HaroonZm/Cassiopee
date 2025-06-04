n = int(input())
lst = list(map(int, input().split()))
lst2 = [0] * n
i = 0
while i < n:
    x = lst[i]
    lst2[x - 1] = i + 1
    i += 1
i = 0
while i < n:
    if i != n - 1:
        print(lst2[i], end=' ')
    else:
        print(lst2[i])
    i += 1