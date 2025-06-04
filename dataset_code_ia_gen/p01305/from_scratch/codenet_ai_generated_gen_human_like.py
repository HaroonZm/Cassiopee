import sys
sys.setrecursionlimit(10**7)

def solve(gates, jackie):
    gates.sort()
    jackie.sort()
    n = 9
    total = 0
    gates_win = 0
    jackie_win = 0

    def dfs(g_used, j_used, g_score, j_score):
        nonlocal total, gates_win, jackie_win
        if len(g_used) == n and len(j_used) == n:
            total += 1
            if g_score > j_score:
                gates_win += 1
            elif j_score > g_score:
                jackie_win += 1
            return

        for gi in range(n):
            if gi in g_used:
                continue
            for ji in range(n):
                if ji in j_used:
                    continue
                g_used.add(gi)
                j_used.add(ji)
                g_card = gates[gi]
                j_card = jackie[ji]
                if g_card > j_card:
                    dfs(g_used, j_used, g_score + g_card + j_card, j_score)
                elif j_card > g_card:
                    dfs(g_used, j_used, g_score, j_score + g_card + j_card)
                else:
                    # cards differ, so no tie possible in this problem input
                    dfs(g_used, j_used, g_score, j_score)
                g_used.remove(gi)
                j_used.remove(ji)

    dfs(set(), set(), 0, 0)
    return gates_win / total, jackie_win / total

input = sys.stdin.readline
t = int(input())
for _ in range(t):
    gates = list(map(int, input().split()))
    jackie = list(map(int, input().split()))
    g_prob, j_prob = solve(gates, jackie)
    print(f"{g_prob:.5f} {j_prob:.5f}")