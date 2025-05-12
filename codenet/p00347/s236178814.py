from itertools import accumulate
import sys

sys.setrecursionlimit(1000000)

def main():
    w, h = map(int, input().split())
    mp = [list(map(int, input().split())) for _ in range(h)]
    acc_mp = list(map(lambda line:[0] + list(accumulate(line)), mp))
    mem = {}

    def score(x, y, turn):
        if (x, y) in mem:return mem[(x, y)]
        if y >= h:
            ret = 0
        elif x >= w:
            ret = acc_mp[y][x] + score(x, y + 1, 0)
        else:
            left = acc_mp[y][x]
            right = acc_mp[y][w] - left
            if turn == 0:
                ret = max(score(x + 1, y, 1), left - right + score(x, y + 1, 1))
            if turn == 1:
                ret = min(score(x + 1, y, 0), left - right + score(x, y + 1, 0))
        mem[(x, y)] = ret
        return ret

    print(abs(score(0, 0, 1)))

main()