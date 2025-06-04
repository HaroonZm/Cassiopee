import sys
sys.setrecursionlimit(10**7)

def can_place(card_set, table):
    return [c for c in card_set if c - 1 in table or c + 1 in table]

def solve(first_cards):
    second_cards = set(c for c in range(1,14) if c != 7) - set(first_cards)
    table = {7}
    memo = {}

    def dfs(f_cards, s_cards, turn):
        key = (tuple(sorted(f_cards)), tuple(sorted(s_cards)), turn)
        if key in memo:
            return memo[key]
        if not f_cards:
            memo[key] = True
            return True
        if not s_cards:
            memo[key] = False
            return False
        if turn == 0:
            places = can_place(f_cards, table)
            if places:
                for c in places:
                    table.add(c)
                    if dfs(f_cards - {c}, s_cards, 1):
                        table.remove(c)
                        memo[key] = True
                        return True
                    table.remove(c)
                memo[key] = False
                return False
            else:
                res = dfs(f_cards, s_cards, 1)
                memo[key] = res
                return res
        else:
            places = can_place(s_cards, table)
            if places:
                for c in places:
                    table.add(c)
                    # Opponent tries to prevent our win; all branches must lead us to failure to lose
                    if not dfs(f_cards, s_cards - {c}, 0):
                        table.remove(c)
                        memo[key] = False
                        return False
                    table.remove(c)
                memo[key] = True
                return True
            else:
                res = dfs(f_cards, s_cards, 0)
                memo[key] = res
                return res

    return dfs(set(first_cards), second_cards, 0)

input = sys.stdin.readline
N = int(input())
for _ in range(N):
    first = list(map(int, input().split()))
    print("yes" if solve(first) else "no")