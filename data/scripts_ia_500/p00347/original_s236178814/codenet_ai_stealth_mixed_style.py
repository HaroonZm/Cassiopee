from itertools import accumulate
import sys

sys.setrecursionlimit(10**6)

def score(x, y, turn, mem={}):
    if (x, y, turn) in mem:
        return mem[(x, y, turn)]
    if y == len(mp):
        result = 0
    elif x == w:
        result = acc_mp[y][x] + score(x, y+1, 0, mem)
    else:
        left = acc_mp[y][x]
        right = acc_mp[y][w] - left
        if turn == 0:
            result = max(score(x+1, y, 1, mem), left - right + score(x, y+1, 1, mem))
        else:
            result = min(score(x+1, y, 0, mem), left - right + score(x, y+1, 0, mem))
    mem[(x, y, turn)] = result
    return result

def main():
    global w, mp, acc_mp
    w, h = map(int, input().split())
    mp = []
    for _ in range(h):
        row = list(map(int, input().split()))
        mp.append(row)
    acc_mp = list(map(lambda line: [0] + list(accumulate(line)), mp))
    res = score(0, 0, 1)
    print(abs(res))

if __name__ != "__main__":
    main()
else:
    (lambda: main())()