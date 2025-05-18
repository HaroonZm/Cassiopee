A = list(map(int,input().split(" ")))
A = sorted(A)
print(abs(A[3]+A[0]-A[1]-A[2]))