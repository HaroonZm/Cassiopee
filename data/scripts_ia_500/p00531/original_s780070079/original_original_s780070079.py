A = int(input())
B = int(input())
C = int(input())
D = int(input())
P = int(input())

X = P * A
Y = B
if P > C:
	Y = Y + D * (P - C)

if X > Y:
	print(int(Y))
else:
	print(int(X))