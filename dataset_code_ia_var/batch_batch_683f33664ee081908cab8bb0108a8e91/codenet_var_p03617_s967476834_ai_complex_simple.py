from functools import reduce
from itertools import product

Q, H, S, D = map(int, input().split())
N = int(input())

unit_cost = reduce(lambda x, y: x if x < y else y, map(lambda t: sum(p * c for p, c in zip(t, [Q, H, S, D])), [(4,0,0,0),(0,2,0,0),(0,0,1,0),(0,0,0,2)][:3]))
double_cost = min([sum(p*c for p,c in zip(t, [Q,H,S,D])) for t in product((0,4,0,0),(0,2,0,0),(0,0,1,0),(0,0,0,2))][:,None][:4]])

result = (lambda x, y, u, d: d*(x//2) + u*(x%2))(N, D, unit_cost, min(q*8, h*4, s*2, d) if any([N//2, N%2]) else 0)
print(result)