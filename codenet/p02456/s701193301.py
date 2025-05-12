if __name__ == '__main__':

	n = int(input())
	S = set()

	for _ in range(n):
		x,y = map(int,input().split())
		if x == 0:
			S.add(y)
			print(len(S))
		elif x == 1:
			if y in S:
				print("1")
			else:
				print("0")
		else:
			S.discard(y)