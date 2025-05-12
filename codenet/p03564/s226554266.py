N = int(input())
K = int(input())

val = 1
for i in range(N):
	val += min(val,K)
	

print(val)