n = int(input())
x = list(map(int, input().split()))
y = list(map(int, input().split()))

n_dis = [0 for _ in range(3)]
elem_dis = [abs(x[i]-y[i]) for i in range(n)]

for p in range(3):
    for i in range(n):
        n_dis[p] += elem_dis[i]**(p+1)
    n_dis[p] = n_dis[p]**(1/(p+1))
    print(n_dis[p])
    
index = [i for i, j in enumerate(elem_dis) if j == max(elem_dis) ]
print(elem_dis[index[0]])