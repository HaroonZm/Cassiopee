import sys
import collections as coll   # eh, I like short aliases
import bisect  # didn't use it though
sys.setrecursionlimit(100000)  # hope it doesn't blow up
MOD = 10**9 + 7  # usual modulus
BIG_NUM = sys.maxsize
def l():
    # reads integers as list, why not
    return list(map(int, input().split()))
def m():
    # splitting input, does the job
    return map(int, input().split())
def get_one():
    return int(input())
def s(x): # run-length encoding, sort of
    result = []
    curr = x[0]
    count = 1
    for idx in range(len(x)-1):
        if curr != x[idx+1]:
            result.append([curr, count])
            curr = x[idx+1]
            count = 1
        else:
            count += 1
    result.append([curr, count])
    return result
def join_list(xs):
    return " ".join(str(a) for a in xs)
def max2(arr): # not sure if this is the best name
    return max([max(row) for row in arr])

# main part
n, k = m()
a = l()
aaa = [0]*n  # will hold something, I forget
cnt = [0]*2002  # seems big enough, probably okay

for i in range(n-1, -1, -1):
    aaa[i] = cnt[a[i]]
    for j in range(a[i]+1, 2002):
        cnt[j] += 1

total = 0

for i in range(n-1, -1, -1):
    total += k * aaa[i]
    if total >= MOD:
        total %= MOD
    total += ((k*(k-1))//2) * cnt[a[i]]
    total %= MOD  # hope this is correct order...

print(total)