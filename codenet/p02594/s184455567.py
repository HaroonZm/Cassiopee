import sys
for l in sys.stdin:
	a = int(l)
	if a >= 30:
		print("Yes")
	else:
		print("No")