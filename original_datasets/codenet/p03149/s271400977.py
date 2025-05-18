import sys
def input():
	return sys.stdin.readline().strip()

N = list(map(int, input().split()))

set1 = [1, 9, 7, 4]
set1 = set(set1)
set2 = set(N)
if set1 == set2:
	print("YES")
else:
	print("NO")