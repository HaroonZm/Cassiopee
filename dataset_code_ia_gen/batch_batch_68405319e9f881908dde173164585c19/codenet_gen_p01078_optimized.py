import math
N,K=map(int,input().split())
M=N//math.gcd(N,K)
area=M*math.sin(2*math.pi*K*M/N)/2
print(f"{area:.8f}")