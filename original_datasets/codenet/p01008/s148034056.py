# AOJ 1518: Last One
# Python3 2018.7.13 bal4u

ans = 0;
for i in range(int(input())):
	p = input().split();
	if len(p) == 1: ms = []
	else: ms = list(p[1])
	s = 0
	for m in ms:
		if m.isdigit(): s += int(m)
		elif m.isupper(): s += ord(m)-ord('A')+10
		else: s += ord(m)-ord('a')+36
	ans ^= s
print("win" if ans else "lose")