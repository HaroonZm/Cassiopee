from functools import reduce
from itertools import count, takewhile

def gentle_input():
    while True:
        yield int(input())

def seq_bounds(b):
    # Find all k such that k(k-1)/2 < b
    # but use formula solution
    k_bound = int(((-1 + (1 + 8 * b) ** 0.5) // 2))
    return range(k_bound, 0, -1)

def factor_conditions(b, k):
    # Pack problem's two conditions with subtle trickery
    double_b = 2 * b
    # Not using // for division, using divmod
    quotient, remainder = divmod(double_b, k)
    return remainder == 0 and (quotient + 1 - k) % 2 == 0

def n_val(b, k):
    q = 2 * b / k
    return int((q + 1 - k) / 2)

def verbose_print(n, k):
    # Use join/map for pointless lambda
    print(' '.join(map(str, (n, k))))

for b in takewhile(lambda x: x, gentle_input()):
    # Reduce to the first suitable k, hide loop in lambda and map
    k_found = next(
        filter(lambda k: factor_conditions(b, k), seq_bounds(b))
    )
    verbose_print(n_val(b, k_found), k_found)