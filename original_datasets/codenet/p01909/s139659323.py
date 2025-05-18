# AOJ 2809: Graduation Ceremony
# Python3 2018.7.11 bal4u

MAX = 2002
dx = (0,1,0,-1)   # URDL
dy = (-1,0,1,0)
tr = {'U':0, 'R':1, 'D':2, 'L': 3}

S = list(input())
K = int(input())
u, d, l, r = [0]*MAX, [0]*MAX, [0]*MAX, [0]*MAX
for s in S:
	dir = tr[s]
	j2 = j = K
	while j > 0:
		j -= 1
		u[j2] = min(-d[j], u[j2])+dy[dir]
		r[j2] = max(-l[j], r[j2])+dx[dir]
		d[j2] = max(-u[j], d[j2])+dy[dir]
		l[j2] = min(-r[j], l[j2])+dx[dir]
		j2 -= 1
	r[0] = l[0] = l[0]+dx[dir]
	u[0] = d[0] = d[0]+dy[dir]
ans = 0;
for i in range(K+1):
	j  = max(-l[i], r[i])
	j2 = max(-u[K-i], d[K-i])
	j += j2;
	if j > ans: ans = j
print(ans)