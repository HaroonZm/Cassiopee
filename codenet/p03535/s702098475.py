N = int(input())
D = [int(d) for d in input().split()]
Dcount = [0] * 13

for i in range(13):
    Dcount[i] = D.count(i)
if Dcount[0] > 0 or Dcount[12] > 1: print(0)
else:
    for i in Dcount[1:12]:
        if i >= 3:
            print(0)
            break
    else:
        base = [0, 24]
        if Dcount[12] == 1: base.append(12)
        Single = []
        for i in range(1, 12):
            if Dcount[i] == 2:
                base.append(i)
                base.append(24-i)
            elif Dcount[i] == 1:
                Single.append(i)
        lensingle = len(Single)
        minmax = 0
        for i in range(2**lensingle):
            Clock = base.copy()
            bit = format(i, "b").zfill(lensingle)
            for j in range(lensingle):
                if bit[j] == "0": Clock.append(Single[j])
                else: Clock.append(24 - Single[j])
            Clock.sort()
            minsub = 24
            for j in range(1, len(Clock)):
                minsub = min(minsub, Clock[j] - Clock[j-1])
            minmax = max(minmax, minsub)
        print(minmax)