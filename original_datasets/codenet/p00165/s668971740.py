# AOJ 0165 Lottery
# Python3 2018.6.23 bal4u

#define MAX  1000000
#define SQRT 1000     // sqrt(MAX)

MAX = 1000000
SQRT = 1000     # sqrt(MAX)
comp = [0]*(MAX+2)

def sieve():
	for i in range(3, SQRT, 2):
		if comp[i] == 0:
			for j in range(i*i, MAX, i): comp[j] = 1
sieve()
tbl = [0]*(MAX+2)
tbl[2] = k = 1
for i in range(3, MAX, 2):
	if comp[i] == 0: k += 1
	tbl[i+1] = tbl[i] = k

while 1:
	n = int(input())
	if n == 0: break
	ans = 0;
	for i in range(n):
		p, m = map(int, input().split())
		a, b = p-m, p+m
		if a < 2: a = 2
		if b > 1000000: b = 1000000
		ans += tbl[b]-tbl[a-1] - 1;
	if ans < 0: ans = 0
	print(ans)