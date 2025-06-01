# AOJ 0196 Baseball Championship
# Python3 2018.6.21 bal4u

while 1:
	n = int(input())
	if n == 0: break
	team = []
	for i in range(n):
		r = list(input().split())
		t = r.pop(0)
		w = l = 0
		for p in r:
			if int(p) == 0: w += 1      # 勝ち数
			elif int(p) == 1: l += 1    # 負け数
		team.append((t, i, w, l))
	for i in sorted(team, key=lambda x:(-x[2],x[3],x[1])): print(*i[0])