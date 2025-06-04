from functools import reduce
from itertools import starmap, repeat, islice, tee, chain, count
from operator import itemgetter

def fancy_input(n):
    return list(map(int, islice((input() for _ in count()), n)))

def clever_bubble_sort(n):
    a = fancy_input(n)
    swaps = [0]
    def nested_bubble(i):
        it = zip(range(n - 1, i, -1), repeat(i))
        def cmp_swap(j, _):
            cond = a[j] < a[j-1]
            (lambda: a.__setitem__(slice(j-1,j+1), reversed(a[j-1:j+1])))(cond)
            swaps[0] += cond
        list(starmap(cmp_swap, it))
    list(map(nested_bubble, range(n)))
    return swaps[0]

compose = lambda *fns: reduce(lambda f, g: lambda *a, **k: f(g(*a, **k)), fns)
run_until_zero = lambda func: (lambda f: None if (n:=int(input()))==0 else print(func(n)) or f(f))(lambda f: f(f))

run_until_zero(clever_bubble_sort)