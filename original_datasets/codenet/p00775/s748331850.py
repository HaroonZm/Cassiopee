from math import sqrt
def inpl(): return list(map(int, input().split()))
R, N = inpl()
while R:
    H = [0] * 41
    r0 = 0
    l0 = 0
    for _ in range(N):
        l, r, h = inpl()
        if l < 0 and r >= 0:
            l0 = max(l0, h)
        if l <= 0 and r > 0:
            r0 = max(r0, h)

        l += (l <= 0)
        r -= (r >= 0)

        for i in range(l, r+1):
            if i != 0:
                H[i+20] = max(H[i+20], h)
    H[20] = min(l0, r0)
    ans = 20
    for x in range(-R+1, R):
        time = R - sqrt(R**2 - x**2) + H[x+20]
        ans = min(ans, time)
    print(ans)
    R, N = inpl()