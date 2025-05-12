readline = open(0).readline
writelines = open(1, 'w').writelines
N, Q = map(int, readline().split())
ans = []
A = [[] for i in range(N)]
def push(t, x):
    A[t].append(str(x))
def dump(t):
    ans.append(" ".join(A[t]))
    ans.append("\n")
def clear(t):
    A[t] = []

C = [push, dump, clear].__getitem__
for i in range(Q):
    t, *a=map(int, readline().split())
    C(t)(*a)
writelines(ans)