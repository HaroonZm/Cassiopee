from heapq import heappush, heappop

def read_input():
    S = input()
    K = int(input())
    return S, K

def initialize_cost(L, INF):
    cost = [[INF]*(L+1) for _ in range(L+1)]
    cost[0][L] = 0
    return cost

def process_queue(S, L, cost, INF):
    que = [(0, 0, L)]
    ss = []
    while que:
        d, a, b = heappop(que)
        if cost[a][b] < d:
            continue
        ss.append((a, b))
        only_one_character(a, b, d, cost)
        check_same_char(S, a, b, d, cost, que)
        handle_different_chars(S, a, b, d, cost, que)
    return ss

def only_one_character(a, b, d, cost):
    if a+1 == b:
        if d+1 < cost[a+1][b]:
            cost[a+1][b] = d + 1

def check_same_char(S, a, b, d, cost, que):
    if a+1 < b and S[a] == S[b-1]:
        if d+2 < cost[a+1][b-1]:
            cost[a+1][b-1] = d + 2
            if a+1 < b-1:
                heappush(que, (d+2, a+1, b-1))

def handle_different_chars(S, a, b, d, cost, que):
    if a+1 < b and S[a] != S[b-1]:
        if d+2 < cost[a+1][b]:
            cost[a+1][b] = d + 2
            if a+1 < b:
                heappush(que, (d+2, a+1, b))
        if d+2 < cost[a][b-1]:
            cost[a][b-1] = d + 2
            if a < b-1:
                heappush(que, (d+2, a, b-1))

def minimal_ln(cost, L):
    return min(cost[i][i] for i in range(L+1))

def initialize_dp(L, cost, ln):
    dp = [[0]*(L+1) for _ in range(L+1)]
    for i in range(L+1):
        if cost[i][i] == ln:
            dp[i][i] = 1
    return dp

def reverse_ss(ss):
    return ss[::-1]

def populate_dp(S, L, cost, dp, ss):
    for a, b in ss:
        d = cost[a][b]
        r = 0
        if a+1 == b:
            if d+1 == cost[a+1][b]:
                r = dp[a+1][b]
        else:
            if S[a] == S[b-1]:
                if d+2 == cost[a+1][b-1]:
                    r = dp[a+1][b-1]
            else:
                if d+2 == cost[a+1][b]:
                    r += dp[a+1][b]
                if d+2 == cost[a][b-1]:
                    r += dp[a][b-1]
        dp[a][b] = r

def check_none(a, b, dp, K):
    if dp[a][b] < K:
        print("NONE")
        return True
    return False

def reconstruct_string(S, L, cost, dp, K):
    SL = []
    SR = []
    a = 0
    b = L
    while a < b:
        if reconstruct_one_character(a, b, cost):
            SL.append(S[a])
            a += 1
            continue
        if S[a] == S[b-1]:
            reconstruct_same_char(a, b, S, cost, SL, SR)
            a += 1
            b -= 1
        elif S[a] < S[b-1]:
            c = (cost[a][b]+2 == cost[a+1][b])
            if c and K <= dp[a+1][b]:
                SL.append(S[a])
                SR.append(S[a])
                a += 1
            else:
                if c:
                    K -= dp[a+1][b]
                SL.append(S[b-1])
                SR.append(S[b-1])
                b -= 1
        else:
            c = (cost[a][b]+2 == cost[a][b-1])
            if c and K <= dp[a][b-1]:
                SL.append(S[b-1])
                SR.append(S[b-1])
                b -= 1
            else:
                if c:
                    K -= dp[a][b-1]
                SL.append(S[a])
                SR.append(S[a])
                a += 1
    SR.reverse()
    SL.extend(SR)
    print("".join(SL))

def reconstruct_one_character(a, b, cost):
    return a+1 == b and cost[a][b]+1 == cost[a+1][b]

def reconstruct_same_char(a, b, S, cost, SL, SR):
    assert cost[a][b]+2 == cost[a+1][b-1]
    SL.append(S[a])
    SR.append(S[b-1])

def solve():
    INF = 10**9
    S, K = read_input()
    L = len(S)
    cost = initialize_cost(L, INF)
    ss = process_queue(S, L, cost, INF)
    ln = minimal_ln(cost, L)
    dp = initialize_dp(L, cost, ln)
    ss_rev = reverse_ss(ss)
    populate_dp(S, L, cost, dp, ss_rev)
    if check_none(0, L, dp, K):
        return
    reconstruct_string(S, L, cost, dp, K)

solve()