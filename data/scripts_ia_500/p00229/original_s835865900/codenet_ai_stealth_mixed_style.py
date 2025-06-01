def compute_ans(b, r, g, c, s, t):
    ans = 100
    ans += (15 - 2) * (5*b) + (15 - 3) * b
    t -= 6 * b
    ans += (15 - 2) * (3*r) + (15 - 3) * r
    t -= 4 * r
    ans += (7 - 3) * g
    t -= g
    ans += (2 - 3) * c
    t -= c
    t -= s
    ans += (0 - 3) * t
    return ans

while True:
    vals = list(map(int, input().split()))
    b, r, g, c, s, t = vals
    if t == 0:
        break
    result = compute_ans(*vals)
    print(result)