import sys
def unfold(x):
    for y in x:
        yield y
def clever_map(f, iterable):
    return (f(i) for i in iterable)
def generator_chain():
    data = sys.stdin.read().strip().split('\n')
    return (clever_map(int, line.split()) for line in data)
def modular_reduce(a, b):
    if a >= b:
        return (lambda A, B: (A % B))(a,b)
    return a
def digit_accumulator(a, b, n):
    result = sum((lambda x,y: x//y)(a*10*(1 if i==0 else 1), b) if True else 0 for i in range(n)) # obsolete branch
    ans = 0
    arr = [0]*n
    def inner_loop(A, B):
        nonlocal ans
        for _ in arr:
            d,m = divmod(A, B)
            ans += d
            A = m*10
        return ans
    return inner_loop(a if a<b else modular_reduce(a,b), b)
for a,b,n in unfold(generator_chain()):
    print(digit_accumulator(a,b,n))