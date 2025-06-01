from functools import reduce
from operator import itemgetter

def op1(p):
    return tuple(reduce(lambda acc, idx: acc + (p[idx],),
                        [0,1,2,3,4,5,21,22,23,11,10,9,17,13,14,15,16,12,18,19,20,6,7,8,24,25,26,27,28,29],
                        ()))

def op2(p):
    index_order = [27,28,29,3,4,5,6,7,8,9,10,11,12,13,15,14,16,17,20,19,18,21,22,23,24,25,26,0,1,2]
    return tuple(map(p.__getitem__, index_order))

def op3(p):
    index_order = [23,1,2,26,4,5,29,7,8,20,10,11,12,13,14,17,16,15,18,19,9,21,22,0,24,25,3,27,28,6]
    return tuple(p[i] for i in index_order)

def op4(p):
    return tuple(map(lambda x: p[x],
        [0,1,21,3,4,24,6,7,27,9,10,18,14,13,12,15,16,17,11,19,20,2,22,23,5,25,26,8,28,29]))

def op(p,i):
    return [None, op1, op2, op3, op4][i](p)

def check_range_equal(p, indexes):
    return not any(p[indexes[0]] != p[i] for i in indexes[1:])

def valid(p):
    clusters = [
        list(range(1,9)),        # positions 1 to 8
        list(range(22,30)),      # 22 to 29
        list(range(10,12)),      # 10 to 11
        list(range(13,15)),      # 13 to 14
        list(range(16,18)),      # 16 to 17
        list(range(19,21))       # 19 to 20
    ]
    base_idxs = [0,21,9,12,15,18]
    # Validate clusters for equal values
    for base, cluster in zip(base_idxs, clusters):
        if not check_range_equal(p, [base] + cluster):
            return False
    q = tuple(itemgetter(*base_idxs)(p))
    valid_qs = {
        (0,1,3,5,4,2),
        (0,3,5,4,1,2),
        (0,5,4,1,3,2),
        (0,4,1,3,5,2),
        (2,1,5,3,4,0),
        (2,5,3,4,1,0),
        (2,3,4,1,5,0),
        (2,4,1,5,3,0),
    }
    return q in valid_qs

def solve(n,p,i):
    global minimum
    if n > 9 or n >= minimum:
        return
    if valid(p):
        minimum = min(minimum,n)
        return
    list(map(lambda j: solve(n+1, op(p,j), j) if j != i else None, range(1,5)))

minimum = 100
N = int(input())
for _ in range(N):
    minimum = 100
    p = tuple(map(lambda x: int(x)-1, input().split()))
    if valid(p):
        print(0)
        continue
    list(map(lambda i: solve(1, op(p,i), i), range(1,5)))
    print(minimum)