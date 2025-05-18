A, B, C = map(int,input().split())
K = int(input())

ans = 0
X = [0]*3 #X[0]:red X[1]:green X[2]:blue
for i in range(K + 1):
    for j in range(K + 1 - i):
        X[0] = A*2**i
        X[1] = B*2**j
        X[2] = C*2**(K - i - j)
        if X[1] > X[0] and X[2] > X[1]:
            ans = 1
print("Yes" if ans == 1 else "No")