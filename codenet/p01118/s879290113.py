"""
スクリーンキーボード
https://onlinejudge.u-aizu.ac.jp/challenges/sources/ICPC/Prelim/1633

"""
import sys

def solve(h, w):
    keyboard = dict()
    for y in range(h):
        for x, ch in enumerate(input()):
            keyboard[ch] = (x, y)

    cx, cy = 0, 0
    ans = 0
    for ch in input():
        nx, ny = keyboard[ch]
        ans += (abs(nx - cx) + abs(ny - cy) + 1)
        cx, cy = nx, ny
    return ans

def main(args):
    while True:
        h, w = map(int, input().split())
        if h == 0 and w == 0:
            break
        ans = solve(h, w)
        print(ans)

if __name__ == '__main__':
    main(sys.argv[1:])