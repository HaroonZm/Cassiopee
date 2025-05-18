def inp():
	global n
	n = int(input())
	return n
def pos(p, l):
	global w
	if p < 0:
		return -1
	while l > 0 and p < n:
		l -= w[p]
		p += 1
		if l == 0:
			return p
	return -1
while inp() > 0:
	w = []
	for i in range(n):
		w.append(len(input()))
	for i in range(n):
		if pos(pos(pos(pos(pos(i,5),7),5),7),7) >= 0:
			print(i+1)
			break