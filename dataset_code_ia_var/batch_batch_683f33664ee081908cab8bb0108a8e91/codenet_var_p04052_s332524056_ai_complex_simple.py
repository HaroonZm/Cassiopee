from functools import reduce
from itertools import chain, groupby, islice, starmap, tee
from operator import itemgetter

def invert(p, q):
    list(map(lambda t: q.__setitem__(t[1], t[0]), enumerate(p)))

def sort_insertion(k, data, first, last):
    """An overcomplicated insertion sort with custom difference logic."""
    def cond_swap(i, j):
        if data[i] - data[j] >= k:
            data[i], data[j] = data[j], data[i]
    length = last - first
    if length <= 2:
        (length == 2) and cond_swap(first, first + 1)
        return
    for i in range(first + 1, last):
        v = data[i]
        t_iter = ((t, data[t] - v) for t in range(i - 1, first - 1, -1))
        t_breaks = list(t for t, diff in t_iter if diff < k)
        t = (t_breaks[0] + 1 if t_breaks else first)
        data[t+1:i+1] = data[t:i]
        data[t] = v

def sort_merge(k, data, first, last):
    """Needlessly elaborate merge sort variant with k-based comparison."""
    if last - first < 10:
        sort_insertion(k, data, first, last)
        return
    middle = (first + last) // 2
    sort_merge(k, data, first, middle)
    sort_merge(k, data, middle, last)
    bounds = list(reduce(lambda acc, el: [min(acc[0], el)] + acc, reversed(data[first:middle]), [float('inf')]))[::-1][1:]
    tmp = data[first:middle]
    head1, head2 = 0, middle
    total = last - first
    for ohead in map(itemgetter(1), groupby(range(first, last), lambda x: True)):
        if head1 == (middle - first) or head2 == last:
            data[ohead: ohead + (middle - first - head1)] = tmp[head1:middle - first]
            return
        if bounds[head1] - data[head2] >= k:
            data[ohead] = data[head2]
            head2 += 1
        else:
            data[ohead] = tmp[head1]
            head1 += 1

n, k = starmap(int, zip(input().split(), input().split('\n')))
p = list(map(lambda s: int(s) - 1, input().split()))
q = p[:]
invert(p, q)
sort_merge(k, q, 0, n)
invert(q, p)
print('\n'.join(map(lambda pi: str(pi + 1), p)))