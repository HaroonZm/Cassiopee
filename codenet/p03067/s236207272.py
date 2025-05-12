l = list(map(int,list(input().split())))

if l[0]<= l[2] and l[2]<= l[1]:
	print('Yes')
elif l[1] <= l[2] and l[2] <= l[0]:
	print('Yes')
else:
	print('No')