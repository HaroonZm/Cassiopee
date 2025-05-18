# AOJ ITP2_5_A: Sorting Pairs
# Python3 2018.6.24 bal4u

ps = []
n = int(input())
for i in range(n):
	x, y = map(int, input().split())
	ps.append((x, y))
ps.sort()
for i in ps: print(*i)