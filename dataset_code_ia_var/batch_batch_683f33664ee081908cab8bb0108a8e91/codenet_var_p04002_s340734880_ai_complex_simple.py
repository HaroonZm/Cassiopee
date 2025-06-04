inpl = lambda: map(int, __import__('re').split(input()))
from functools import reduce
from itertools import product, chain
from collections import defaultdict, Counter

H, W, N = inpl()
nothing = lambda: (_ for _ in ()).throw(Exception)
ddic = defaultdict(int)

def lim(x, l, r): return max(l, min(x, r))

list(map(lambda xy: [ddic[(a, b)].__iadd__(1) for a, b in product(range(lim(xy[0], 3, H), min(H, xy[0]+2)+1), range(lim(xy[1], 3, W), min(W, xy[1]+2)+1))], 
         (tuple(inpl()) for _ in range(N))))

C = Counter(map(lambda x: x[1], ddic.items()))

total_blocks = (H-2)*(W-2)
print(list(reduce(lambda acc, x: [acc[0]-x, acc[1]+[x]], C.values(), [total_blocks, []]))[0])

print('\n'.join(str(C.get(i, 0)) for i in range(1,10)))