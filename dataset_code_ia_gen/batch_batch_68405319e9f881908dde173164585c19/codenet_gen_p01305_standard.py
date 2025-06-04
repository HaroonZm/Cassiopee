import sys
from math import comb

sys.setrecursionlimit(10**7)

def dfs(gate_cards, jacky_cards, g_used, j_used, g_score, j_score, cache):
    if (g_used, j_used) in cache:
        return cache[(g_used, j_used)]

    n = len(gate_cards)
    turn = bin(g_used).count("1")
    if turn == n:
        if g_score > j_score:
            return (1, 0)
        elif g_score < j_score:
            return (0, 1)
        else:
            return (0, 0)

    g_win, j_win = 0, 0
    for i in range(n):
        if not (g_used & (1 << i)):
            for j in range(n):
                if not (j_used & (1 << j)):
                    g_c = gate_cards[i]
                    j_c = jacky_cards[j]
                    g_s, j_s = g_score, j_score
                    if g_c > j_c:
                        g_s += g_c + j_c
                    elif g_c < j_c:
                        j_s += g_c + j_c
                    res = dfs(gate_cards, jacky_cards, g_used | (1 << i), j_used | (1 << j), g_s, j_s, cache)
                    g_win += res[0]
                    j_win += res[1]
    cache[(g_used, j_used)] = (g_win, j_win)
    return (g_win, j_win)

def main():
    input = sys.stdin.readline
    T = int(input())
    for _ in range(T):
        gate_cards = list(map(int, input().split()))
        jacky_cards = list(map(int, input().split()))
        cache = {}
        g_win, j_win = dfs(gate_cards, jacky_cards, 0, 0, 0, 0, cache)
        total = g_win + j_win
        if total == 0:
            print("0.00000 0.00000")
        else:
            print(f"{g_win/total:.5f} {j_win/total:.5f}")

if __name__ == "__main__":
    main()