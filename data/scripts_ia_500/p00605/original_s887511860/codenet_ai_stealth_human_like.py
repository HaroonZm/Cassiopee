def judge(stock, require):
	# Check if stock meets all requirements
	for i in range(len(stock)):
		if stock[i] < require[i]:
			return 'No'  # Not enough stock
	return 'Yes'  # All requirements met

while True:
	# Read input; map to int directly
	inpt = map(int, raw_input().split())
	if inpt[0] == 0:
		break  # Terminate if first input is 0
	else:
		n = inpt[0]
		k = inpt[1]
		stock = map(int, raw_input().split())  # Available stock
		require = [0] * k  # Initialize requirements with zeros

		for _ in range(n):
			blood = map(int, raw_input().split())
			for j in range(k):
				require[j] += blood[j]  # Accumulate requirements per type

		print judge(stock, require)  # Output result

# Could be more pythonic but this works fine I guess