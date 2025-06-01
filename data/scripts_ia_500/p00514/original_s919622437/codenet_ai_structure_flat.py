import math
n, m, r = map(int, input().split())
a = r - n * m
if a < 0:
    print(0)
else:
    if 0 <= a + n - 1 and a <= a + n - 1:
        fact_p = math.factorial(a + n - 1)
        fact_q = math.factorial(a)
        fact_p_q = math.factorial(n - 1)
        print(fact_p // (fact_q * fact_p_q))
    else:
        print(0)