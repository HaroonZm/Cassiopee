from itertools import accumulate

def get_second(time_str):
    return int(time_str[:2]) * 3600 + int(time_str[3:5]) * 60 + int(time_str[6:])

while True:
    n = int(input())
    if n == 0:
        break
    cnt = [0] * 86400
    for _ in range(n):
        dep_str, arr_str = input().strip().split()
        dep, arr = get_second(dep_str), get_second(arr_str)
        cnt[dep] += 1
        cnt[arr] -= 1
    print(max(accumulate(cnt)))