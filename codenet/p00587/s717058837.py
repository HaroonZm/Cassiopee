# AOJ 1001: Binary Tree Intersection And Union
# Python3 2018.7.5 bal4u

def parse(p, i):
	global sz
	node[i][2] += 1
	del p[0]
	if p[0] != ',':
		if node[i][0] == 0:
			node[i][0] = sz
			sz += 1
		parse(p, node[i][0])
	del p[0]
	if p[0] != ')':
		if node[i][1] == 0:
			node[i][1] = sz
			sz += 1
		parse(p, node[i][1])
	del p[0]

def act(i, k):
	global ans
	if node[i][2] < k: return
	ans += '('
	if node[i][0] > 0: act(node[i][0], k)
	ans += ','
	if node[i][1] > 0: act(node[i][1], k)
	ans += ')'

while True:
	try: op, a, b = input().split()
	except: break
	sz = 1
	node = [[0 for j in range(3)] for i in range(210)]
	parse(list(a), 0)
	parse(list(b), 0)
	ans = ''
	act(0, 2 if op== 'i' else 1)
	print(ans)