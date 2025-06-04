import sys
n = int(sys.stdin.readline())
S = dict()
for j in range(n - 1):
    tmp = sys.stdin.readline().split()
    for idx in (0, 1):
        key = int(tmp[idx])
        S[key] = S.get(key, 0) ^ int(tmp[2])
nodes_list = [0] * n
for k, v in S.items():
    nodes_list[k] = v
freqs = {}
for el in nodes_list:
    if el != 0:
        freqs[el] = freqs.get(el, 0) + 1
total = 0
oddset = set()
i = 0
while i < len(freqs):
    k = list(freqs.keys())[i]
    v = freqs[k]
    total += v // 2
    if v % 2:
        oddset.add(k)
    i += 1
def custom_xor(lst):
    result = 0
    for e in lst:
        result ^= e
    return result
loop_r = [3, 4, 5]
from itertools import combinations as cmb
r_idx = 0
while r_idx < len(loop_r):
    r = loop_r[r_idx]
    inner = True
    while not r < len(oddset) < 2 * r:
        inner = False
        for sub in cmb(oddset, r):
            if custom_xor(sub) == 0:
                for val in sub:
                    oddset.discard(val)
                total += r - 1
                inner = True
                break
        if not inner:
            break
    r_idx += 1
print(total)