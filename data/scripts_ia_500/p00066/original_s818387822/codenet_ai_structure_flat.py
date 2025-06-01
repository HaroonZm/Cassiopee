import sys
for line in sys.stdin:
	line = line.rstrip('\n')
	found = False
	for c in ['o', 'x']:
		if (line[0] == c and line[1] == c and line[2] == c) or (line[3] == c and line[4] == c and line[5] == c) or (line[6] == c and line[7] == c and line[8] == c) or (line[0] == c and line[3] == c and line[6] == c) or (line[1] == c and line[4] == c and line[7] == c) or (line[2] == c and line[5] == c and line[8] == c) or (line[0] == c and line[4] == c and line[8] == c) or (line[2] == c and line[4] == c and line[6] == c):
			print c
			found = True
			break
	if not found:
		print 'd'