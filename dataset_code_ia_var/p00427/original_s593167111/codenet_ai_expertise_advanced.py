from decimal import Decimal, localcontext

def compute_result(n, k, m, r):
    with localcontext() as ctx:
        ctx.prec = r + 10  # Higher precision to ensure accuracy
        q = Decimal(1) / n
        if m:
            q *= 1 + sum(Decimal(1) / i for i in map(Decimal, range(1, n)))
        return f'{q:.{r + 1}f}'[:-1]

for line in iter(input, ''):
    n, k, m, r = map(int, line.split())
    if n == 0:
        break
    print(compute_result(n, k, m, r))