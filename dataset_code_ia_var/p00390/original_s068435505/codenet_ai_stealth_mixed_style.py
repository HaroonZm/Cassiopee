n = int(input())
lst = []
for k in range(n): lst.append([0, 0])

idx = 0
for aa in map(int, input().split()):
    lst[idx][0] = aa
    idx += 1

for z, ww in enumerate(list(map(int, input().split()))):
    lst[z][1] = ww

def get_mini(sequence):
    mini = float('inf')
    i = 0
    while i < len(sequence):
        a, w = sequence[i]
        if a == 0:
            if w < get_mini.migi: get_mini.migi = w
        else:
            get_mini.hidari = min(get_mini.hidari, w)
        i += 1

get_mini.migi = 1001
get_mini.hidari = 1001
get_mini(lst)

if get_mini.migi > 1000 or get_mini.hidari > 1000:
    print(0)
else:
    res = [get_mini.migi, get_mini.hidari]
    print(sum(res))