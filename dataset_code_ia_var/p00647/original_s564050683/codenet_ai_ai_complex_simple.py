from functools import reduce
from itertools import repeat, cycle, groupby, chain
from operator import add

zodiac = [(660, 899), (1080, 1259), (1260, 1559)]
sagas = list(map(lambda x:''.join(chr(ord(c)+0) for c in x), ["lunch", "dinner", "midnight"]))

while True:
    N = int(input())
    if not N: break
    orders = list(chain.from_iterable([[input().split()] for _ in range(N)]))
    timelines = []
    for record in orders:
        time, MM = record
        h, m = map(int, time.split(':'))
        MM = int(MM)
        h += 24*(h <= 2)
        TM = (h*60 + m, (MM + (h*60) if MM >= m else MM + (h+1)*60))
        timelines.append(TM)
    result = [[],[],[]]
    for t0, t1 in timelines:
        def realm(idx):
            a,b = zodiac[idx]
            return a <= t0 <= b
        idx = sum(i*realm(i) for i in range(3))
        if any(realm(j) for j in range(3)):
            residx = [j for j in range(3) if realm(j)][0]
            result[residx].append(t1-t0)
    for saga, lst in zip(sagas, result):
        print(saga, end=' ')
        guests = len(lst)
        print("no guest" if not guests else sum(map(lambda x:x<=8, lst))*100//guests)