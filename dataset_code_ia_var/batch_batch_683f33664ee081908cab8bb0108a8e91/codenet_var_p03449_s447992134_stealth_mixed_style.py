N=int(input())
row1 = input().split()
row2 = input().split()
A = [[int(x) for x in row1],[int(y) for y in row2]]

B = []
tmp1 = []
acc = 0
for idx, val in enumerate(A[0]):
    acc += val
    tmp1.append(acc)
B.append(tmp1)

B2 = [0]*N
B2[0]=A[0][0]+A[1][0]
for j in range(1,N):
    B2[j] = max(B2[j-1],B[0][j]) + A[1][j]
B.append(B2)

def last_val(matrix):
    return matrix[1][-1]
print(last_val(B))