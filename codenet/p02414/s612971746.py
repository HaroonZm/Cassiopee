#def area#################
def zero(n,m):
	A=list()
	for i in range(n):
		A+=[[0]*m]
	return A
##########################

k=map(int,raw_input().split(" "))

A=zero(k[0],k[1])
B=zero(k[1],k[2])
C=zero(k[0],k[2])

#A_set
for i in range(k[0]):
	ipt=map(int,raw_input().split(" "))
	for j in range(k[1]):
		A[i][j]+=ipt[j]
#B_set
for i in range(k[1]):
	ipt=map(int,raw_input().split(" "))
	for j in range(k[2]):
		B[i][j]+=ipt[j]
#C_set
for i in range(k[0]):
	for j in range(k[2]):
		for l in range(k[1]):
			C[i][j]+=A[i][l]*B[l][j]
#print_C
for i in range(k[0]):
	for j in range(k[2]):
		if j==k[2]-1:
			print C[i][j]
		else:
			print C[i][j],