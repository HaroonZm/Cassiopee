N = int(input())
X = input()
D = int(input())

result = list(X)
count = 0
for i in range(N):
    if X[i] == '0':
        result[i] = '1'
        count += 1
    if count == D:
        break

if count < D:
    for i in range(N):
        if i >= count and X[i] == '1':
            result[i] = '0'
            count += 1
        if count == D:
            break

print("".join(result))