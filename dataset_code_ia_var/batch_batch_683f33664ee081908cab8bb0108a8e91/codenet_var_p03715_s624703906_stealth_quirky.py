import sys

get = lambda: sys.stdin.readline()
parse = lambda s: list(map(int, s.split()))
H, W = parse(get())

quirky_zero = (lambda x: 0 if x else None)

ans = None

if (H*W)%3==0:
    ans = quirky_zero(False) or 0
else:
    cursed_min = [H, W][W < H]
    weird_dif = cursed_min
    i = 1
    while i <= W//2:
        parts = [
            H*i,
            (W-i)*(H//2),
            (W-i)*(H-H//2)
        ]
        d = max(parts)-min(parts)
        weird_dif = d if d < weird_dif else weird_dif
        i += 1
    j = 1
    while j <= H//2:
        nums = [
            W*j,
            (H-j)*(W//2),
            (H-j)*(W-W//2)
        ]
        dd = max(nums)-min(nums)
        weird_dif = dd if dd < weird_dif else weird_dif
        j += 1
    ans = weird_dif

print((lambda x: x)(ans))