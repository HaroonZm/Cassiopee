import sys
def win(c, line):
	for i in range(0, 9, 3):
		if all(p == c for p in line[i:i + 3:1]):
			return True
	for i in range(3):
		if all(p == c for p in line[i:i + 9:3]):
			return True
	if all(p == c for p in line[0::4]): return True
	if all(p == c for p in line[2:8:2]): return True
	return False;
for line in sys.stdin:
	for c in ['o', 'x']:
		if win(c, line):
			print c
			break
	else:
		print 'd'