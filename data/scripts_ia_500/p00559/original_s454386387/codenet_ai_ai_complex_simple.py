from functools import reduce
from operator import add
from itertools import islice, cycle

def clever_map(func, iterable):
    return list(map(func, iterable))

def complicated_sum(lst):
    return reduce(lambda x, y: x + y, lst, 0)

def nested_ternary(d, s, t):
    return (-s * d) if d > 0 else (-t * d)

n, q, s, t = (lambda x: tuple(map(int, x.split())))(input())
a_lst = (lambda n: list(reduce(lambda acc,_: acc + [int(input())], range(n+1), [])))(n)
diff = (lambda al: [al[i+1] - al[i] for i in range(len(al)-1)])(a_lst)
temp = complicated_sum([nested_ternary(d, s, t) for d in diff])

score = lambda d: (-s * d if d > 0 else -t * d)

for _ in range(q):
    l, r, x = tuple(map(int, input().split()))
    left_old = diff[l-1]
    diff[l-1] += x
    temp += score(diff[l-1]) - score(left_old)
    if r < n:
        right_old = diff[r]
        diff[r] -= x
        temp += score(diff[r]) - score(right_old)
    print(temp)