n, k, q = map(int, input().split())
a = list(map(int, input().split()))
ans = 10**9

for i in a:
    temp_list = []
    group = []
    group_len = 0
    for num in a + [-1]:
        if num < i:
            if group_len >= k:
                group.sort()
                for x in range(group_len - k + 1):
                    temp_list.append(group[x])
            group = []
            group_len = 0
        else:
            group.append(num)
            group_len += 1
    if len(temp_list) < q:
        continue
    temp_list.sort()
    diff = temp_list[q-1] - i
    if diff < ans:
        ans = diff

print(ans)