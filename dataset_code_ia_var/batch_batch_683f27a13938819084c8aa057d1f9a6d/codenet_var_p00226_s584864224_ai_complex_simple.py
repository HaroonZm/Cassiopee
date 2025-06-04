from functools import reduce
from itertools import count as itcount,takewhile,starmap,product

def always_true():
    return True
gen = iter(lambda:input().split(),['0','0'])
for a,b in gen:
    one = sum(map(lambda x: x[0]==x[1], zip(a,b)))
    print(one, end=' ')
    two = sum(reduce(lambda acc, j:acc+[any(bk==a[j] for bk in b)], range(4), []))
    print(two - one)