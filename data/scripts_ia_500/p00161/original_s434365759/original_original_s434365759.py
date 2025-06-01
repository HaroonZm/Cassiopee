# AOJ 0161 Sport Meet
# Python3 2018.6.18 bal4u

while True:
	n = int(input())
	if n == 0: break
	team = {}
	for i in range(n):
		a = list(map(int, input().split()))
		s = 0
		for j in range(1, 8, 2):
			s += 60*a[j] + a[j+1]
		team[a[0]] = s
	ans = sorted(team.items(), key=lambda x: x[1])
	print(ans[0][0], ans[1][0], ans[n-2][0], sep='\n')