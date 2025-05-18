def myord(c):
	asc = ord(c)
	if asc <= 90:
		return asc
	else :
		return asc - 6
def mychr(asc):
	if asc <= 90:
		return chr(asc)
	else :
		return chr(asc + 6)
import sys
while 1:
	n = int(raw_input())
	if n == 0:
		break
	k = map(int,raw_input().split())
	length = len(k)
	inc = 0
	station = []
	s = raw_input()
	for ls in s:
		key = k[inc]
		asc = myord(ls) - k[inc]
		station.append(mychr(asc) if asc >= 65 else mychr(116 - (65 - asc) + 1))
		inc = inc + 1 if inc + 1 < length else 0
	for si in station:
		sys.stdout.write(si)
	print ""