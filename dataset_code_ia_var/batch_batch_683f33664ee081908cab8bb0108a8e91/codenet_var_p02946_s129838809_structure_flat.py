K_X = input().split()
K = int(K_X[0])
X = int(K_X[1])
min_x = X - (K - 1)
max_x = X + (K - 1)
result = []
for i in range(min_x, max_x + 1):
    result.append(str(i))
print(" ".join(result))