def return_cnt(x):
    ret = 0
    for value in (500, 100, 50, 10, 5, 1):
        ret += x // value
        x %= value
    return ret

def make_price(x, values, values_cnt):
    ret = 0
    for val, cnt in zip(values, values_cnt):
        use = min(x // val, cnt)
        ret += use
        x -= val * use
    if x == 0:
        return ret
    else:
        return 10**20

while 1:
    line = input()
    if not line or line.startswith('0'):
        break
    p, n1, n5, n10, n50, n100, n500 = map(int, line.split())
    values = [500, 100, 50, 10, 5, 1]
    values_cnt = [n500, n100, n50, n10, n5, n1]
    INF = float('inf')

    result = min([make_price(i, values, values_cnt) + return_cnt(i - p) for i in range(p, p + 500)])
    print(result)