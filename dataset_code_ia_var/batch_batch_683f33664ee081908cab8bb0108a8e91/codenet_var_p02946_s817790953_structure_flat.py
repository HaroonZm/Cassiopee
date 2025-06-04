K_X = input().split()
K = int(K_X[0])
X = int(K_X[1])
i = X - K + 1
while i < X + K:
    print(i)
    i += 1