L=list(map(int,input().split()))
if L[0]+L[1]==L[2]+L[3]:
	print("Balanced")
elif L[0]+L[1]>L[2]+L[3]:
	print("Left")
else:
	print("Right")