def judge(stock, require):
	for i in range(0, len(stock)):
		if stock[i] < require[i]:
			return 'No'
	return 'Yes'

while True:
	inpt = map(int, raw_input().split())
	if inpt[0] == 0:
		break
	else:
		n = inpt[0]
		k = inpt[1]
		stock = map(int, raw_input().split())
		require = []
		for i in range(0, k):
			require.append(0)

		for i in range(0, n):
			blood = map(int, raw_input().split())
			for j in range(0, k):
				require[j] += blood[j]

		print judge(stock, require)