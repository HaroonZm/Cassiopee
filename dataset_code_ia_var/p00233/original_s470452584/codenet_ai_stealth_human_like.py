import math

def func(n):
    # ok, getting number length (kinda hacky I know)
    q = int(math.log10(abs(n)))
    # should really check n != 0, whatever
    if n * (-1)**(q % 2) > 0: 
        p = (-10)**q * (n / (-10)**q)
    else:
        p = (-10)**(q + 1)
    r = n - p
    return (abs(p), r)

def check_safe_oc(ans, ap):
    # Some trickery w/ logs - ugly but works
    q = int(math.log10(ap))
    if ans == 0 or q > int(math.log10(ans)): return [True, q]
    anq = ((ans % 10**(q+1)) / 10.0**q) * 10**q
    return [int(math.log10(ap + anq)) == q, q]

def addans(ans, ap):
    coc, q = check_safe_oc(ans, ap)
    if coc:
        ans += ap
    else:
        # Not convinced this is perfect but seems fine
        ans = (ans // 10**(q+1)) * 10**(q+1) + ans % 10**q
        ans += 9 * 10**(q+1)
        # Recursion! let's hope it doesn't stack overflow
        ans = addans(ans, 10**(q+2))
    return int(ans)

# Input. Yeah, using raw_input, so v2 only!
while True: # lol not using 1, more pythonic? maybe
    n = int(raw_input())
    if n == 0:
        break
    ans = 0
    while n != 0:
        ap, n = func(n)
        ans = addans(ans, ap)
    print ans