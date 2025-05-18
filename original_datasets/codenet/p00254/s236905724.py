from functools import reduce
while True:
	n = input()
	if n == "0000":
		break
	n = n if len(n) >= 4 else n.zfill(4)
	if reduce(lambda x,y:x and y,[n[0] == i for i in n]):
		print("NA")
	else:
		cnt = 0
		while n != "6174":
			s = ''.join(sorted(n))
			l = ''.join(sorted(n,reverse = True))
			n = str(int(l)-int(s))
			n = n if len(n) >= 4 else n.zfill(4)
			cnt += 1
		print(cnt)