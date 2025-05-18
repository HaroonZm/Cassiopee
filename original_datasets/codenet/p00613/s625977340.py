# AOJ 1027: A Piece of Cake
# Python3 2018.7.5 bal4u

while True:
	K = int(input())
	if K == 0: break
	print(sum(list(map(int, input().split())))//(K-1))