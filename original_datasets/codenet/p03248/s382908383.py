def main():
	s = input()
	if s[-1] == "1" or s[0] == "0":
		print(-1)
		return
	if s[0:-1][::-1] != s[:-1]:
		print(-1)
		return
	temp = 1
	init = []
	for i in range(1,int((len(s)+1)/2)):
		if s[i] == "1":
			for j in range(temp+1, i+2):
				print(temp, j, sep=" ")
			init += [temp]
			temp = i+2
	if temp != len(s):
		for j in range(temp+1, len(s)+1):
			print(temp, j, sep=" ")
	init += [temp]
	for i in range(len(init)-1):
		print(init[i], init[i+1], sep=" ")
	

main()