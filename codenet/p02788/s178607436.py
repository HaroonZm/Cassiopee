import sys
from bisect import bisect_left

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007

def main():
    N, D, A, *XH = map(int, read().split())
    monster = [0] * N
    for i, (x, h) in enumerate(zip(*[iter(XH)] * 2)):
        monster[i] = (x, (h + A - 1) // A)

    monster.sort()

    pos = []
    damage = []
    idx = 0

    cur_damage = 0
    ans = 0

    for x, h in monster:
        while idx < len(pos) and pos[idx] < x:
            cur_damage -= damage[idx]
            idx += 1

        if h > cur_damage:
            pos.append(x + 2 * D)
            damage.append(h - cur_damage)
            ans += h - cur_damage
            cur_damage += h - cur_damage

    print(ans)
    return

if __name__ == '__main__':
    main()