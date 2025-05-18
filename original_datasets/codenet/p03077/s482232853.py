N=int(input())
A=[]
for i in range (5):
	A.append(int(input()))
if N%min(A)==0:
	print(4+(N//(min(A))))
else:
	print(5+(N//(min(A))))