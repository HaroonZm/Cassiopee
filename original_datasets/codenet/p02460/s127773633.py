if __name__ == '__main__':

	n = int(input())
	d = {}

	for i in range(n):
		cmd = input().split()
		if cmd[0] == "0":
			d[cmd[1]] = cmd[2]
		elif cmd[0] == "1":
			if cmd[1] in d:
				print(d[cmd[1]])
			else:
				print("0")
		else:
			if cmd[1] in d:
				del d[cmd[1]]