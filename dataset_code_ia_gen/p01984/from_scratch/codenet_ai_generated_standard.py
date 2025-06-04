import sys
import bisect

MAXLEN = 19  # 10**18 約10^19未満のため余裕をもって19桁

singka_nums = []

def dfs(num, d1, d2, length, max_len):
    if length > max_len:
        return
    if length > 0:
        singka_nums.append(num)
    dfs(num*10 + d1, d1, d2, length+1, max_len)
    dfs(num*10 + d2, d1, d2, length+1, max_len)

digits = [str(i) for i in range(1,10)]
all_nums = set()

for i in range(1,10):
    for j in range(0,10):
        if i == j:
            continue
        d1 = i
        d2 = j
        singka_nums = []
        dfs(0, d1, d2, 0, MAXLEN)
        for v in singka_nums:
            if v > 0:
                all_nums.add(v)

all_nums = sorted(all_nums)

input = sys.stdin.readline
while True:
    line = input()
    if not line:
        break
    n = line.strip()
    if n == '0':
        break
    N = int(n)
    print(all_nums[N-1])