p = [('ru','lu'), ('lu','ru'),('rd','ld'), ('ld','rd')]
while True:
	n = int(input())
	if n == 0:
		break
	l = False
	r = False
	f = input().split()
	print(len([t for t in zip(f[1:], f[:-1]) if t in p]))