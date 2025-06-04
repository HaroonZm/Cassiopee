N = int(input())
row = []
for i in range(N):
    row.append(0)
row2 = input().split(" ")
for i in range(N):
    row2[i] = int(row2[i])
for i in range(N):
    row[row2[i] - 1] = i + 1
for i in range(N):
    if i < N - 1:
        print(row[i], end=" ")
    else:
        print(row[i])