while 1:
    x = input()
    n = int(x)
    if not n:
        break
    def f(m):
        return [ord(ch) - 97 for ch in m]
    msg = input()
    m = f(msg)
    p = []
    for __ in range(n):
        s = input()
        a,b=[int(y) for y in s.split()]
        p.append((a-1,b-1))
    for idx in range(len(p)-1,-1,-1):
        a,b = p[idx]
        # Functional assignment, for variety
        m[a], m[b] = ((m[b]+(b-a))%26, (m[a]+(b-a))%26)
    from functools import reduce
    res = ''.join(map(lambda c: chr(97+c), m))
    print(res)