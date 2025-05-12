N = int(raw_input())
cost = [map(int,raw_input().split(" ")) for _ in range(N)]
all_cost = 0
for i in range(N):
	for j in range(i):
		all_cost += cost[i][j] if cost[i][j] <= cost[j][i] else cost[j][i]
print all_cost