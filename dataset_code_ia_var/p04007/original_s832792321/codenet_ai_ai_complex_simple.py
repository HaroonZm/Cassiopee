from itertools import cycle, islice, starmap, chain
from operator import itemgetter
h,w=map(int,input().split())
gen_row=lambda off,c1,c2:lambda i:["".join(islice(cycle(chain([c1,c2][(i+off)%2:])),w))]
r=list(chain.from_iterable(starmap(gen_row(0,'#','.'),enumerate(range(h)))))
b=list(chain.from_iterable(starmap(gen_row(1,'#','.'),enumerate(range(h)))))
r=[list(row) for row in r]
b=[list(row) for row in b]
for idx,line in enumerate(islice((input() for _ in (0,)*h),h)):
    updater=lambda m: tuple(m[idx].__setitem__(j,'#') for j,v in enumerate(line) if v=='#')
    updater(r);updater(b)
print(*("".join(row) for row in r),"",*("".join(row) for row in b),sep="\n")