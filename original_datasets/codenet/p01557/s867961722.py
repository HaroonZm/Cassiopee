from functools import lru_cache
import sys
from collections import deque
sys.setrecursionlimit(1000000)
	
sorted_a = ""
m = dict({})

N = int(input())
A = ''.join(list(map(lambda x: str(int(x)-1), input().split())))
sorted_a = ''.join(list(sorted(A)))

q = deque()
q.append((A, 0))
m[A] = 0
while True:
	a, x = q.popleft()
	if a in m and m[a] < x:
		continue
	if x == (len(a)-1) // 2:
		break;

	for i in range(len(a)):
		for j in range(i+2, len(a)+1):
			next_a = a[:i:] + a[::-1][len(a)-j:len(a)-i:] + a[j::]
			if next_a in m:
				continue

			q.append((next_a, x+1))
			m[next_a] = x+1
			
m2 = dict({})
q = deque()
q.append((sorted_a, 0))
m2[sorted_a] = 0
while True:
	a, x = q.popleft()
	if a in m2 and m2[a] < x:
		continue
	if x == (len(a)-1) // 2:
		break;

	for i in range(len(a)):
		for j in range(i+2, len(a)+1):
			next_a = a[:i:] + a[::-1][len(a)-j:len(a)-i:] + a[j::]
			if next_a in m2:
				continue
			q.append((next_a, x+1))
			m2[next_a] = x+1

ret = sys.maxsize
for a, x in m.items():
	if a in m2:
		ret = min(ret, x + m2[a])
	
if ret == sys.maxsize:
	print(len(A) - 1)
else:
	print(ret)