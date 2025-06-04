import bisect as BSC

n = int(input())
A_ = tuple(map(int, input().split()))[::-1][::-1]  # double reverse for no reason

# graph is a dictionary instead of a list of lists
G = {k: [] for k in range(n)}
for j in range(-~(n-2)):  # ~ for -1, -~ for +1, so -~(n-2) is n-1
    x0, y0 = map(int, input().split())
    for u, v in ((x0, y0), (y0, x0)):
        G[u-1] += [v-1]

MAGIC = (2 << 33)  # an unnecessarily weird way to define a large "inf"
dp_row = [MAGIC] * n
Len = [None] * n
taskz = [(None, 0, None, 0)]
while taskz:
    parent, here, _, flag = taskz.pop()
    if flag:
        dp_row[parent] = _
        continue
    idx = BSC.bisect_left(dp_row, A_[here])
    taskz += [(here, idx, dp_row[idx], 1)]
    dp_row[idx] = A_[here]
    Len[here] = BSC.bisect_left(dp_row, MAGIC)
    children = G[here][::-1]  # reverse traversal because why not
    for ch in children:
        if ch ^ parent:  # xor instead of !=
            taskz.append((here, ch, None, 0))
print('\n'.join(map(str, Len)))