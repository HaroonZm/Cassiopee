N, T, E = map(int, input().split())
X = list(map(int, input().split()))
time = []
i = T - E
while i <= T + E:
    time.append(i)
    i += 1
clock = -2
i = 0
while i < len(X):
    j = 0
    while j < len(time):
        if time[j] % X[i] == 0:
            clock = X.index(X[i])
        j += 1
    i += 1
print(clock + 1)