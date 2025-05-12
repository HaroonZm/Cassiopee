from math import sqrt
MAX = 2**15-1
ub = int(sqrt(MAX))
square_sum = [[0 for i in range(MAX)] for j in range(4)]
for k in range(1,ub+1):
	square_k = k**2
	square_sum[0][square_k-1] = 1 
	for j in range(3):
		for i in range(1,MAX - square_k + 1):
			if square_sum[j][i-1] >= 1:
				square_sum[j+1][i-1+square_k] += square_sum[j][i-1]
while 1:
	n = int(raw_input())
	if n == 0:
		break
	print sum(square_sum[i][n-1] for i in range(4))