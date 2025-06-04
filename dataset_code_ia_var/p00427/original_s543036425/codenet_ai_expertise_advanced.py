from decimal import Decimal, localcontext, ROUND_HALF_UP
from itertools import count, islice
from sys import stdin

def harmonic_sum(n):
    # Efficient harmonic sum calculation using generator expression
    return sum(Decimal(1) / Decimal(i) for i in range(1, n))

def format_decimal(val, r):
    # Advanced formatting: round and keep r decimals (plus "0.")
    with localcontext() as ctx:
        ctx.prec = r + 5  # extra precision for calculations
        ctx.rounding = ROUND_HALF_UP
        val = +val  # applies the context (rounding, etc)
        val = str(val.quantize(Decimal('1.' + '0'*r)))
        # In case exponent notation is returned
        if 'E' in val or 'e' in val:
            val = '{0:.{1}f}'.format(float(val), r)
        return val

for line in stdin:
    n, k, m, r = map(int, line.split())
    if n == 0:
        break

    with localcontext() as ctx:
        ctx.prec = r + 5  # guard digits for intermediate calculations
        ctx.rounding = ROUND_HALF_UP
        ans = Decimal(1) / Decimal(n)
        if m == 1:
            ans *= 1 + harmonic_sum(n)
        print(format_decimal(ans, r))