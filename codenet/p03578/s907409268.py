N = int(input())
D = sorted(list(map(int, input().split())))
M = int(input())
T = sorted(list(map(int, input().split())))

j = -1
for i in T:
	j += 1
	while j<N and D[j]!=i:
		j += 1
	if j == N:
		print('NO')
		exit()
		
print('YES')