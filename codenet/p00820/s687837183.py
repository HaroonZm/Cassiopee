R = 2**15+1
r = 182
s = [i*i for i in range(r)]
L = [0]*R
for i in range(r):
	for j in range(i,r):
		for k in range(j,r):
			for l in range(k,r):
				if s[i]+s[j]+s[k]+s[l] < R:
					L[s[i]+s[j]+s[k]+s[l]] += 1

while 1:
	n = input()
	if n == 0: break
	print L[n]