x,y,z,d=map(int,input().split())
if abs(x-z)<=d:
	print("Yes")
elif abs(x-y)<=d and abs(y-z)<=d:
	print("Yes")
else:
	print("No")