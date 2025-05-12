if __name__ == '__main__':
	
	n = int(input())

	for i in range(21):
		s = pow(2,i)
		if n < s:
			if i == 0:
				print(1)
			else:
				print(pow(2,i-1))
			break
		elif n == s:
			print(pow(2,i))
			break