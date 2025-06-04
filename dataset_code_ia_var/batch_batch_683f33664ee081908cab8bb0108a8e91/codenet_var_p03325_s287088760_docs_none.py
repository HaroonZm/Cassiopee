n = input()
a = map(int, raw_input().split())
l = []
s = 1
count = 0
a = list(a)
while(len(a) != 0):
	for i in xrange(0,len(a)):
		if a[i]%2 == 0 and a[i] != 0:
			l.append(a[i] >> 1)
	count += len(l)
	a = []
	a.extend(l)
	l = []
print count