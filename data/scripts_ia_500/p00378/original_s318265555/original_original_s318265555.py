import math

A, B, X = map(int, input().split())
if A<B:
	print(A*(-(-X//1000)))
elif A<2*B:
	C = A*(X//1000)
	if X%1000==0:
		pass
	elif X%1000<=500:
		C += B
	else:
		C += A
	print(C)
else:
	print(B*(-(-X//500)))