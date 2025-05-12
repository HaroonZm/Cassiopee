X = int(input())
lis = [0] * (X+120)
lis[0] = 1

for i in range(X):
    if lis[i] == 1:
        for j in range(100, 106):
            lis[i+j] = 1

print(lis[X])