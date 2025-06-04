Q = int(input())
for _ in range(Q):
    c, a, n = map(int, input().split())
    teams_CCA = min(c // 2, a) if a > 0 else 0
    teams_CCC = c // 3
    teams_CAN = min(c, a, n)
    print(max(teams_CCA, teams_CCC, teams_CAN))