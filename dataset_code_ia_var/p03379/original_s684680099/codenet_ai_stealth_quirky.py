from sys import stdin

def get():
    return stdin.readline()

N = eval(get())
X = [*map(int,get().split())]
Y = sorted(X)
n = N//2
answers = {True: Y[n], False: Y[n-1]}
for k in range(N):
    e = X[k]
    print(answers[e <= Y[n-1]]) if e <= Y[n-1] or e >= Y[n] else None