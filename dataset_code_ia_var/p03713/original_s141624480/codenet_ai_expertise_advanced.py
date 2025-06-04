from functools import partial

def solve(h, w):
    res = float('inf')
    for i in range(1, h):
        rects1 = (i * w, (h - i) * (w // 2), (h - i) * (w - w // 2))
        rects2 = (i * w, (h - i) // 2 * w, (h - i - (h - i) // 2) * w)
        res = min(res, max(rects1) - min(rects1), max(rects2) - min(rects2))
    return res

def main():
    h, w = map(int, input().split())
    print(min(partial(solve, h, w)(), partial(solve, w, h)()))

if __name__ == '__main__':
    main()