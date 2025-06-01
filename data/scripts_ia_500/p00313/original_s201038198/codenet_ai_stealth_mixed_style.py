def inp2list():
    return [int(x) for x in input().split()][1:]

N = int(input())
A = inp2list()
B = inp2list()
C = inp2list()

R = list(False for _ in range(N))
for i in C:
    if i not in A or i in B:
        R[i-1] = True

print(sum(True for x in R if x))