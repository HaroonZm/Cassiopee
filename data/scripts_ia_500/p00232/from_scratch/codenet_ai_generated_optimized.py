import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline

while True:
    X,Y,Z = map(int, input().split())
    if X==0 and Y==0 and Z==0:
        break
    V = list(map(int, [input() for _ in range(X)]))
    events = {}
    for _ in range(Z):
        N_,E_,A_ = map(int, input().split())
        events[N_] = (E_,A_)

    from functools import lru_cache

    base_prob = 1/X

    @lru_cache(None)
    def dfs(pos,money):
        if pos >= Y:
            return money
        exp = 0
        for v in V:
            next_pos = pos + v
            next_money = money
            if next_pos >= Y:
                exp += base_prob * next_money
                continue
            if next_pos in events:
                E_, A_ = events[next_pos]
                if E_ == 1:
                    # advance A_ steps ignoring further events
                    final_pos = next_pos + A_
                    if final_pos >= Y:
                        exp += base_prob * next_money
                    else:
                        exp += base_prob * dfs(final_pos, next_money)
                elif E_ == 2:
                    next_money2 = next_money + A_
                    exp += base_prob * dfs(next_pos, next_money2)
                else:
                    next_money2 = max(0, next_money - A_)
                    exp += base_prob * dfs(next_pos, next_money2)
            else:
                exp += base_prob * dfs(next_pos, next_money)
        return exp

    ans = dfs(0,0)
    print(int(ans))