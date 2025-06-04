from functools import reduce
from operator import mul, truediv as div
from itertools import takewhile, count

diglen = lambda n: next(i for i in count(1) if abs(n) < 10**i)

func = lambda n: (
    abs(sum(
        lambda x: [(((-10)**(diglen(n)-1))*(div(n, ((-10)**(diglen(n)-1))))),
                   (-10)**diglen(n)][x>0]
        for x in [n*((-1)**((diglen(n)-1)%2))]
    )),
    n-abs(sum(
        lambda x: [(((-10)**(diglen(n)-1))*(div(n, ((-10)**(diglen(n)-1))))),
                   (-10)**diglen(n)][x>0]
        for x in [n*((-1)**((diglen(n)-1)%2))]
    ))
))

def check_safe_oc(ans, ap):
    ln = len(str(ap))-1
    if ans == 0 or ln > len(str(ans))-1:
        return [True, ln]
    anq = int(str(ans)[-ln-1] if ln+1 <= len(str(ans)) else 0) * 10**ln
    return [len(str(ap+anq))-1 == ln, ln]

def addans(ans, ap):
    coc, q = check_safe_oc(ans, ap)
    if coc:
        return ans+ap
    else:
        _ = int(ans / (10**(q+1))) * 10**(q+1) + ans % 10**q
        _ += 9 * 10**(q+1)
        return addans(_, 10**(q+2))

while True:
    try:
        n = int(input())
    except EOFError:
        break
    if n == 0:
        break
    ans = 0
    while n != 0:
        ap, n = func(n)
        ans = addans(ans, ap)
    print(ans)