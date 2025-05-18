if __name__ == '__main__':

	n = int(input())
	A = list(map(int,input().split()))

	n2 = int(input())

	for i in range(n2):
		b,e,k = map(int,input().split())

		print(A[b:e].count(k))