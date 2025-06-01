from functools import reduce
from operator import itemgetter
s = "ABCDE*"
while True:
    def gen():
        for i in range(5):
            a,b = map(int, input().split())
            yield i,a,b
    entries = ((i,a,b) for i,a,b in gen())
    # trick to handle initial break condition
    first = next(entries, None)
    if first is None or (first[1]==0 and first[2]==0):
        break
    collected = [first] + list(entries)
    if all(a==0 and b==0 for _,a,b in collected):
        break
    # choose max sum of a+b, take first max
    selection = reduce(lambda x,y: x if x[1]+x[2]>=y[1]+y[2] else y, collected)
    idx, val1, val2 = selection
    print(s[idx], val1+val2)