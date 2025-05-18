import sys
def input():
	return sys.stdin.readline().strip()

N = 1407
K = 38

num_all = [[0]*K for _ in range(N)]

for i in range(K):
	num_all[0][i] = i + 1
num = 1
for i in range(K):
	for j in range(K - 1):
		num_all[num][0] = i + 1
		num += 1
num = K + 1
for i in range(1, K):
	for j in range(1, K):
		num_all[i][j] = num
		num += 1

for n in range(2, K + 1):
	for j in range(K - 1):
		for i in range(K - 1):
			num = K + 1 + j*(K - 1) + i
			loc = K + (n - 2)*(K - 1) + ((i + j*(n - 2))%(K - 1))
			num_all[loc][j + 1] = num

def list_print(A):
	length = len(A)
	for i in range(length - 1):
		print(A[i], end="")
		print(" ", end="")
	print(A[- 1])

list_print([N, K])
  
for i in range(N):
	list_print(num_all[i])