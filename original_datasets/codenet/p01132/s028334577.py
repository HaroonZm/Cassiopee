def opt_change(n):
	change = [0,0,0,0]
	purse = (10,50,100,500)
	for i in range(4):
		change[3-i] = n / purse[3-i]
		n = n % purse[3-i]
	return change

flag = 0
while 1:
	price = int(raw_input())
	if price == 0:
		break
	if flag == 0:
		flag = 1
	else :
		print "" 
	purse_num = map(int,raw_input().split())
	purse = [10,50,100,500]
	own = sum([purse[i] * purse_num[i] for i in range(4)])
	result = opt_change(own-price)
	for i in range(4):
		num = 0 if purse_num[i] <= result[i] else (purse_num[i] - result[i])
		if num != 0:
			print purse[i], num