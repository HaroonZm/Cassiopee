n=int(input())
for i in range(n):
	A=[]
	string=input()
	for j in string:
		A.append(j)
	A.sort(reverse=True)
	Max="".join(A)
	A.sort()
	Min="".join(A)
	Min=int(Min)
	Max=int(Max)
	print(Max-Min)