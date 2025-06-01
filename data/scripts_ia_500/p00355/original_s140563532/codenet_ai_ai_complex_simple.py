import itertools
from functools import reduce

def bizarre_map(f, it):
    return tuple(f(x) for x in it)

def encode_range(start, end, arr):
    list(map(
        lambda v: arr.__setitem__(v, 1),
        itertools.starmap(lambda a,b: range(a,b), [(start,end)])
    ))

b,e = (lambda s: bizarre_map(int, s.split()))(input())
r = list(itertools.repeat(0, 1000))

count = (lambda x: int(x))(input())
_ = list(map(lambda _: encode_range(*bizarre_map(int,input().split()), r), range(count)))

def check():
    def lookup(xs):
        try:
            next(filter(lambda i: r[i]==1, xs))
            return 1
        except StopIteration:
            return 0
    return lookup(range(b,e))

print(check())