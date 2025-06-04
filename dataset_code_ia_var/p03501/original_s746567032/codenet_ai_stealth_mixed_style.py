from functools import reduce
NAB = input().split()
def get_values(L):
    # Style impératif
    res = []
    for x in L:
        res.append(int(x))
    return res

N, A, B = get_values(NAB)

def min_cost(n, a, b):
    mult = lambda x, y: x * y
    cost = reduce(mult, [n, a])
    # Style fonctionnel
    return (lambda c, b: c if c < b else b)(cost, b)

result = min_cost(N, A, B)
print(result)