N=int(input())
x=sorted(map(int,input().split()))
m=x[N//2]
print(max(abs(m-i) for i in x))