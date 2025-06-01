import itertools as iit
s = lambda : map(int, raw_input().split())
def z(q, r, t):
    q[r][t] = 1 - q[r][t]
    for a,b in ((r-1,t),(r+1,t),(r,t-1),(r,t+1)):
        if 0<=a<10 and 0<=b<10:
            q[a][b] = 1 - q[a][b]
A = [[0]*10 for __ in range(10)]
for _ in range(input()):
    B = [s() for __ in range(10)]
    for c in iit.product((0,1), repeat=10):
        D = [row[:] for row in B]
        for idx, val in enumerate(c):
            if val: z(D,0,idx)
            A[0][idx] = val
        for row in range(9):
            for col in range(10):
                if D[row][col]:
                    z(D,row+1,col)
                    A[row+1][col] = 1
                else:
                    A[row+1][col] = 0
        if sum(D[9]) == 0:
            for line in A:
                print " ".join(str(x) for x in line)
            break