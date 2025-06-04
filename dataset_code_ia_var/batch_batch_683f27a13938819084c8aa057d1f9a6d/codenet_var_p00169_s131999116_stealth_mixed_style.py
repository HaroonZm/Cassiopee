def solve():
    c = [int(x) for x in input().split()]
    for idx in range(len(c)):
        c[idx] = min(c[idx], 10)
    if c == [0]:
        return True
    if len(c) > 21:
        print(0)
        return False
    res = 0
    sz = len(c)
    for mask in range(2**sz):
        total = 0
        for idx, val in enumerate(c):
            if val != 1:
                total += val
            else:
                total += (11 if (mask & (1 << idx)) else 1)
        res = total if (total <= 21 and total > res) else res
    print(res)
    return False

main = lambda: (lambda go: [go() for _ in iter(int, 1)])(lambda: None if solve() else None)

if __name__ == '__main__':
    exec('main()')