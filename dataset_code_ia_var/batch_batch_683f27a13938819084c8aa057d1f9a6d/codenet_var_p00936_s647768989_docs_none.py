def solve():
    N = int(input())
    c = [int(i) for i in input().split()]
    if N == 1:
        return c[0]*2
    r = c[0]*2
    x = [c[0]]
    for i in range(1,N):
        r_ = c[i]
        r_n = r_
        for j in range(i):
            b = c[j]
            x_ = x[j]
            dt = 2*((r_*b)**(1/2))
            x_ += dt
            r_n = max(r_n, x_)
        x.append(r_n)
        if r < r_n + r_:
            r = r_n + r_
    return r

print(solve())