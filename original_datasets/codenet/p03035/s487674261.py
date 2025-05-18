input = input().split()

listInt = [int(i) for i in input]

if listInt[0] >= 13:
	print(listInt[1])
elif listInt[0] > 5:
	print(int(listInt[1] / 2))
else:
	print(0)