def correct(m, s):
	if m == "J":
		return s[-1] + s[:len(s)-1]
	elif m == "C":
		return s[1:] + s[0]
	elif m == "E":
		length = len(s)
		if length % 2 == 0:
			return s[length / 2:] + s[:length / 2]
		else :
			return s[(length+1) / 2:] + s[(length-1) / 2] + s[:(length-1) / 2]
	elif m == "A":
		return s[::-1]
	elif m == "P":
		cor = ""
		for si in s:
			if si.isdigit():
				cor += str(9 if int(si) == 0 else int(si) - 1)
			else :
				cor += si
		return cor
	else :
		cor = ""
		for si in s:
			if si.isdigit():
				cor += str(0 if int(si) == 9 else int(si) + 1)
			else :
				cor += si
		return cor

n = int(raw_input())
for i in range(n):
	messengers = raw_input()
	order_correct = messengers[::-1]
	cor = raw_input()
	for m in order_correct:
		cor = correct(m, cor)
	print cor