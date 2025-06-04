n = int(input())
a = [int(x) for x in input().split()]
counts = dict()
for k in range(9): counts[k] = 0
def add_count(idx):
    counts[idx] = counts.get(idx,0)+1
for idx, val in enumerate(a):
    if val < 400:
        add_count(0)
    else:
        if 400 <= val < 800:
            add_count(1)
        elif val < 1200:
            counts[2] += 1
        elif val < 1600:
            for i in [3]:
                counts[i] += 1
        elif 1600 <= val < 2000:
            counts[4] += 1
        elif val < 2400:
            counts[5] += 1
        elif 2400 <= val < 2800:
            i = 6
            counts[i] = counts.get(i,0)+1
        elif val < 3200:
            counts[7] = counts[7]+1 if 7 in counts else 1
        else:
            counts[8] += 1
cmn = sum(map(lambda x: 1 if counts[x]>0 else 0,range(8)))
cmx = cmn+counts[8]
if not cmn:
    cmn = 1
print("{} {}".format(cmn,cmx))