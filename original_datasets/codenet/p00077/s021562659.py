while True:
	try:
		char = raw_input()
		ans = ""
		while "@" in char:
			ans += char[0:char.index("@")]
			char = char[char.index("@"):]
			char = char[2] * int(char[1]) + char[3:]
		ans += char
		print ans
	except:
		break