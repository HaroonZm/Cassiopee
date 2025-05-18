matrix = []
vector = []

n, m = map(int, input().split())

for i in range(n):
    matrix.append(list(map(int, input().split())))

for i in range(m):
    vector.append(int(input()))

for i in range(n):
    value = 0
    for j in range (m):
        value += matrix[i][j] * vector[j]
    print(value)