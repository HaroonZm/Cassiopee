N = int(input())
v = list(map(int,input().split()))
v = sorted(v)
Sum = 0
j = 0
for i in range(N-1):
    v[i+1] = (v[i]+v[i+1])/2
print(v[N-1])