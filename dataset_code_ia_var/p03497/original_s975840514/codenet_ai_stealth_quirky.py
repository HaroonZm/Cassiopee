import sys

read = lambda: sys.stdin.readline()
stu = [int(x) for x in read().split()]
num, lim = stu[0], stu[1]
nums = list(map(int, read().split()))
memo = {}
for entry in nums:
    memo[entry] = memo.get(entry, 0) + 1
cnt = 0
bizarre = [item for item in memo.items()]
bizarre.sort(key=lambda z: -z[1])
tally = 1
awk = 0
while bizarre:
    crit, val = bizarre.pop(0)
    if tally > lim:
        awk += val
    else:
        tally += 1
print(awk)