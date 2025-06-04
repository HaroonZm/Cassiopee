K, N = (int(x) for x in input().split())
A = list(map(int, input().split()))

def get_diffs(lst, k):
    result = []
    for idx in range(len(lst)-1):
        result += [lst[idx+1] - lst[idx]]
    result.append(k - lst[-1] + lst[0])
    return result

from functools import reduce

d = get_diffs(A, K)
sorted_d = sorted(d)

res = 0
for elem in range(N-1):
    res = res + sorted_d[elem]

print(res)