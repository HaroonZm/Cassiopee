X, Y, Z = map(int, input().split())

W = Y
Y = X
X = W

A = Z
Z = X
X = A

print(X , Y , Z)