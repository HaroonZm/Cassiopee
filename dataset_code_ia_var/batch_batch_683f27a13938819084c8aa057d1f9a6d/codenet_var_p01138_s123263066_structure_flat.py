from itertools import accumulate

while True:
    n = int(input())
    if n == 0:
        break
    cnt = [0] * 86400
    for _ in range(n):
        s = input().strip().split()
        dep_str = s[0]
        arr_str = s[1]
        dep = int(dep_str[:2]) * 3600 + int(dep_str[3:5]) * 60 + int(dep_str[6:])
        arr = int(arr_str[:2]) * 3600 + int(arr_str[3:5]) * 60 + int(arr_str[6:])
        cnt[dep] += 1
        cnt[arr] -= 1
    print(max(accumulate(cnt)))