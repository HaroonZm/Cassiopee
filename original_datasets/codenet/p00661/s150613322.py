# AOJ 1076 Time Manipulation
# Python3 2018.7.10 bal4u

while True:
	n, m = map(int, input().split())
	if n == 0: break
	p = list(map(int, input().split()))
	if 1 in p: n = 0
	print(n/2)