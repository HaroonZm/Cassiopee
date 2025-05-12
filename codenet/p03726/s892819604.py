import sys
sys.setrecursionlimit(10**6)

n = int(input())
deg = [0 for _ in range(n)]
adj = [[] for _ in range(n)]
for _ in range(n-1):
	a, b = map(int, input().split())
	adj[a-1].append(b-1)
	adj[b-1].append(a-1)
	deg[a-1] += 1
	deg[b-1] += 1

M = max(deg)
if M == 1:
	print("Second")
elif M == 2:
	if n%2 == 1:
		print("First")
	else:
		print("Second")
else:
	for i in range(n):
		if deg[i] > 2:
			ori = i
			break

	l = [[] for _ in range(n)]
	def dfs(x, rt):
		cnt = 0
		for v in adj[x]:
			if v == rt:
				continue
			else:
				l[x].append(dfs(v, x))
				if l[x][-1] == 1:
					cnt += 1
		if not l[x]:
			return 1
		elif len(l[x]) == 1:
			return 1^l[x][0]
		elif cnt > 1:
			print("First")
			sys.exit()
		elif cnt == 1:
			return 0
		else:
			if x == ori:
				print("First")
				sys.exit()
			return 1

	dfs(ori, -1)
	print("Second")