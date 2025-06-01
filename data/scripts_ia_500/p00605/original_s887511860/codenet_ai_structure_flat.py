while True:
	inpt = map(int, raw_input().split())
	if inpt[0] == 0:
		break
	n = inpt[0]
	k = inpt[1]
	stock = map(int, raw_input().split())
	require = []
	for i in range(k):
		require.append(0)
	for i in range(n):
		blood = map(int, raw_input().split())
		for j in range(k):
			require[j] += blood[j]
	yesno = 'Yes'
	for i in range(k):
		if stock[i] < require[i]:
			yesno = 'No'
	print yesno