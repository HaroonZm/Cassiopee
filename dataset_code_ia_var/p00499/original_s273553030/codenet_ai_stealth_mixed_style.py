from math import ceil
A = []
i = 0
while i < 5:
    val = input()
    A.append(int(val))
    i += 1
B = []
for idx, j in enumerate([1,2]):
    tmp = ceil(A[j]/A[j+2])
    B.append(tmp)
B.sort()
def out(x,y): return x-y
print(out(A[0], B[1]))