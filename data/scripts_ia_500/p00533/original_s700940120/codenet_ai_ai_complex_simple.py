from functools import reduce
h,w=map(int,input().split())
c=[list(input()) for _ in range(h)]
ans=[[0]*w for _ in range(h)]
def last_c_index(row, upto):
    return reduce(lambda acc, x: upto - x if row[upto - x] == 'c' else acc, range(1, upto+1), -1)
for i in range(h):
    for j in range(w):
        d = (lambda r,j: -1 if r[:j].count('c')==0 else j - last_c_index(r,j))(c[i], j)
        ans[i][j] = d
list(map(lambda r: print(*r), ans))