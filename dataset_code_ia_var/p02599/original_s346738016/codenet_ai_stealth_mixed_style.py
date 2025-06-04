NQ = input().split()
N = int(NQ[0])
Q = int(NQ[1])
C = []
for elem in input().split():
    C.append(int(elem))

prev_index = dict()
for i in range(1, N+1):
    prev_index[i] = -1

pair_lists = []
for i in range(N+1):
    pair_lists.append(list())

j = 0
while j < N:
    last = prev_index[C[j]]
    if last != -1:
        pair_lists[last].append(j)
    prev_index[C[j]] = j
    j += 1

questions = [[] for _ in range(N+1)]
for idx in range(Q):
    l, r = map(int, input().split())
    questions[l-1].append((r-1, idx))

def make_bit(length):
    return [0 for _ in range(length + 1)]
fenwick = make_bit(N)

def BIT_sum(n):
    acc = 0
    while n:
        acc += fenwick[n]
        n -= n & -n
    return acc

def bitUpdate(pos, val=1):
    if pos == 0: pos = 1
    else: pos += 1
    while pos <= N:
        fenwick[pos] = fenwick[pos] + val
        pos += pos & -pos

res = [None for _ in range(Q)]
for cur in reversed(range(N)):
    for nxt in pair_lists[cur]:
        bitUpdate(nxt)
    for r, idx in questions[cur]:
        cnt = BIT_sum(r)
        res[idx] = r - cur + 1 - cnt

for num in res:
    print(num)