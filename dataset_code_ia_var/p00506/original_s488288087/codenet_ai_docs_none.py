n = int(input())
values = list(map(int, input().split()))
minv = min(values) + 1
print(1)
i = 2
ng_value = [1] * minv
while i < minv:
    if not 0 in [1 if values[k] % i == 0 else 0 for k in range(n)]:
        print(i)
    else:
        for j in range(i, minv, i):
            ng_value[j] = 0
    b = True
    for j in range(i + 1, minv):
        if ng_value[j]:
            i = j
            b = False
            break
    if b:
        break