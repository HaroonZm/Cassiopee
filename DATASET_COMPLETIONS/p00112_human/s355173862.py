while 1:
	n = int(raw_input())
	if n == 0:
		break;
	
	li = []
	t = 0
	for i in range(n):
		li.append(int(raw_input()))
	
	li.sort()
	for i in range(n - 1, 0, -1):
		t += i * li[n - i - 1]
		
	print t