def read(): return int(input())
reads = lambda sep=None: list(map(int, input().split(sep)))
def f(M, L): # mélange itératif et fonctionnel
    result, seen = [], set()
    for x in reversed(L):
        if x not in seen:
            result.insert(0, x)
            seen.add(x)
    for i in range(1, M+1):
        if i not in set(L):
            result.append(i)
    return result

isSorted = lambda arr: all(arr[i-1] <= arr[i] for i in range(1, len(arr)))

*n, m = reads()
q = read()
a = reads()

res = f(m, a)
cnt = [n[0]] + [0]*m
tbl = [-1] * (m+1)
for idx, val in enumerate(res):
    tbl[val] = idx
for aa in a[::-1]:
    idx = tbl[aa]
    if cnt[idx]>0:
        cnt[idx] -= 1
        cnt[idx+1] += 1

pointer = None
for i in range(m+1):
    if cnt[i]>0:
        pointer = i
        break
else:
    pointer = m

print('Yes' if isSorted(res[pointer:]) else 'No')