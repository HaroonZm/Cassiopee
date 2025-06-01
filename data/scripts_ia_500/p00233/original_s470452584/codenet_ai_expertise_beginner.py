import math

def func(n):
    if n == 0:
        return (0, 0)
    q = int(math.log10(abs(n)))
    if n * (-1) ** (q % 2) > 0:
        p = (-10) ** q * (n / (-10) ** q)
    else:
        p = (-10) ** (q + 1)
    r = n - p
    return (abs(int(p)), r)

def check_safe_oc(ans, ap):
    if ap == 0:
        return [True, 0]
    q = int(math.log10(ap))
    if ans == 0 or q > int(math.log10(ans)):
        return [True, q]
    anq = int((ans % 10 ** (q + 1)) / 10 ** q) * 10 ** q
    return [int(math.log10(ap + anq)) == q, q]

def addans(ans, ap):
    coc, q = check_safe_oc(ans, ap)
    if coc:
        ans += ap
    else:
        ans = int((ans / 10 ** (q + 1))) * 10 ** (q + 1) + ans % (10 ** q)
        ans += 9 * 10 ** (q + 1)
        ans = addans(ans, 10 ** (q + 2))
    return ans

while True:
    n = int(input())
    if n == 0:
        break
    ans = 0
    while n != 0:
        ap, n = func(n)
        ans = addans(ans, ap)
    print(ans)