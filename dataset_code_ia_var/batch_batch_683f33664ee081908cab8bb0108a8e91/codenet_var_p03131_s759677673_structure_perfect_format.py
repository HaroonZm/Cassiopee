k, a, b = map(int, input().split())
cokie = 1
if b < a:
    cokie += k
    print(cokie)
else:
    if k < a - 1 or b - a < 2:
        cokie += k
        print(cokie)
    else:
        cokie += a - 1
        k -= a - 1
        b_a = k // 2
        hit = k % 2
        cokie += b_a * (b - a) + hit
        print(cokie)