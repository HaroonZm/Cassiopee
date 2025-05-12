D = input()
d1  = [raw_input().split() for i in range(input())]
p1  = sorted([int(i[1]) for i in d1 if i[0] == "D"])[::-1]
d2  = [raw_input().split() for i in range(input())]
p2  = sorted([int(i[1]) for i in d2 if i[0] == "DD"])[::-1]

ans = 0
for i in range(D+1):
	try:
		cur = sum(p1[:i]) + sum(p2[:(D-i)/2])
		ans = max(ans,cur)
	except:
		pass
print ans