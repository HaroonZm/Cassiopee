"""Minimum cost Sort."""

def make_cycle(A):
    """Return a list which has the minimum element of A and
    switch elements cycles as list.

    A is a list whose elements' type is 'int'.

    Each cycle list has its minimum elements in the first index.
    """
    B = list(A)
    B.sort()
    cycle_list = [B[0]]
    for i, b in enumerate(B):
        if b != None:
            new_cycle = []
            new_cycle.append(b)
            B[i] = None
            si = A.index(b)
            while si != i:
                st = B[si]
                new_cycle.append(st)
                B[si] = None
                si = A.index(st)
            cycle_list.append(new_cycle)
    return cycle_list

def min_sorting_cost(A):
    """Return the minimum cost of sorting A.

    A is a list whose elements' type is 'int'.
    """
    cycles = make_cycle(A)
    min_w = cycles[0]
    cost = 0
    for c in cycles[1:]:
        n = len(c)
        min_cw = c[0]
        dec = (n - 1) * (min_cw - min_w)
        inc = 2 * (min_w + min_cw)
        if dec < inc:
            cost += sum(c) + min_cw * (n - 2)
        else:
            cost += sum(c) + min_cw * (n - 2) - dec + inc
    return cost

n = int(input())

A = list(map(int, input().split()))

ans = min_sorting_cost(A)

print(ans)