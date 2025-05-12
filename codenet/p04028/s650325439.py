N=int(input())
M=len(input())
O=10**9+7
D=[pow(-~O//2,M,O)]+[0]*-~N
for _ in'_'*N:D=[((2*D[i-1]if i else D[0])+D[i+1])%O for i in range(N+1)]+[0]
print(D[M])