while True:
	try:
		s = raw_input()
		t = raw_input()
		if len(s) < len(t):
			tmp = s
			s = t
			t = tmp
		ans = 0
		sp = 0
		while sp < len(t):
			if len(t) - sp <= ans:
				break
			L = ans
			while L < len(t) - sp + 1:
				if t[sp:sp+L] in s:
					ans = L
					L += 1
				else:
					break
			sp += 1
		print ans
	except:
		break