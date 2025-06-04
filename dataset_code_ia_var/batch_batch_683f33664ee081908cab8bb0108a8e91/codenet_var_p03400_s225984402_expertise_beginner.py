N = int(input())
D_X = input().split()
D = int(D_X[0])
X = int(D_X[1])
A = []
for i in range(N):
    A.append(int(input()))

def count(a):
    tmp = 1
    cnt = 0
    i = 1
    while tmp <= D:
        cnt = cnt + 1
        tmp = a * i + 1
        i = i + 1
    return cnt

cnt = 0
for a in A:
    cnt = cnt + count(a)

print(cnt + X)