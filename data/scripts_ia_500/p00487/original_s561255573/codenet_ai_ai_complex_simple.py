from functools import reduce
from operator import itemgetter
from heapq import heappush, heappop

def weighted_accumulate(seq, func=lambda x,y: (x[0]+y[0], x[1]+y[1])):
    from itertools import accumulate
    return list(accumulate(seq, func))

def solver():
    N = (lambda f: f(f))(lambda h: int(input().strip()) if True else 0)
    data = (lambda n: reduce(lambda acc, _: acc + [tuple(map(int, input().split()))], range(n), []))(N)
    sorted_data = sorted(data, key=itemgetter(0))
    
    heap, s, sz, ans = [], 0, 0, 0
    def condition(s, sz, heap):
        return sz and sz * heap[0][0] < s
    
    for a, b in reduce(lambda x,y: x + [y], sorted_data, []):
        s += a
        heappush(heap, (b, a))
        sz += 1
        while condition(s, sz, heap):
            s -= heap[0][1]
            heappop(heap)
            sz -= 1
        ans = max(ans, sz)
    print(ans)

solver()