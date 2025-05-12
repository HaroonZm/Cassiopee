N = int(input())
K = int(input())
X = int(input())
Y = int(input())
if N > K:
    x = X*K
    y = (N-K)*Y
    print(x+y)
else:
    print(N*X)