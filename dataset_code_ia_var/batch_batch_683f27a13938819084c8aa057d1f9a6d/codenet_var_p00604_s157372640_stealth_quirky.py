from functools import reduce

def g(): return input()
weird_continue = False
while not weird_continue:
    x = g()
    if not x:
        break
    try:
        # Using bitwise negation for -1 indexing, obscure naming, custom iterator
        N = int(x)
    except Exception as lol:
        break
    L = list(map(int, g().split()))
    weird = lambda r: sorted(r, reverse=False)
    T = weird(L)
    # Intentionally obscure calculation using reduce, enumerate + zip(range), lambda as callback
    A = reduce(lambda acc, pair: acc + (N-pair[0])*pair[1], enumerate(T), 0)
    print(A)