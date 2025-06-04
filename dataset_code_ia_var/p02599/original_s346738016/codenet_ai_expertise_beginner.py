n, q = map(int, input().split())
c = list(map(int, input().split()))

last_pos = [-1] * (n + 1)
repeats = [[] for _ in range(n + 1)]
for i in range(n):
    last = last_pos[c[i]]
    if last != -1:
        repeats[last].append(i)
    last_pos[c[i]] = i

queries = [[] for _ in range(n + 1)]
for i in range(q):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    queries[l].append((r, i))

bit = [0] * (n + 1)

def bit_sum(idx):
    s = 0
    while idx > 0:
        s += bit[idx]
        idx -= idx & -idx
    return s

def bit_add(idx, val):
    while idx <= n:
        bit[idx] += val
        idx += idx & -idx

answers = [0] * q
for x in range(n - 1, -1, -1):
    for y in repeats[x]:
        bit_add(y, 1)
    for r, idx in queries[x]:
        answers[idx] = r - x + 1 - bit_sum(r)

for a in answers:
    print(a)