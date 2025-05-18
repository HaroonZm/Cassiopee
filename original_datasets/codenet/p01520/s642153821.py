N, T, E = map(int, input().split())
X = list(map(int, input().split()))

time = [i for i in range(T - E, T + E + 1)]

clock = -2

for i in range(len(X)) :
    for j in range(len(time)) :
        if time[j] % X[i] == 0 :
            clock = X.index(X[i])
            
print(clock + 1)