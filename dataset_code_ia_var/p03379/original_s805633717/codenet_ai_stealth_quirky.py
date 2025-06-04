N = eval(input())
X = list(map(lambda z:int(z), input().split()))
Y = X[:]
Y.sort()
i = 0
while i < N:
    print([Y[N//2], Y[N//2-1]][X[i] >= Y[N//2]])
    i += 1