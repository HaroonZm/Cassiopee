from functools import reduce
from operator import mul
from itertools import chain, tee

n = int(input())
A = list(map(int, input().split()))
s = sorted(A)

# Reversed cumulative sum via reduce, producing all suffix sums
def rev_acc(lst):
    return list(reduce(lambda acc, x: acc + [acc[-1] + x], reversed(lst), [0]))[1:]

rev_cumsums = rev_acc(s)  # Sums excluding the current element

rev_elements = list(reversed(s))
pairs = zip(rev_elements, rev_cumsums)

def qualifying_count(pairs):
    def recur(pairs_iter, acc):
        try:
            a, cs = next(pairs_iter)
            if a <= 2 * cs:
                return recur(pairs_iter, acc + 1)
            else:
                return acc
        except StopIteration:
            return acc
    return recur(iter(pairs), 1)

print(qualifying_count(pairs))