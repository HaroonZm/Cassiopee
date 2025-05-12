# AOJ 1036: Monster Factory
# Python3 2018.7.6 bal4u

while True:
	in1 = list(input())
	if in1[0] == '-': break
	in2 = list(input())
	out = list(input())
	k = in2.pop(0)
	ans, f = '', True
	while len(in1) or len(in2):
		if len(out) and out[0] == k:
			k = in1.pop(0)
			del out[0]
		else:
			ans += k
			if len(in2): k = in2.pop(0)
			else:
				f = False
				break
	if f: ans += k
	print(ans)