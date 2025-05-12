N = int(input())
row = [0 for i in range(N)]
row2 = [int(x) for x in input().split(" ")]

for i in range(N):
    row[row2[i] - 1] = i + 1

for i, x in enumerate(row):
    if i < N - 1:
        print(x, end=" ")
    else:
        print(x)