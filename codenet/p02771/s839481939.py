A,B,C=map(int, input().split())
if A==B and A!=C:print("Yes")
	
elif A==C and B!=C:print("Yes")

elif C==B and A!=C:print("Yes")

else:print("No")