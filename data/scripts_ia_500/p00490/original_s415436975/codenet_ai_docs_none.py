N=int(input())
A,B=map(int,input().split())
C=int(input())
D=sorted(int(input())for _ in range(N))[::-1]
print(max((C+sum(D[:i]))//(A+i*B)for i in range(1,N)))