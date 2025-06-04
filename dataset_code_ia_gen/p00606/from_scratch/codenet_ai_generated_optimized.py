import sys

rooms = "ABCDEFGHI"
pos = {c: i for i, c in enumerate(rooms)}

# adjacency: from each room index, get list of reachable neighbors by directions: N,E,S,W
adj = {
    0: [1,3,-1,-1],
    1: [2,4,0,-1],
    2: [5,-1,1,-1],
    3: [4,6,-1,0],
    4: [5,7,3,1],
    5: [8,-1,4,2],
    6: [7,-1,-1,3],
    7: [8,-1,-1,4],
    8: [-1,-1,-1,5]
}

def solve(n, s, t, b):
    s_i = pos[s]
    t_i = pos[t]
    b_i = pos[b]

    # dp[battery_left][room] = probability to end in battery room starting with battery_left and at room 'room'
    # We want dp[n][s_i]
    dp = [[0]*(9) for _ in range(n+1)]
    # base case: battery 0, probability=1 if at battery room t_i, else 0
    for r in range(9):
        dp[0][r] = 1.0 if r == t_i else 0.0

    for battery in range(1, n+1):
        for r in range(9):
            res = 0.0
            for d in range(4):
                nr = adj[r][d]
                # If no room or junk room, do not move
                if nr == -1 or nr == b_i:
                    nr = r
                res += dp[battery-1][nr] * 0.25
            dp[battery][r] = res
    return dp[n][s_i]

input = sys.stdin.readline
while True:
    line = input()
    if not line:
        break
    n = int(line)
    if n == 0:
        break
    s,t,b = input().split()
    print(f"{solve(n,s,t,b):.8f}")