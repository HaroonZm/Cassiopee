import itertools

A1 = [int(i) for i in input().split()]
A2 = [int(i) for i in input().split()]
A3 = [int(i) for i in input().split()]
A = [A1, A2, A3]

f = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

N = int(input())
b = []
for _ in range(N):
    b += input().split()
b = list(map(int, b))

for i in range(3):
    for j in range(3):
        for x in b:
            if A[i][j] == x:
                f[i][j] = 1

s = 0

if f[0][0] + f[0][1] + f[0][2] == 3:
    s = 1
if f[1][0] + f[1][1] + f[1][2] == 3:
    s = 1
if f[2][0] + f[2][1] + f[2][2] == 3:
    s = 1
if f[0][0] + f[1][0] + f[2][0] == 3:
    s = 1
if f[0][1] + f[1][1] + f[2][1] == 3:
    s = 1
if f[0][2] + f[1][2] + f[2][2] == 3:
    s = 1
if f[0][0] + f[1][1] + f[2][2] == 3:
    s = 1
if f[0][2] + f[1][1] + f[2][0] == 3:
    s = 1

if s == 1:
    print("Yes")
else:
    print("No")