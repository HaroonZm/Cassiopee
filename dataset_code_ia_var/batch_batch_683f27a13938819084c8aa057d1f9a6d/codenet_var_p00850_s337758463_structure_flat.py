from collections import deque

d = deque([(0, 1, [1])])
num_list = [float('inf')] * 2001
num_list[1] = 0

while d:
    times, now, nums = d.popleft()
    for i in nums:
        tmp = i + now
        if tmp > 2000:
            continue
        if num_list[tmp] >= times:
            num_list[tmp] = times
            d.append((times + 1, tmp, nums + [tmp]))
    for i in nums:
        tmp = max(now - i, i - now)
        if tmp <= 0:
            continue
        if num_list[tmp] >= times:
            num_list[tmp] = times
            d.append((times + 1, tmp, nums + [tmp]))

ans = []
while True:
    a = int(input())
    if not a:
        break
    if a == 1:
        ans.append(num_list[a])
    else:
        ans.append(num_list[a] + 1)

for i in ans:
    print(i)