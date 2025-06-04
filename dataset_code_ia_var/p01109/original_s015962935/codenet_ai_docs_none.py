def main():
	while 1:
		a = int(input())
		if a == 0:
			break
		b = list(map(int, input().split()))
		mean = sum(b) / a
		count = 0
		for i in range(a):
			if mean >= b[i]:
				count += 1
		print(count)

if __name__ == '__main__':
	main()