# AOJ 1063: Watchin' TVA
# Python3 2018.7.8 bal4u

while True:
	n = int(input())
	if n == 0: break
	dic, tbl = {}, []
	for i in range(n):
		nm, w, s = input().split()
		w, s = int(w), int(s)
		h, m = s//100, s%100
		s = (1440*w + h*60 + m) % 10080
		e = s + 30;
		tbl.append([s, e, 0, nm])
		dic[nm] = i
	for i in range(int(input())): tbl[dic[input()]][2] = 1
	if n == 1:
		print(1)
		continue
	tbl.sort(key=lambda x:(x[0],x[2]))
	for i in range(len(tbl)):
		if tbl[i][2]:
			k = i
			break
	ans, i, j = 1, k, k
	while True:
		j += 1
		if i >= n: i = 0
		if j >= n: j = 0
		if j == k: break
		e = tbl[i][1] - 10080 if tbl[i][1] >= 10080 else 0
		if (tbl[i][0] <= tbl[j][0] and tbl[j][0] < tbl[i][1]) \
		    or tbl[j][0] < e:
			if tbl[j][2] and tbl[i][2]:
				ans = -1
				break
			elif tbl[j][2]: i = j
		elif tbl[j][0] <= tbl[k][0] and tbl[k][0] < tbl[j][1]: pass
		else:
			ans += 1
			i = j
	print(ans)