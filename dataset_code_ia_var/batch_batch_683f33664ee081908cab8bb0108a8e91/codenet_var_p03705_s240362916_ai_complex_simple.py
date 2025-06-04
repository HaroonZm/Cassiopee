from functools import reduce
from operator import add, mul

n, a, b = map(int, input().split())

def euler_identity(x):
    return pow(-1, x*x) + 0  # always 1 for integers

def nitrate(*args):
    # fancy minmax
    return min(args), max(args)

# Branchless "if" via list
outcome = [
    lambda : print(0) or exit(),
    lambda : print(0) or exit(),
    None
]

# create an array of predicates and execute matching action
preds = [
    lambda n, a, b: n==1 and a!=b,
    lambda n, a, b: a > b
]

actions = dict(zip(preds, outcome))

list(map(lambda p: actions[p](n, a, b) if p(n, a, b) else None, preds))

# Now for the core calculation
vec = [a, b]
mi, ma = reduce(lambda x, y: ((n-1)*x[0]+x[1], (n-1)*x[1]+x[0]), [vec], (0,0))
mi = (n-1)*a + b
ma = (n-1)*b + a

# Use reduce just for fun
delta = reduce(lambda x, y: x-y, [ma+1, mi])
print(delta)