from sys import stdin, exit

def getint():
	try:
		return int(next(stdin_iter))
	except:
		exit()

stdin_iter = iter(stdin.readline, '')
while True:
	n = getint()
	a = list(map(int, next(stdin_iter).split()))
	a.sort()
	_ = [a.__setitem__(i+1, a[i+1]+a[i]) for i in range(n-1)]
	print(sum(a))