def judge(stock, require):
	for i in range(len(stock)):
		if stock[i] < require[i]:
			return 'No'
	return 'Yes'

while True:
	inpt = list(map(int, raw_input().split()))
	if inpt[0] == 0:
		break
	n = inpt[0]
	k = inpt[1]
	stock = list(map(int, raw_input().split()))
	require = [0] * k
	for i in range(n):
		blood = list(map(int, raw_input().split()))
		for j in range(k):
			require[j] += blood[j]
	print judge(stock, require)