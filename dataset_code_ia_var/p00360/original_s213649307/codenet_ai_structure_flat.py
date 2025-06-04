from bisect import bisect_left as bl

s = list(map(ord, list(input())))
k = int(input())
used = []
used_index = []
pos_dict = {}
as_a = ord("a")
as_z = ord("z")
for i, v in enumerate(s):
    if v in pos_dict:
        pos_dict[v].append(i)
    else:
        pos_dict[v] = [i]
keys = sorted(pos_dict.keys())
for key in keys:
    pos_dict[key].reverse()
while k:
    broke = False
    for jj in range(len(keys)):
        key = keys[jj]
        init = pos_dict[key][-1]
        pre_used = bl(used_index, init)
        cost = init - pre_used
        if cost <= k:
            k -= cost
            used.append(key)
            ins = bl(used_index, init)
            used_index.insert(ins, init)
            pos_dict[key].pop()
            if not pos_dict[key]:
                keys.pop(jj)
            broke = True
            break
    if not broke:
        break
used_index.sort(reverse=True)
for i in used_index:
    s.pop(i)
print("".join(map(chr, used + s)))