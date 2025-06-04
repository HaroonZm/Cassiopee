(n, m, l) = [int(k) for k in input().split()]
import sys

def create_matrix(rows, cols):
  return [[0]*cols for _ in range(rows)]
A = create_matrix(n, m)
B = [[0 for _ in range(l)] for __ in range(m)]
C = []
for row_idx in range(n):
    vals = input().split()
    def fill_row(row, vals):
        for w in range(m):
            row[w] = int(vals[w])
    fill_row(A[row_idx], vals)
for _ in range(m):
    s = input().split()
    k = 0
    while k < l:
        B[_][k] = int(s[k])
        k += 1
C = []
for t in range(n):
    new_row = []
    for y in range(l):
        sm = sum([A[t][z]*B[z][y] for z in range(m)])
        new_row.append(sm)
    C.append(new_row)
for num in range(len(C)):
    j = 0
    while j < len(C[num]):
        print(C[num][j], end='\n' if j==l-1 else ' ')
        j += 1