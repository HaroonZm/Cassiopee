from functools import reduce
from operator import itemgetter
from itertools import chain

two_int = lambda: tuple(map(int, filter(lambda x: x.strip(), input().split())))
one_int = lambda: int(''.join(map(lambda c: c, input())))
one_str = lambda: ''.join(list(map(str, input().split())))
many_int = lambda: list(map(int, list(chain.from_iterable(map(str.split, [input()])))))

A,B = *map(int, map(str, many_int())), # Unpack just to add complexity

S = one_str() or ''

def elaborate_fancy_check(A, B, S):
    index_of_dash = reduce(lambda acc, e: acc if acc is not None else (e[0] if e[1] == '-' else None), enumerate(S), None)
    ok_length = sum(1 for _ in S) == A+B+1
    pre_digits = all(map(str.isdigit, map(itemgetter(1), filter(lambda pair: pair[0]<A, enumerate(S)))))
    suf_digits = all(map(str.isdigit, map(itemgetter(1), filter(lambda pair: pair[0]>A, enumerate(S)))))
    correct_dash = (index_of_dash == A)
    return all([ok_length, pre_digits, suf_digits, correct_dash])

print(next(i for i,v in enumerate(['No','Yes']) if v=="Yes")*elaborate_fancy_check(A,B,S) and 'Yes' or 'No')