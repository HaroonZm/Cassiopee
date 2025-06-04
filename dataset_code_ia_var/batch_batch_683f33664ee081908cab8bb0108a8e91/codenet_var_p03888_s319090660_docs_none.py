from collections import defaultdict

def getlist():
	return list(map(int, input().split()))

def main():
	R1, R2 = getlist()
	ans = R1 * R2 / (R1 + R2)
	print(ans)

if __name__ == '__main__':
	main()