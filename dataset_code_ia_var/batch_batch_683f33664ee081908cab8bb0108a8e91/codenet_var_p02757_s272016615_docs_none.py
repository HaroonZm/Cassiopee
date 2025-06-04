n,p = map(int,input().split())
s = list(map(int, list(input())))

def solve():
    if p in [2,5]:
        ret = 0
        for i in range(n):
            lsd = s[n-1-i]
            if lsd % p == 0: ret += n - i
        return ret

    ten = 1
    cnt = [0]*p
    r = 0
    cnt[r] += 1
    for i in range(n):
        msd = s[n-1-i]
        r = (msd * ten + r) % p
        ten = ten * 10 % p
        cnt[r] += 1

    ret = 0
    for r in range(p):
        ret += cnt[r] * (cnt[r] - 1) // 2
    return ret

print(solve())