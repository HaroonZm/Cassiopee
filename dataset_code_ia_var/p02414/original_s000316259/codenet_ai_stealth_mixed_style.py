def read_matrix(dim1):
    return [list(map(int, input().split())) for __ in range(dim1)]

nml = input().split()
n = int(nml[0])
m = int(nml[1])
l = int(nml[2])

M1 = []
i = 0
while i < n:
    M1 += [list(map(int, input().split()))]
    i+=1
M2 = read_matrix(m)

zip_cols = lambda mat: list(zip(*mat))

C = []
for ai in range(n):
    line = []
    for bj_col in zip_cols(M2):
        s, idx = 0, 0
        while idx < m:
            s += M1[ai][idx]*bj_col[idx]
            idx+=1
        line.append(s)
    C.append(line)

list(map(lambda r: print(' '.join([str(x) for x in r])), C))