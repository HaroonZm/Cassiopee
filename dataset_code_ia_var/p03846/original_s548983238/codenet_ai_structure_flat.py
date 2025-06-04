n = int(input())
response_list = [int(v) for v in input().split()]
ans = 0
mod = 10**9 + 7
if n % 2 == 0:
    right_list = []
    i = 0
    while i < n:
        right_list.append(2 * (i // 2 + 1) - 1)
        i += 1
else:
    right_list = []
    i = 0
    while i < n:
        right_list.append(2 * ((i + 1) // 2))
        i += 1
sorted_list = sorted(response_list)
ok = True
i = 0
while i < n:
    if sorted_list[i] != right_list[i]:
        ok = False
        break
    i += 1
if ok:
    if n % 2 == 0:
        ans = 1
        i = 0
        while i < n // 2:
            ans = (ans * 2) % mod
            i += 1
    else:
        ans = 1
        i = 0
        while i < (n - 1) // 2:
            ans = (ans * 2) % mod
            i += 1
print(ans)