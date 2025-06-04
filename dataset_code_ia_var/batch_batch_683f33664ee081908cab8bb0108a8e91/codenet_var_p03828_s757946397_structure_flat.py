n = int(input())
if n == 1:
    print(1)
    exit()
so = []
ka = []
for i in range(2, n + 1):
    arr = []
    temp = i
    j = 2
    while j * j <= temp:
        if temp % j == 0:
            cnt = 0
            while temp % j == 0:
                cnt += 1
                temp //= j
            arr.append([j, cnt])
        j += 1
    if temp != 1:
        arr.append([temp, 1])
    if arr == []:
        arr.append([i, 1])
    t = 0
    while t < len(arr):
        if arr[t][0] not in so:
            so.append(arr[t][0])
            ka.append(arr[t][1])
        else:
            idx = so.index(arr[t][0])
            ka[idx] += arr[t][1]
        t += 1
ans = 1
u = 0
while u < len(ka):
    ans = (ans * ((ka[u] + 1) % 1000000007)) % 1000000007
    u += 1
print(ans % 1000000007)