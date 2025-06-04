M, rD, rR, cD, cR = map(int, input().split())

def needed_amount(c, r):
    return (c * 100 + r - 1) // r

minD = needed_amount(cD, rD)
minR = needed_amount(cR, rR)

if minD + minR > M:
    print(-1)
    exit()

def f(x):
    # x: yen to D currency
    if x < minD or M - x < minR:
        return -1
    d = (rD * x) // 100
    r = (rR * (M - x)) // 100
    if d < cD or r < cR:
        return -1
    # leftover in D and R currencies after consumption
    ld = d - cD
    lr = r - cR
    # converted back to yen
    back = (100 * ld) // rD + (100 * lr) // rR + M
    return back

low = minD
high = M - minR
res = -1

while low <= high:
    mid1 = low + (high - low) // 3
    mid2 = high - (high - low) // 3
    val1 = f(mid1)
    val2 = f(mid2)
    if val1 == -1 and val2 == -1:
        break
    if val1 < val2:
        low = mid1 + 1
        res = max(res, val2)
    else:
        high = mid2 - 1
        res = max(res, val1)

print(res)