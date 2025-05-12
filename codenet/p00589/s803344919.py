# AOJ 1003: Extraordinary Girl II
# Python3 2018.7.4 bal4u

tbl = ["", "',.!?", "abcABC", "defDEF", "ghiGHI", "jklJKL", \
       "mnoMNO", "pqrsPQRS", "tuvTUV", "wxyzWXYZ"]

while True:
	try: s = input().strip()
	except: break
	ans, i = '', 0
	while i < len(s):
		c = s[i]
		w, d, i = 0, int(c), i+1
		while i < len(s) and s[i] == c: i, w = i+1, w+1
		if d == 0: ans += ' '*w
		else: ans += tbl[d][w%len(tbl[d])]
	print(ans)